#!/usr/bin/python3
"""index file for view"""
from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/status'):
    def status():
        """ Returns the status of the request """
        return jsonify({"status": "OK"})
