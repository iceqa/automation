## Installation
### 1. Install pip for Python 3
```
sudo apt update
sudo apt install python-pip
```
### 2. Install pytest
```
pip install -U virtualenv
python -m virtualenv venv
source venv/bin/activate
pip install pytest
```
### 3. Update JWT in the project.
```
3.1. Generate JWT from https://developer.nexmo.com/jwt.
3.2. Add JWT to "JWT" variable in https://github.com/iceqa/automation/blob/84a5650390d6bc1994fcc5d577e982b7abaf66ee/config/config.py#L9 
```
## Run tests
```
clear & pytest
clear & pytest -s -v tests/
```
