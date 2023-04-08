import flask
from peewee import *

db = SqliteDatabase('db.db')

class Content(Model):
    content = TextField()

    class Meta:
        database = db

db.connect()
db.create_tables([Content])

app = flask.Flask(__name__)

@app.route("/get")
def get():
    return "<html><head><meta http-equiv='refresh' content='10'></head><body><ul>" + "".join(["<li>" + content.content + "</li>" for content in Content.select()]) + "</ul></body></html>"

@app.route("/add/<new>")
def add(new):
    Content.create(content=new)
    return ""
@app.route('/')
def home():
   return flask.render_template('index.html')
app.run()