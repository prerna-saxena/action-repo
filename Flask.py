from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["webhookDB"]
collection = db["events"]

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        event_type = request.headers.get('X-GitHub-Event')

        # Extract relevant data
        if event_type == "push":
            author = data['pusher']['name']
            branch = data['ref'].split('/')[-1]
            timestamp = datetime.now()
            event = {
                "type": "push",
                "author": author,
                "branch": branch,
                "timestamp": timestamp
            }
        elif event_type == "pull_request":
            author = data['pull_request']['user']['login']
            from_branch = data['pull_request']['head']['ref']
            to_branch = data['pull_request']['base']['ref']
            timestamp = datetime.now()
            event = {
                "type": "pull_request",
                "author": author,
                "from_branch": from_branch,
                "to_branch": to_branch,
                "timestamp": timestamp
            }
        elif event_type == "merge":  # Add logic for merge events if available
            author = data['user']['login']
            from_branch = data['head_branch']
            to_branch = data['base_branch']
            timestamp = datetime.now()
            event = {
                "type": "merge",
                "author": author,
                "from_branch": from_branch,
                "to_branch": to_branch,
                "timestamp": timestamp
            }

        # Store to MongoDB
        collection.insert_one(event)
        return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True)
