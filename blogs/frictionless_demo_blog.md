# Walking through the `frictionless` framework

While the [GoodTables](http://goodtables.io/dashboard) web server is a convenient tool for automated data validation, the [`frictionless`](https://frictionlessdata.io/tooling/python/#purpose) framework allows for validation right within your Python or Bash scripts. We'll demonstrate some key `frictionless` functionality, both in Python and command line syntax. As an illustrative point, we will use a CSV file that contains an invalid element – a remnant of careless file creation.

View the original [Jupyter notebook](https://github.com/jmaasch/reproducible-research/blob/master/frictionless_demo/frictionless_demo.ipynb), [Python script](https://github.com/jmaasch/reproducible-research/blob/master/frictionless_demo/frictionless_demo.py), and [dataset](https://github.com/jmaasch/reproducible-research/blob/master/frictionless_demo/merops_peptidase_families.csv) on GitHub.

**Note:** This demo uses `frictionless` version 3.48.0, `pandas` version 1.0.1, and Python 3.8.3.

## Overview

This simple [Python script](https://github.com/jmaasch/reproducible-research/blob/master/frictionless_demo/frictionless_demo.py) shows the command line syntax and equivalent Python syntax that we will review in this demo.

<img width="523" alt="script" src="https://user-images.githubusercontent.com/50045763/105934032-69c88880-601d-11eb-8707-d9a5d1f39e0f.png">

## Command line syntax

### View data

First, we can import the `frictionless` package. We will also use `pandas` for some light dataframe manipulation. Starting with our command line syntax, we can get a sense of what we are working with by printing out the first several lines of our CSV file. 

If you look closely, you will see that the first column contains no header: the first element of row one is empty, as conveyed by the lonely "," preceeded by... nothing at all. In fact, this column is quite useless: it is an artifact of forgetting to pass the argument `index = False` to the `pandas` function `to_csv()` during file creation. This useless indexing column would ideally be removed entirely. Let's see how this oversight plays out during file validation...

<img width="1030" alt="demo1" src="https://user-images.githubusercontent.com/50045763/105934836-ed36a980-601e-11eb-9fd3-14316b13646e.png">

### Describe data

Next, we can describe our data file.

<img width="1031" alt="demo2" src="https://user-images.githubusercontent.com/50045763/105934840-edcf4000-601e-11eb-9e94-614c2dbf7168.png">

### Validate data

When we finally go to validate our data file, that missing column name that we noted above will come back to haunt us... indeed, this is the cause of our failed validation. To make this CSV file valid, we would need to either 1) remove the offending column, which contains no pertinent data anyways, or 2) give the offending column a proper name.

<img width="1032" alt="demo3" src="https://user-images.githubusercontent.com/50045763/105934841-ee67d680-601e-11eb-9dc3-4b1c06ed00d1.png">

## Python syntax

Below, we walk through the Python syntax that provides equivalent functionality. As you'll see, this syntax is extremely similar to its command line equivalent, just more "pythonic." However, the outputs do look a bit different!

<img width="1030" alt="demo4" src="https://user-images.githubusercontent.com/50045763/105934846-ef990380-601e-11eb-87cf-fd13ef3a743c.png">

Clearly, our data is invalid!

<img width="1030" alt="demo5" src="https://user-images.githubusercontent.com/50045763/105935027-3dae0700-601f-11eb-8ad2-6a295272c054.png">

Note that the `message` and `description` values provide a useful elaboration on the reason our CSV file is deemed invalid.

<img width="1028" alt="demo6" src="https://user-images.githubusercontent.com/50045763/105934849-f0319a00-601e-11eb-9b57-8b562b1132ec.png">

## Bottom line

The `frictionless` framework is a convenient way to wrap your data validation needs directly into your existing Python data analysis pipeline. Choose whichever syntax works for you – Python or command line.
