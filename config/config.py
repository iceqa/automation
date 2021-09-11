"""config with access data"""

# URLs
from os import getenv

API_URL = "https://api.nexmo.com"


# JSON Web Token to work with APIs.
JWT = getenv('JWT')
