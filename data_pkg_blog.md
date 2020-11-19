# Constructing a basic data package in Python

Because I do most of my data management and analysis in Python, I find it convenient to package my data in Python as well. The screenshots below are a walk-through of basic data package construction in Python. In this case, I was programming in a Jupyter notebook and handling data that I had scraped from a protein informatics database.

The dataset that I am working with describes human peptidase families, as scraped from the [MEROPS Peptidase Database](https://www.ebi.ac.uk/merops/index.shtml) in June 2020.
<img width="761" alt="pkg_blog1" src="https://user-images.githubusercontent.com/50045763/99606537-f3355c00-29d7-11eb-8191-5691c893f129.png">

First, I invoked the `infer()` method to autopopulate the majority of the fields in my data package.
<img width="762" alt="pkg_blog2" src="https://user-images.githubusercontent.com/50045763/99606540-f3cdf280-29d7-11eb-93bb-145d90897617.png">

Second, I explored the data structures nested within the `merops_pkg.descriptor` object. This gave me a better sense of how to manually manipulate these data structures.
<img width="764" alt="pkg_blog3" src="https://user-images.githubusercontent.com/50045763/99606541-f4668900-29d7-11eb-85c1-540dc333b82e.png">

<img width="762" alt="pkg_blog4" src="https://user-images.githubusercontent.com/50045763/99606544-f4668900-29d7-11eb-94c5-8e57be303208.png">

<img width="774" alt="pkg_blog5" src="https://user-images.githubusercontent.com/50045763/99606547-f4ff1f80-29d7-11eb-9cb6-03bfad928053.png">

<img width="771" alt="pkg_blog6" src="https://user-images.githubusercontent.com/50045763/99606549-f4ff1f80-29d7-11eb-88df-7e88f171b064.png">
