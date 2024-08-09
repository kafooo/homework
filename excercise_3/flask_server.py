from flask import Flask, jsonify, request
import json

app = Flask(__name__)

with open('./data.json', 'r') as f:
        data = json.load(f)

def getSubtags(tag):
    '''Recursively retrieves all subtags of a tag'''
    subtags = [tag]
    for child in data['tags'][tag]['children']:
        subtags.extend(getSubtags(child))
    return subtags

@app.route('/taggedContent', methods=['GET'])
def get_tagged_docs():
    '''Retrieves documents belonging to given tag and it's subtags'''
    tag = request.args.get('tag')
    if not tag:
        return jsonify({'error': 'Tag parameter is required'}), 400
    usedTags = getSubtags(tag)
    documents = []
    for subtag in usedTags:
        documents.extend(data['documents'].get(subtag, []))
    return list(set(documents))