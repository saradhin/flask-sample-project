from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
     'name':'mystore',
     'items':
         [
            {
            'name':'My Item',
            'price': 15.99
            }
        ]
    }
]

@app.route('/')
def home():
    return ('Hello World')

#POST /store date {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET  /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})



#GET  /store
@app.route('/store')
def get_list_store():
    return jsonify({'stores':stores})

#POST /store/<string:name>/item {name:price}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name):
    for store in stores:
        if store['name'] == name:
            request_data = request.get_json()
            new_items = {
                'name': 'new item',
                'price': 20,
            }
            store['items'].append(new_items)
            return jsonify(new_items)
    return jsonify({'message': 'store not found'})

#GET  /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'items not found'})

app.run(port=5000)
