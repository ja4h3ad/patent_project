from logging.config import dictConfig
# from app.services import Services, Patent
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin

# from app.services import Services

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

# app = Flask(__name__, template_folder='app/')
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/parse": {"origins": "http://localhost:port"}})

#services = Services()


@app.route('/')
def doc() -> str:
    app.logger.info("doc - Got request")
    with open("app/ui.html", "r") as f:
        return f.read()

@app.route("/checkifstudyexists", methods=["POST"])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def checkifstudy():
    data = request.get_json()   #gets deserialized into a python dictionary
    app.logger.info(f"/checkifstudy - Got request: {data}")
    study_id = services.checkifstudy(data.get('studyname'))
    app.logger.info(f"/checkifstudy - Output: {study_id}")
    return jsonify({"study_id":study_id})

@app.route("/file", methods=["POST"])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def file():
    data = request.get_json()
    app.logger.info(f"/file - Got request: {data}")
    forms = services.get_file(data.get("filename"))  #filename is a dictionary key
    app.logger.info(f"/get_study - Output: {forms}")
    return jsonify({"transcript": forms})

@app.route("/dialog", methods=["POST"])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def dialog():
    data = request.get_json()
    app.logger.info(f"/dialog - Got request: {data}")
    forms = services.get_dialog(data.get('output_filename'))
    app.logger.info(f"/dialog - Output: {forms}")
    parsed = [{"line_number":line[0], "Speaker": line[1], "Comment": line[2]} for line in forms]
    return jsonify(parsed)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
