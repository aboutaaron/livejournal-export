# copy values of these cookies for LJ from your browser after logging in
import os
from dotenv import load_dotenv

load_dotenv()

cookies = {
    'ljloggedin': os.getenv('LJLOGGEDIN'),
    'ljmastersession': os.getenv('LJMASTERSESSION'),
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) \
        Gecko/20100101 Firefox/67.0'
}
