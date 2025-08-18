# Setup/installation
There are multiple ways of setting up the environment, most notably:
1. Python virtual environment
2. Installing necessary APT packages (Debian based distro's)

## Virtual environment
First prepare the environment:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Now you can run the app:
```
python gui.py
```

## Installing APT packages (Debian based distro's)
First install necessary APT packages:
```
sudo apt install python3-openpyxl python3-pyqt6 python3-requests
```

Now you can run the app:
```
python3 gui.py
```