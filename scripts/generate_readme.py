from rocrate.rocrate import ROCrate
import json
from pathlib import Path
import pandas as pd
from humanize import naturalsize
import re

def get_create_action(crate, datafile):
    actions = crate.get_by_type("CreateAction")
    for action in actions:
        props = action.properties()
        for result in props["result"]:
            if result["@id"] == datafile:
                return action

crate = ROCrate("./")
root = crate.get("./").properties()
gw_section = crate.get(root["mainEntityOfPage"]["@id"])
code_repo = crate.get(root["isBasedOn"]["@id"])
md = f"# {root['name']}\n\n"
md += f"{root['description']}\n\n"
if version := root.get("version"):
    md += f"CURRENT VERSION: {version}\n\n"
md += f"These datasets were generated using notebooks in the [{code_repo['name']}]({code_repo['url']}) repository.\n\n"
md += f"For more information and documentation see the [{gw_section['name']}]({gw_section['url']}) section of the [GLAM Workbench](https://glam-workbench.net)."
md += "\n\n## Dataset summary\n"
details = "\n\n## Dataset details"

for datafile in crate.get_by_type("Dataset"):
    if datafile.id != "./" and not datafile.id.startswith("http"):
        details += f"\n\n### [{datafile['name']}]({datafile['url']})\n\n"
        action = get_create_action(crate, datafile["@id"])
        nb = crate.get(action["instrument"]["@id"])
        file_path = Path(datafile.get("name"))
        if file_path.is_dir():
            md += f"- [{datafile['name']}]({datafile['url']}) (directory containing {datafile['size']:,} files)\n"
            stats = {
                "date harvested": datafile["dateModified"],
                "number of files": f"{datafile['size']:,}",
                "format": "directory",
                "created by": f"<a href='{nb['url']}'>{nb['name']}</a> ([documentation]({nb['mainEntityOfPage']['@id']}))"
            }
        else:
            format = datafile.get("encodingFormat")
            if not format:
                format = datafile["name"].split(".")[-1]
            md += f"- [{datafile['name']}]({datafile['url']}) ({naturalsize(datafile['contentSize'])}, {format})\n"
            stats = {
                "date harvested": datafile["dateModified"],
                "file size": naturalsize(datafile["contentSize"]),
                "format": format,
                "created by": f"<a href='{nb['url']}'>{nb['name']}</a> ([documentation]({nb['mainEntityOfPage']['@id']}))"
            }
            if rows := datafile.get("size"):
                stats["number of rows"] = rows
        if query := action.get("query"):
            stats["query"] = f"`{query}`"
        if description := datafile.get("description"):
            stats["description"] = description
        if licence_id := datafile.get("license"):
            licence = crate.get(licence_id["@id"])
            stats["license"] = f"[{licence['name']}]({licence['url']})"
        #details += pd.DataFrame([stats]).T.style.format(thousands=",").hide(axis=1).to_markdown() + "\n\n"
        details += pd.DataFrame([stats]).T.to_markdown(headers=["",""]) + "\n\n"

        if "conformsTo" in datafile:
            details += "#### Columns\n\n"
            with Path(datafile["conformsTo"]["@id"]).open() as json_file:
                df = pd.json_normalize(json.load(json_file), record_path="fields")
            df["name"] = df["name"].apply(lambda x: f"`{x}`")
            details += df.to_markdown(index=False)

if "workExample" in root:
    details += "## Examples of use\n\n"
    for example_id in root["workExample"]:
        example = crate.get(example_id["@id"]).properties()
        details += f"- [{example['name']}]({example['url']})\n"

md += details

md += "\n\n----\nCreated by [Tim Sherratt](https://timsherratt.au) for the [GLAM Workbench](https://glam-workbench.net)"

md = re.sub(r'<style type="text/css">\s*</style>', '', md)
Path("README.md").write_text(md)
