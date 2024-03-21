import flask
from markupsafe import escape

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Mapping here get->/, maps to the home() fcn.
@app.route("/<name>", methods=['GET'])
def home(name):
	return f"<h1>The Title of the Page</h1><p>This is some text on the Web Page.</p><p>{escape(name)}</p>"


app.run(host='0.0.0.0')

