# coding=utf-8
import os
import sys 
reload(sys)
sys.setdefaultencoding("utf-8")
print sys.getdefaultencoding()


from flask import abort, jsonify, Flask, request, Response

app = Flask(__name__)

asr = {
    "stateCode": {
        "code": 0,
        "desc": "成功"
    },
    "statusText": "我是一个学生",
    "timestamp": "1500531770453",
    "result": "语音结果识别正确"
}

ocr={
    "RequestId":"048a663b-9da7-47d0-b47e-1ebce9fc88fe",
    "Status":"success",
    "Result":"pic is too big",
    "RemainMoney":9900
}


@app.route("/asr", methods=['GET'])
def get_asr_result():
    return jsonify(asr)

@app.route("/ocr", methods=['GET'])
def get_ocr_result():
    return jsonify(ocr)
    
if __name__ == "__main__":
    app.run(host = "127.0.0.1",port = 8989,debug = True )
