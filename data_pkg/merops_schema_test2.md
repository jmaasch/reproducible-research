# MEROPS Peptidase Families Data Package

All human (Homo sapiens) peptidase families available in the MEROPS Peptidase Database (https://www.ebi.ac.uk/merops/index.shtml). Data were scraped using a custom Python script in July 2020.

- licenses: CC0-1.0 (https://creativecommons.org/publicdomain/zero/1.0/)
- missing values represented by: `[""]`
- keywords:
  - peptide
  - peptidase
  - protease
  - proteinase
  - proteolytic cleavage
  - cleavage site
  - protein
  - MEROPS
  - bioinformatics
  - protein informatics

## Data model

This data model relies on the 5 following fields corresponding to the columns of the tabular file.

### `Family`

- title: 
- description: Peptidase family
- type: string

### `Subfamily`

- title: 
- description: Peptidase subfamily
- type: string

### `Type enzyme`

- title: 
- description: Peptidase enzyme type
- type: string

### `Group`

- title: 
- description: Peptidase group
- type: string

