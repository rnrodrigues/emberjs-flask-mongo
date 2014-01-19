from flask import Flask, Response
from pymongo import MongoClient
import json
import os
from datetime import datetime
from bson import ObjectId

class MongoDocumentEncoder(json.JSONEncoder):
  def default(self, o):
    if isinstance(o, datetime):
      return o.isoformat()
    elif isinstance(o, ObjectId):
      return str(o)
    return json.JSONEncoder(self, o)

def jsonify(*args, **kwargs):
  return Response(json.dumps(dict(*args, **kwargs), cls=MongoDocumentEncoder, separators=(",",":"), ensure_ascii=False), mimetype="application/json; charset=utf-8")

application = app = Flask(__name__, static_url_path="")

# Replace MONGOLAB_URI with your full mongolab uri
client = MongoClient(os.getenv("MONGOLAB_URI"))

db = client["db-lapso"]


### Routes ###

@app.route('/')
def index():
  return app.send_static_file("index.html")

@app.route("/users")
def get_users():
  users = list(db.users.find())
  return jsonify({"users": users})

@app.route("/countries")
def get_countries():
  countries = list(db.countries.find())
  return jsonify({"countries": countries})

if __name__=="__main__":
  app.run(debug=True)
