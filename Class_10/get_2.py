import flask
from flask import request, jsonify, abort, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True
my_dataset = [{'id':0,'name':'The Title' }, {'id':1,'name':' Title2'}]

@app.route("/test1", methods=['GET'])
def test1():
    mydata = [1, 2, 3]
    return mydata


@app.route('/api/v1/resources/movies', methods=['GET'])
def api_all():
    # abort(401)
    return jsonify(my_dataset)


@app.route("/api/v1/resources/movies/<int:m_id>", methods=['GET'])
def api_movie(m_id):
    return list(filter(lambda i: i["id"] == m_id, my_dataset))

@app.route('/api/v1/resources/movies', methods=['POST'])
def form_example():
    # handle the POST request
    name = request.form.get("name")
    mid = request.form.get("id")
    my_dataset.append({'id':int(mid), 'name':name})
    print(my_dataset)
    return "Success"

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


app.run()

# 80 = HTTP
# 443 = HTTPS (SSL)