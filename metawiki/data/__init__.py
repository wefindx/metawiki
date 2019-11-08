import os
import json
import urllib.request
from distutils.sysconfig import get_python_lib

lov_path = os.path.join(get_python_lib(), 'metawiki/data/LOV.json')

def get(url):
    request = urllib.request.Request(
        url,
        headers={'content-type': 'application/json'}
    )
    data = (urllib.request.urlopen(request)).read().decode('utf-8')
    result = json.loads(data)
    return result

def update_lov():
    vocabs = get('https://lov.linkeddata.es/dataset/lov/api/v2/vocabulary/list')
    with open(lov_path, 'w') as f:
        f.write(json.dumps(vocabs))

def get_lov():
    return json.load(open(lov_path, 'r'))
