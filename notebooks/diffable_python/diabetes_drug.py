# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# Snomed/NHS Dictionary of Medicines Devices codes for oral diabetes drugs.

from ebmdatalab import bq
import os
import pandas as pd 

# +
sql = '''WITH bnf_codes AS (
  SELECT bnf_code FROM hscic.presentation WHERE 
    bnf_code LIKE '060102%' #BNF diabetes drugs (not including insulin)
 
  )

SELECT "vmp" AS type, id, bnf_code, nm
FROM dmd.vmp
WHERE bnf_code IN (SELECT * FROM bnf_codes)

UNION ALL

SELECT "amp" AS type, id, bnf_code, descr
FROM dmd.amp
WHERE bnf_code IN (SELECT * FROM bnf_codes)

ORDER BY type, bnf_code, id'''

azithromycin_codelist = bq.cached_read(sql, csv_path=os.path.join('..','data','azithromycin_codelist.csv'))
pd.set_option('display.max_rows', None)
azithromycin_codelist
