# -*- coding: utf-8 -*-

import requests
from flask import Flask

requests.packages.urllib3.disable_warnings()

app = Flask(__name__)


import views