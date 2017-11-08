import json
from flask import Flask
from . import scrapper, database

app = Flask(__name__)
speakers, talks = [], []

with database.micDB() as db:
  for p in scrapper.pyconPresentations(2016):
    db.insertTalk(p)
    talks = db.getTalks()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/speakers')
def getPresentations():
  return json.dumps(speakers)

@app.route('/presentations')
def getPresentations():
  return json.dumps(talks)
