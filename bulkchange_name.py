import json
import os
import glob

def name_changer(filename):
    name, ext = os.path.splitext(filename)
    os.rename(filename, name + '_v2' + ext)   

for file in glob.glob('*.json'):
    name_changer(file)
