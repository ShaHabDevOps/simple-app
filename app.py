#!/usr/bin/env python3
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from shahabuddin for the rollback  Pipelin!"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
))))
