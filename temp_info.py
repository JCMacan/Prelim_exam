from flask import Flask, jsonify, request

app = Flask(__name__)
temp=[
    {
        "Temp_id": "01",
        "Date": "October 4, 2022",
        "Temperature": "38 degrees C"
    },


    {
        "Temp_id": "02",
        "Date": "October 4, 2022",
        "Temperature": "35 degrees C"
    },
     {
        "Temp_id": "03",
        "Date": "October 4, 2022",
        "Temperature": "36 degrees C"
    }

]

@app.route('/temp', methods=['GET'])
def displayTemp():
    return jsonify(temp)

@app.route('/temp', methods=['POST'])
def addTemp():
    temp1 = request.get_json()
    temp.append(temp)
    return {'id': len(temp1)},200

@app.route('/temp/<int:index>', methods=['DELETE'])
def deletetemp(index):
    temp.pop(index)
    return 'Temperature ID was successfully deleted', 200


if __name__ == '__main__':
    app.run()