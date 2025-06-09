from flask import Flask  # import the Flask class

app = Flask(__name__)  # create your Flask app instance

@app.route('/')  # define the route (the home page)
def index():
    return '<h1>Welcome to my page!</h1>'  # return some HTML

@app.route('/<string:username>')  # dynamic route with a username
def user(username):
    return f'<h1>Profile for {username}</h1>'  # dynamic HTML response

if __name__ == '__main__':  # this runs the app only if this file is executed directly
    app.run(port=5555, debug=True)  # run Flask on port 5555 with auto-reload on
