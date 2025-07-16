import requests
from elasticsearch import Elasticsearch

# This function fetches METAR data for a given station and period from the Aviation Weather API.
def fetch_metar(station, period):
    url = 'https://aviationweather.gov/api/data/metar?ids=' + station + '&format=json&taf=false&hours=' + str(period)
    response = requests.get(url)
    response.raise_for_status()  # Raises an error for bad responses
    return response.json()

# This function indexes the fetched METAR data into an Elasticsearch index.
def index_metar(metar_json, es_index, es_host, es_port, api_key='Wjl2RUU1Z0I5WnZHSDBxeEFHSy06THF6VC01MnJXbWdmUklFNmNFTFZDQQ=='):
    es = Elasticsearch([{'host': es_host, 'port': es_port, 'scheme': 'https'}], api_key=api_key)
    for record in metar_json:
        es.index(index=es_index, body=record)

# Main function to fetch and index METAR data
if __name__ == "__main__":
    station = 'SBGR'  # Change to desired airport code
    period = 1
    es_index = 'skybuoy-metar-test-00001'
    es_host = 'skybuoy-a7bc33.es.us-east-1.aws.elastic.cloud'  # Change to your Elasticsearch host
    es_port = 443  # Change to your Elasticsearch port
    metar_json = fetch_metar(station, period)
    index_metar(metar_json, es_index, es_host, es_port)
    print(metar_json)