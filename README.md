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
### 3. Update JWT in the project
```
pip install pytest-dotenv
add .env file to root of your project
add a variable with name "JWT"
go to https://developer.nexmo.com/jwt and generate JWT token
open _env file and add generated token to "JWT" variable
```
## Run tests
```
clear & pytest
clear & pytest -s -v tests/
```
