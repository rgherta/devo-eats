# app.py
# https://cloud.google.com/community/tutorials/building-flask-api-with-cloud-firestore-and-deploying-to-cloud-run

# Required imports
import os
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

@app.route('/add', methods=['POST'])
def create():
    """
        create() : Add document to Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    try:
        id = request.json['id']
        my_collection.document(id).set(request.json)
        response = jsonify({"success": True})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/list', methods=['GET'])
def read():
    """
        read() : Fetches documents from Firestore collection as JSON.
        todo : Return document that matches query ID.
        all_todos : Return all documents.
    """
    try:
        # Check if ID was passed to URL query
        todo_id = request.args.get('id')
        if todo_id:
            todo = my_collection.document(todo_id).get()
            doc = todo.to_dict()
            doc["id"] = todo_id
            response = jsonify(doc)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response, 200
        else:

            #all_todos = [doc.to_dict() for doc in my_collection.stream()]
            docs = [ {doc.id : doc} for doc in my_collection.stream()]
            results = []
            for doc in docs:
              key = (list(doc.keys())[0])
              doct = doc[key].to_dict()
              doct["id"] = key
              results.append(doct)

            response = jsonify(results)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response, 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/update', methods=['POST', 'PUT'])
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

@app.route('/delete', methods=['GET', 'DELETE'])
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

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, debug=True, host='0.0.0.0', port=port)