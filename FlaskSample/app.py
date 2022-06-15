# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 16:53:18 2022

@author: Boopa
"""

from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def helloIndex():
    return 'Hello World from Python Flask!'

app.run()