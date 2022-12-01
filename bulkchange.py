import json
import os
import glob

def file_changer(filename):
    # Read Existing JSON File
    with open(filename, 'r+') as f:
        data = json.load(f)
  
    # Append new object to list data
    data.update({'query':  "query test($channelIDs: String!, $type: String!) {  getHomeChannelV2(channelIDs: $channelIDs, page: $type) {    channels {      id      name      layout      header {        id        name      }      grids {        url        applink        imageUrl        attribution      }      rankIdentifier    }  }}",})
    data.update({'queryName': filename})
    # Create new JSON file
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
  
for file in glob.glob('*.json'):
    file_changer(file)
