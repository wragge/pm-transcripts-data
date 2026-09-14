# pm-transcripts-data

The Department of Prime Minister and Cabinet's [PM Transcripts site](https://pmtranscripts.pmc.gov.au) provides transcripts of more than 20,000 speeches, media releases, and interviews by Australian Prime Ministers. These transcripts can be searched online, and the underlying XML files can be downloaded using a simple API. This repository includes transcripts harvested from the PM Transcripts site, together with a CSV index, and aggregations of transcripts by Prime Minister.

These datasets were generated using notebooks in the [GitHub - GLAM-Workbench/pm-transcripts · GitHub](https://github.com/GLAM-Workbench/pm-transcripts/) repository.

For more information and documentation see the [PM Transcripts data - GLAM Workbench](https://www.glam-workbench.net/pm-transcripts/pm-transcripts-data/) section of the [GLAM Workbench](https://glam-workbench.net).

## Dataset summary
- [pms/combined](https://github.com/wragge/pm-transcripts-data/tree/main/pms/combined) (directory containing 18 files)
- [pms/zips](https://github.com/wragge/pm-transcripts-data/tree/main/pms/zips) (directory containing 18 files)
- [pms/speech](https://github.com/wragge/pm-transcripts-data/tree/main/pms/speech) (directory containing 18 files)
- [transcripts](https://github.com/wragge/pm-transcripts-data/tree/main/transcripts) (directory containing 28,560 files)
- [index.csv](https://github.com/wragge/pm-transcripts-data/blob/main/index.csv) (4.9 MB, text/csv)


## Dataset details

### [pms/combined](https://github.com/wragge/pm-transcripts-data/tree/main/pms/combined)

|                 |                                                                                                                                                                                                                          |
|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| date harvested  | 2026-09-12                                                                                                                                                                                                               |
| number of files | 18                                                                                                                                                                                                                       |
| format          | directory                                                                                                                                                                                                                |
| created by      | <a href='https://github.com/GLAM-Workbench/pm-transcripts/blob/main/aggregate_transcripts.ipynb'>Aggregate transcripts by PM</a> ([documentation](https://www.glam-workbench.net/pm-transcripts/aggregate_transcripts/)) |
| description     | One text file for each Prime Minister containing the aggregated contents of all the XML transcript files.                                                                                                                |
| license         | [Creative Commons Attribution 4.0 International  Licence](https://creativecommons.org/licenses/by/4.0/)                                                                                                                  |
| copyright       | Commonwealth of Australia                                                                                                                                                                                                |



### [pms/zips](https://github.com/wragge/pm-transcripts-data/tree/main/pms/zips)

|                 |                                                                                                                                                                                                                          |
|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| date harvested  | 2026-09-12                                                                                                                                                                                                               |
| number of files | 18                                                                                                                                                                                                                       |
| format          | directory                                                                                                                                                                                                                |
| created by      | <a href='https://github.com/GLAM-Workbench/pm-transcripts/blob/main/aggregate_transcripts.ipynb'>Aggregate transcripts by PM</a> ([documentation](https://www.glam-workbench.net/pm-transcripts/aggregate_transcripts/)) |
| description     | One zip file for each Prime Minister containing the aggregated XML transcript files.                                                                                                                                     |
| license         | [Creative Commons Attribution 4.0 International  Licence](https://creativecommons.org/licenses/by/4.0/)                                                                                                                  |
| copyright       | Commonwealth of Australia                                                                                                                                                                                                |



### [pms/speech](https://github.com/wragge/pm-transcripts-data/tree/main/pms/speech)

|                 |                                                                                                                                                                                                                          |
|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| date harvested  | 2026-09-10                                                                                                                                                                                                               |
| number of files | 18                                                                                                                                                                                                                       |
| format          | directory                                                                                                                                                                                                                |
| created by      | <a href='https://github.com/GLAM-Workbench/pm-transcripts/blob/main/aggregate_transcripts.ipynb'>Aggregate transcripts by PM</a> ([documentation](https://www.glam-workbench.net/pm-transcripts/aggregate_transcripts/)) |
| description     | One text file for each Prime Minister containing the aggregated contents of all the XML transcript files identified as speeches in the file metadata.                                                                    |
| license         | [Creative Commons Attribution 4.0 International  Licence](https://creativecommons.org/licenses/by/4.0/)                                                                                                                  |
| copyright       | Commonwealth of Australia                                                                                                                                                                                                |



### [transcripts](https://github.com/wragge/pm-transcripts-data/tree/main/transcripts)

|                 |                                                                                                                                                                                                              |
|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| date harvested  | 2026-09-12                                                                                                                                                                                                   |
| number of files | 28,560                                                                                                                                                                                                       |
| format          | directory                                                                                                                                                                                                    |
| created by      | <a href='https://github.com/GLAM-Workbench/pm-transcripts/blob/main/harvest_transcripts.ipynb'>Harvest transcripts</a> ([documentation](https://www.glam-workbench.net/pm-transcripts/harvest_transcripts/)) |
| description     | The complete collection of XML-formatted transcript files downloaded from PM Transcripts.                                                                                                                    |
| license         | [Creative Commons Attribution 4.0 International  Licence](https://creativecommons.org/licenses/by/4.0/)                                                                                                      |
| copyright       | Commonwealth of Australia                                                                                                                                                                                    |



### [index.csv](https://github.com/wragge/pm-transcripts-data/blob/main/index.csv)

|                |                                                                                                                                                                                                                                                                     |
|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| date harvested | 2026-09-12                                                                                                                                                                                                                                                          |
| file size      | 4.9 MB                                                                                                                                                                                                                                                              |
| format         | text/csv                                                                                                                                                                                                                                                            |
| created by     | <a href='https://github.com/GLAM-Workbench/pm-transcripts/blob/main/index_and_analyse_transcript_metadata.ipynb'>Create an index to the harvested files</a> ([documentation](https://www.glam-workbench.net/pm-transcripts/index_and_analyse_transcript_metadata/)) |
| number of rows | 28561                                                                                                                                                                                                                                                               |
| description    | A CSV file containing metadata extracted from the transcript XML files.                                                                                                                                                                                             |
| license        | [CC0 Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/)                                                                                                                                                                                  |

#### Columns

| name           | type    | description                                              |
|:---------------|:--------|:---------------------------------------------------------|
| `id`           | integer | transcript identifier                                    |
| `title`        | string  | title of the transcript                                  |
| `pm`           | string  | name of the Prime Minister                               |
| `date`         | date    | date the text was issued/created                         |
| `release_type` | string  | type of transcript, eg: speech, interview, press release |
| `subjects`     | string  | subjects covered by the transcript                       |
| `pdf`          | string  | link to a PDF version (where available)                  |

----
Created by [Tim Sherratt](https://timsherratt.au) for the [GLAM Workbench](https://glam-workbench.net)