from flask import Flask, request, jsonify
from service import AttractionService
from models import Schema

import json

app = Flask(__name__)

@app.after_request
def add_headers(response):
   response.headers['Access-Control-Allow-Origin'] = "*"
   response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
   response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
   return response

@app.route("/")
def hello():
   return "Hello World!"

@app.route("/<name>")
def hello_name(name):
   return "Hello " + name

@app.route("/attraction", methods=["GET"])
def list_todo():
   return jsonify(AttractionService().list())

@app.route("/attraction", methods=["POST"])
def create_todo():
   return jsonify(AttractionService().create(request.get_json()))

@app.route("/attraction/<item_id>", methods=["PUT"])
def update_item(item_id):
   return jsonify(AttractionService().update(item_id, request.get_json()))

@app.route("/attraction/<item_id>", methods=["GET"])
def get_item(item_id):
   return jsonify(AttractionService().get_by_id(item_id))

@app.route("/attraction/<item_id>", methods=["DELETE"])
def delete_item(item_id):
   return jsonify(AttractionService().delete(item_id))

@app.route("/visit/<item_id>", methods=["POST"])
def visit_attraction(item_id):
   return jsonify(AttractionService().visit(item_id))

@app.route("/attraction/search/<state>", methods=["POST"])
def state_search(state):
   return jsonify(AttractionService().state_search(state))



if __name__ == "__main__":
   Schema()
   app.run(debug=True, host='127.0.0.1', port=5000)
