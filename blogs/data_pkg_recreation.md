# Reproducing a data package

## Import packages

First, we will import the packages we need: `datapackage` for data package construction, `frictionless` for data file validation, and `pandas` for light dataframe manipulation.

## Read data

Next, we will import our data files and explore them. Note that `df_623` and `df_719` do not have the same column headers nor the same shape. This makes analyses that draw comparisons between the two datasets less convenient. Therefore, we also have `df_719_adj`, which has adjusted `df_719` so that it adheres to the same format as `df_623`.

```python
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   sample_name           30 non-null     object 
 1   golay_index_barcode   30 non-null     object 
 2   primer_name           30 non-null     object 
 3   full_primer_sequence  30 non-null     object 
 4   sample_id             30 non-null     object 
 5   DNA_conc              30 non-null     float64
 6   is.neg                30 non-null     bool   
 7   sample_origin         30 non-null     object 
 8   anti_coagulant        18 non-null     object 
 9   subject_id            30 non-null     object 
 10  extraction_batch      30 non-null     int64  
 11  dna_extraction_kit    30 non-null     object 
dtypes: bool(1), float64(1), int64(1), object(9)
```

```python
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   samle_name          95 non-null     object 
 1   sample_description  95 non-null     object 
 2   sample_ID           95 non-null     object 
 3   barcode             95 non-null     object 
 4   is.neg              95 non-null     bool   
 5   DNA_Conc            95 non-null     float64
 6   sample_origin       95 non-null     object 
 7   extraction_batch    68 non-null     float64
 8   dna_extraction_kit  95 non-null     object 
dtypes: bool(1), float64(2), object(6)
```

```python
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   sample_name           95 non-null     object 
 1   golay_index_barcode   95 non-null     object 
 2   primer_name           95 non-null     object 
 3   full_primer_sequence  95 non-null     object 
 4   sample_id             95 non-null     object 
 5   DNA_conc              95 non-null     float64
 6   is.neg                95 non-null     bool   
 7   sample_origin         95 non-null     object 
 8   anti_coagulant        34 non-null     object 
 9   subject_id            95 non-null     object 
 10  extraction_batch      68 non-null     float64
 11  dna_extraction_kit    95 non-null     object 
dtypes: bool(1), float64(2), object(9)
```
