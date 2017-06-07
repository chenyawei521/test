import json
import msgpack
import ConfigParser
from flask import Flask, request
from flask_cors import CORS
from SXPrograms.gout.gout import goutVar

app = Flask(__name__)
CORS(app)

config_path = "../config.conf"


def read_config():
    config = ConfigParser.ConfigParser()
    with open(config_path, "r") as cfg_file:
        config.readfp(cfg_file)
        bson_path = config.get("local", "bson_path")
        knowledge_path = config.get("local", "knowledge_path")
    return bson_path, knowledge_path


def read_txt():
    config = read_config()
    knowledge_path = config[1]
    f = open(knowledge_path, "r")
    lines = f.readlines()
    if not lines:
        return json.dumps({"status": 2090101, "message": "read failed"})
    line_data = []
    rs2freq = {}
    for i in range(len(lines)):
        line_data.append(lines[i].split())
        rs2freq[line_data[i][0]] = line_data[i][1:]
    return rs2freq


def read_bson():
    config = read_config()
    bson_path = config[0]
    b = open(bson_path, "r")
    bson_data = b.read()
    if not bson_data:
        return json.dumps({"status": 2090101, "message": "read bson failed"})
    vs = msgpack.unpackb(bson_data)
    return vs

@app.route("/ping/", methods=["GET"])
def ping():
    return json.dumps("hello")


@app.route("/gout/", methods=["POST"])
def gout():
    data = request.data
    data = json.loads(data)
    if "sample_no" not in data:
        return json.dumps({"status": 2090101, "message": "sample_no not exit"})
    sample_no = data["sample_no"]
    if "knowledge_info" not in data:
        return json.dumps({"status": 2090101, "message": "knowledge_info not exit"})
    knowledge_info = data["knowledge_info"]
    if "data_source" not in data:
        return json.dumps({"status": 2090101, "message": "data_source not exit"})
    data_source = data["data_source"]

    config = read_config()
    bson_path = config[0]
    # knowledge_path = config[1]
    # f = open(knowledge_path, "r")
    # lines = f.readlines()
    # if not lines:
    #     return json.dumps({"status": 2090101, "message": "read failed"})
    # line_data = []
    # rs2freq = {}
    # for i in range(len(lines)):
    #     line_data.append(lines[i].split())
    #     rs2freq[line_data[i][0]] = line_data[i][1:]
    # print rs2freq
    rs2freq = read_txt()
    # if data_source == "sanger":
    #     bson_path =os.path.join(bson_dir, sample_no)
    # elif data_source =="ngx":
    #     bson_path = os.path.join(bson_dir, sample_no)
    # b = open(bson_path, "r")
    # b = open("C:\Users\chen\Desktop\\6211.bson", "r")


    # b = open(bson_path, "r")
    # bson_data = b.read()
    # if not bson_data:
    #     return json.dumps({"status": 2090101, "message": "read bson failed"})
    # vs = msgpack.unpackb(bson_data)
    vs = read_bson()
    med = goutVar(knowledge_info, vs, rs2freq)
    med_lev = med[0]
    med_out = med[1]
    if not med_lev:
        return json.dumps({"status": 2090101, "message": "get scores failed"})
    if not med_out:
        return json.dumps({"status": 2090101, "message": "get vars failed"})
    return json.dumps({"status": 2090101, "data": {"scores": med_lev, "vars": med_out}, "message": "success"})


# @app.route('/service/<sample_no>/', methods=["POST"])
@app.route('/service/', methods=["POST"])
def hello():
    print "hello"
    data = request.data
    data = json.loads(data)
    print data["test"]
    return json.dumps(data)


@app.route('/service/<sample_no>/', methods=["POST"])
def he(sample_no):
    print sample_no
    data = request.data
    data = json.loads(data)
    print data["test"]
    return json.dumps(data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1234)

