# Setup/installation

## Virtual environment
First prepare the environment:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Now you can run the app using a script:
```
./run.sh
```
Or by running the source Python script manually
```
python src/set_creator.py
```
## ‼️Important limitations‼️
Only configuration with Google Sheets and Local database works at the moment.

## Usage

### Google Sheets configuration
For Google Sheets integration, a service account is needed. Spreadsheets with your sets need to be shared with that service account. More information about Google service accounts and how to set them up are availabe [here](https://docs.cloud.google.com/iam/docs/service-account-overview).

Credentials for a service account need to be downloaded in a JSON format. When downloaded, the credentials need to be found in the app. When loaded, all available spreadsheets will be listed in a combo-box. Also all sheets related to a specific spreadsheets will also be listed.

Just select an appropriate spreadsheet and a sheet. Also configure in which colums are song names and keys.

### Local database integration
A local SQLite database with song data needs to be located through the app.

### Additional configurations
You can write a set name in the app. A default one is provided for based on spreadsheets configuration.