# app.py
# https://cloud.google.com/community/tutorials/building-flask-api-with-cloud-firestore-and-deploying-to-cloud-run

# Required imports
import os
import json
import sys
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

# Initialize Flask app
app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate('service-account.key')
default_app = initialize_app(cred)
db = firestore.client()

coll_name = os.environ.get('COLLECTION', 'restaurants')
my_collection = db.collection(coll_name)


@app.route('/microservice-ratings/add', methods=['POST'])
def create():
    try:

        payload = json.loads(request.get_data())
        restaurantID = payload['id']
        data = my_collection.document(restaurantID).collection("ratings").document().set(payload['r'])

        print(request.get_data(), file=sys.stdout)
        print(data, file=sys.stdout)

        return restaurantID, 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/microservice-ratings/list', methods=['GET'])
def read():
    try:
        todo_id = request.args.get('id')
        reviews = my_collection.document(todo_id).collection("ratings").stream()
        revs = [ rev.to_dict() for rev in reviews]

        response = jsonify(revs)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/microservice-ratings/update', methods=['POST', 'PUT'])
def update():
    """
        update() : Update document in Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post today'}
    """
    try:
        id = request.json['id']
        my_collection.document(id).update(request.json)
        response = jsonify({"success": True})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/microservice-ratings/delete', methods=['GET', 'DELETE'])
def delete():
    """
        delete() : Delete a document from Firestore collection.
    """
    try:
        # Check for ID in URL query
        todo_id = request.args.get('id')
        my_collection.document(todo_id).delete()
        response = jsonify({"success": True})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200
    except Exception as e:
        return f"An Error Occured: {e}"

port = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(threaded=True, debug=True, host='0.0.0.0', port=port)