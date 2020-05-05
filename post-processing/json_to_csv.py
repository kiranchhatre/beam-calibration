import codecs, json, collections, csv
from operator import itemgetter
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

json_file = '/home/berkeleylab/Misc_code/AWS_files/tranfer/worker_n_optimizer/results.json'
data = []

with codecs.open(json_file, 'rU', 'utf-8') as data_file:
    for line in data_file:
        data.append(json.loads(line))

with open("results_json_new.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)