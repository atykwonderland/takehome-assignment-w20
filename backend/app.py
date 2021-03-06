from typing import Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.
    
    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})


@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)

#Part 6
@app.route("/shows", methods=['GET'])
def get_all_shows():
    minEpisodes = request.args.get('minEpisodes')
    data = db.get('shows')
    if minEpisodes == None:
        return create_response({"shows": data})
    new_data = [x for x in data if x['episodes_seen'] >= int(minEpisodes)]
    return create_response({"shows": new_data})

@app.route("/shows/<id>", methods=['DELETE'])
def delete_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    db.deleteById('shows', int(id))
    return create_response(message="Show deleted")

#Part 2
@app.route("/shows/<id>", methods=['GET'])
def get_single_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    return create_response(db.getById('shows', int(id)))

#Part 3
@app.route("/shows", methods=['POST'])
def create_new_show():
    data = request.json
    if hasattr(data, 'name')==False or hasattr(data, 'episodes_seen')==FALSE:
        return create_response(status=422, message="You must input the show name and the number of episodes seen")
    return create_response(db.create('shows', data))

#Part 4
@app.route("/shows/<id>", methods=['PUT'])
def update_show(id):
    data = request.json
    if db.getByID('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    return create_response(db.updateById('shows', int(id), data))


"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
if __name__ == "__main__":
    app.run(port=8080, debug=True)
