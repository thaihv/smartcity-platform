from mapbox import Datasets
import json
datasets = Datasets(access_token='sk.eyJ1IjoidGhhaWh2IiwiYSI6ImNrdmt0c3djdzA1NnMydW04anQ4YWsyeTAifQ.pgbFTRvK6pBmKdilbLkMZg')
# create_resp = datasets.create(name="Bay Area",
# description = "Bay Area zipcode")
listing_resp = datasets.list()
print(listing_resp.json())



dataset_id = [ds['id'] for ds in listing_resp.json()][2]

print(dataset_id)

data = json.load(open(r'.\geodata\data\ztca_bayarea.json'))

print(data['features'])

for count,feature in enumerate(data['features']):
    resp = datasets.update_feature(dataset_id, count, feature)
