from flask import Flask, jsonify

app = Flask(__name__)

# json_data = [
# {"name":"Tacey","age":23,"sex":"male","interst":("Programing","Reading")} ,
# {"name":"Amber","age":23,"sex":"female","interst":("Food","Dog")}
# ]

@app.route('/jsontest', methods=['GET'])
def get_json():
    # return jsonify({'json': json_data})
    return jsonify({"status": 2040313, "message": "Bad request: %s need datetime "})
if __name__ == '__main__':
    app.run()
