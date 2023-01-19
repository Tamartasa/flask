from flask import Flask, request

app = Flask("sample_web_app")


@app.route("/")
def hello_all():
    return "Hello!!!!!!!!"

@app.route("/users/<string:username>")
def get_user_data(username):
    return username

@app.route("/tamar")
def hi_tamar():
    return f"Hi {request.args.get('name')}!!!"

@app.route("/beauty")
def hi_beauty():
    return "<p style='color: red'>Hi Tamar!</p>"


if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=5555)
    app.run(debug=True, port=5001)

