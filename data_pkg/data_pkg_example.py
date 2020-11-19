# Constructing a basic data package.
#
# The following code constructs and explores a basic data package.
# This data package collates metadata for a dataset scraped from
# the MEROPS Peptidase Database in June 2020.
# (https://www.ebi.ac.uk/merops/index.shtml).
#
# More information on programmatically creating data packages
# can be found here:
# https://frictionlessdata.io/tooling/data-package-tools/#tools
#
# Jacqueline R. M. A. Maasch | November 2020

# Importations.
from datapackage import Package
import pandas as pd

# Read data file.
df = pd.read_csv("merops_peptidase_families.csv")

# Explore.
print(df.info())
display(df.head(2))

# Construct package.
merops_pkg = Package()
merops_pkg.infer("merops_peptidase_families.csv")

# View inferred package.
display(merops_pkg.descriptor)

# Test if valid.
print("\nPackage valid:", merops_pkg.valid)

# Access fields of schema.
print("Data type of schema:",
      type(merops_pkg.descriptor["resources"][0]["schema"]),
      "\n")
print("Data type of fields:",
      type(merops_pkg.descriptor["resources"][0]["schema"]["fields"]),
      "\n")
print("Data type of individual field:",
      type(merops_pkg.descriptor["resources"][0]["schema"]["fields"][0]),
      "\n")
display(merops_pkg.descriptor["resources"][0]["schema"]["fields"])

# Update fields of schema.
fields = merops_pkg.descriptor["resources"][0]["schema"]["fields"]
desc_family = "Human peptidase family (e.g. 'A1')."
desc_subfamily = "Human peptidase subfamily (e.g. 'A1B')."
desc_type = "Type enzyme for peptidase subfamily (e.g. 'pepsin A (Homo sapiens)')."
desc_group = "Peptidase group (e.g. 'Aspartic (A) Peptidase')."
desc_list = [desc_family, desc_subfamily, desc_type, desc_group]

for i in range(0, len(fields)):
    fields[i]["description"] = desc_list[i]

display(merops_pkg.descriptor["resources"][0]["schema"]["fields"])

# Add additional metadata to package.
merops_pkg.descriptor["keywords"] = ["peptide",
                                     "protein",
                                     "peptidase",
                                     "proteinase",
                                     "protease",
                                     "bioinformatics",
                                     "protein informatics",
                                     "MEROPS",
                                     "cleavage",
                                     "proteolysis"]

merops_pkg.descriptor["title"] = "Human peptidase families"
merops_pkg.descriptor["contributors"] = {"title": "JRMA Maasch",
                                         "role": "author"}
merops_pkg.descriptor["licenses"] = [{"name": "CC0-1.0",
                                      "title": "CC0 1.0",
                                      "path": "https://creativecommons.org/publicdomain/zero/1.0/"}]
merops_pkg.descriptor["description"] = "A dataset of human peptidase families as scraped from the MEROPS Peptidase Database in June 2020 (https://www.ebi.ac.uk/merops/index.shtml)."

# Display updated package.
display(merops_pkg.descriptor)

# Save data package.
merops_pkg.commit()
merops_pkg.save("merops_data_pkg.zip")
