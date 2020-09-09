import csv

import pandas as pd

import requests

with open('mlchallengeset.tsv','r',encoding='utf8') as fin:
    cr = csv.reader(fin, delimiter='\t')
    filecontents = [line for line in cr]

data=pd.DataFrame(filecontents)

dataset = data.rename(columns={0: 'category', 1: 'primary_image_url',2: 'all_image_urls', 3: 'attributes',4:'index'})

dataset['category'].value_counts()






