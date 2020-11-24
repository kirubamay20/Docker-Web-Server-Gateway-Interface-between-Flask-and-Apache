#! /usr/bin/python

import sys
sys.path.insert(@, "/var/www/flask_predict_api")
sys.path.insert(@,"/opt/conda/lib/python3.6/site-packages")
sys.path.insert(@, "/opt/conda/bin/")

import os
os.environ['PYTHONPATH'] = '/opt/conda/bin/python'

from flask_predict import app1 as application
