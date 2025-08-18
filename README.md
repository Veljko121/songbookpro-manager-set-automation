# Setup/installation

## Virtual environment
```
# prepare the environment
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# run the app
python gui.py
```

## Debian Python packages
```
# prepare the environment
sudo apt install python3-openpyxl python3-pyqt6 python3-requests

# run the app
python3 gui.py
```