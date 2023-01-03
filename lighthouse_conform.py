import json
from datetime import date

import bq_ingest as bq

filename = 'g1.globo.com-20221120T212933.json'
with open(filename, 'r') as f:
    data = json.load(f)

categories = []
selectors = []
descriptions = []
audits = data.get('audits',[])
for audit in audits:
    if 'details' in data['audits'][audit]:
        if 'items' in data['audits'][audit]['details']:
            for item in data['audits'][audit]['details']['items']:
                categories.append(audit)
                descriptions.append(data['audits'][audit]['title'])
                if len(item)>0:
                    selectors.append(item['node']['selector'])
url = data['requestedUrl']
day = date.today()
score = data['categories']['accessibility']['score']

payload = {
    "Url": url,
    "Score": score ,
    "Category": categories,
    "Description": descriptions,
    "Selector": selectors,
    "Day": day
}

bq.insert(payload)
print('Done')