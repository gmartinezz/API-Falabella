import urllib.request
from hashlib import sha256
from hmac import HMAC

def generate_signature(api_key, parameters):
    concatenated = urllib.parse.urlencode(sorted(parameters.items()))
    return HMAC(api_key.encode(), concatenated.encode(), sha256).hexdigest()


