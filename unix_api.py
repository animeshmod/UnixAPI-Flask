#!/usr/bin/env python
import os 
from flask import Flask, jsonify, Blueprint
from flask import abort
import subprocess
from flask_restful import Api,Resource
import json

def create_app(config_obj=None):
    app = Flask(__name__)
    return app

app = create_app()

"""The commandlist contains the commands which are allowed to be executed through the API call
"""

commandlist = [
     {
         "command": "DiskSpace",
         "syntax": u'df -h',
         "aid": 1
     },
     {
         "command": "DirectoryList",
         "syntax": u'ls -ltr',
         "aid": 2
     },
     {
         "command": "Processes",
         "syntax": u'ps -ef | grep process',
         "aid": 3
     }
 ]

@app.errorhandler(404)
def not_found(error):
     """ Sending valid error output for invalid entry
     """
     return (jsonify({'error': 'Not found'}), 404)

@app.route('/commands', methods=['GET'])
def get_commands():
     print("Calling")
     """The functions sends the list of commands supported by the API with the syntaz it executes and corresponding
        ID which user can pass.
     """
     return jsonify({'Commands': commandlist})

@app.route('/commands/<int:task_id>', methods=['GET'])
def get_command(task_id):
     """The function executes the unix command based on the id provided in api call.
     """
     task = [command for command in commandlist if command['aid'] == task_id] 
     if len(task) == 0:
         abort(404)

     ## Getting the actual command from dictionary
     syntax = [d["syntax"] for d in task]

     syntax = syntax[0]

     p = subprocess.check_output(syntax, shell=True)  

     return jsonify({'Commands': p})   


if __name__ == '__main__':
    app.run()

