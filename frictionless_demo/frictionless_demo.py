# Importations.
import frictionless
import pandas as pd

#############################
### Command line syntax.
#############################

# View first 4 lines of data file.
! cat merops_peptidase_families.csv | sed '1,4!d'

# Describe data file's inferred schema.
! frictionless describe merops_peptidase_families.csv

# Extract normalized data that conforms to inferred schema.
# E.g. invalid cells removed.
! frictionless extract merops_peptidase_families.csv | sed '1,10!d'

# Validate data file.
! frictionless validate merops_peptidase_families.csv

#############################
### Python syntax.
#############################

# View first 4 lines of data file.
df = pd.read_csv("merops_peptidase_families.csv")
display(df.head(4))

# Describe data file's inferred schema.
frictionless.describe("merops_peptidase_families.csv")

# Extract normalized data that conforms to inferred schema.
# E.g. invalid cells removed.
frictionless.extract("merops_peptidase_families.csv")[:4]

# Validate data file.
frictionless.validate("merops_peptidase_families.csv")
