import requests
from connector_dataclasses import jsonToDataclasses

ROOT_URL = 'https://www.confluent.io/hub/'
INDEX = 'page-data/index/page-data.json'


def fetch(url):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache'
    }
    session = requests.session()

    response = session.get(url=url, headers=headers)
    if response.status_code != 200:
        err = f"Error calling {url}: {response.status_code} \n{response.content}"
        print(err)
        return {}
    return response.json()


def getConnectors():
    index = fetch(f"{ROOT_URL}{INDEX}")
    id = index['staticQueryHashes'][0]
    
    raw = fetch(f"{ROOT_URL}page-data/sq/d/{id}.json")
    return raw['data']['allHubPlugin']['nodes']


def main():
    connectors_json = getConnectors()
    connectors_dataclass = jsonToDataclasses(connectors_json)
    
    premium = [conn.license_type for conn in connectors_dataclass if conn.license_type == 'premium']
    print(f"{len(connectors_json)} connectors found, of which {len(premium)} are premium")
    

if __name__ == '__main__':
    main()
