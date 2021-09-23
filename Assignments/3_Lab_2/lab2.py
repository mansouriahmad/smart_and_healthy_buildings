
import pandas as pd
import requests
import io
from pprint import pprint
from urllib.request import urlopen

df = pd.read_csv('GitHub_Alias.csv')

result_df = pd.DataFrame(df['GitHub Username'])

base_url = "https://raw.githubusercontent.com"
for index, row in df.iterrows():
    if (row['Lab Directory Name'] != '-'):
        url = base_url + "/{}/{}/{}/{}/{}".format(
            row['GitHub Username'],
            row['Repository Name'],
            row['Branch Name'],
            row['Lab Directory Name'],
            row['Readme file name']
        )
    else:

        url =   base_url + "/{}/{}/{}/{}".format(
            row['GitHub Username'],
            row['Repository Name'],
            row['Branch Name'],
            row['Readme file name']
        )
    # url = 'https://raw.githubusercontent.com/mansouriahmad/smart_and_healthy_buildings/master/Assignments/2_Lab_1/readme.md'
    print(url)
    try:
        req = urlopen(url)
        mybytes = req.read()
        mystr = mybytes.decode("utf8")
        req.close()

        print(mystr)
        # print(req.read())
    except Exception as er:
        print(er)
