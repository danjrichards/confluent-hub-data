# Confluent Hub Data Extractor
Confluent Hub provides a searchable interface for all Kafka Connectors.
This script extracts the download URLs for each by parsing the JSON used to populate the home page: https://www.confluent.io/hub/


## Set up
```bash
python3 -m venv ./venv
source ./venv/bin/activate
python3 -m pip install -r requirements.txt
```

## run the code
```bash
python3 hub-data.py
```
