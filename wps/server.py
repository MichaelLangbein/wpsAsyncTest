import flask
from flask_cors import CORS, cross_origin
from pywps import Service
from wps.sayHiWps import SayHiWps



app = flask.Flask(__name__)
cors = CORS(app)
processes = [SayHiWps()]
service = Service(processes=processes, cfgfiles=['wps/pywps.cfg'])




@app.route('/wps/', methods=['GET', 'POST'])
@cross_origin(headers=['Content-Type'])
def wps():
    return service



@app.route('/outputs/<path:filename>')
def outputfile(filename):
    targetfile = os.path.join('outputs', filename)
    if os.path.isfile(targetfile):
        file_ext = os.path.splitext(targetfile)[1]
        with open(targetfile, mode='rb') as f:
            file_bytes = f.read()
        mime_type = None
        if 'xml' in file_ext:
            mime_type = 'text/xml'
        return flask.Response(file_bytes, content_type=mime_type)
    else:
        flask.abort(404)


@app.route('/static/<path:filename>')
def staticfile(filename):
    targetfile = os.path.join('static', filename)
    if os.path.isfile(targetfile):
        with open(targetfile, mode='rb') as f:
            file_bytes = f.read()
        mime_type = None
        return flask.Response(file_bytes, content_type=mime_type)
    else:
        flask.abort(404)




if __name__ == '__main__':
    app.run(threaded=False, host='localhost', port=1410)