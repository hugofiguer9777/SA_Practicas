from flask import Flask, request, jsonify, Response
#from bson import json_util
#from bson.objectid import ObjectId
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)