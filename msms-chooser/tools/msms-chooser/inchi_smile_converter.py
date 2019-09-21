import os
import csv
import requests

# this is used to query inchi, smiles using Ming's web api
def inchi2smiles (inchi):
    url = "http://dorresteinappshub.ucsd.edu:5065/inchi/smiles?inchi=%s"%inchi
    response = requests.get(url)
    if response.status_code !=200 :
        #print(response.text)
        print(url)
        print("no results for %s"%inchi)
        return ""
    return response.text

def smiles2inchi (smiles):
    url = "http://dorresteinappshub.ucsd.edu:5065/smiles/inchi?smiles=%s&width=350&height=250cache=2"%smiles
    response = requests.get(url)
    if response.status_code !=200 :
        #print(response.text)
        print("no results for %s"%smiles)
        return ""
    return response.text
