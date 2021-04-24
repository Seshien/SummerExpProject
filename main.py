import flask
from GithubHandler import get_repos, get_stars

app = flask.Flask(__name__)

def main():
    app.run()

@app.route('/')
def hello_world():
    return flask.make_response('Hello, World!')

@app.route('/repositories/<user>')
def handle_repos(user):
    return get_repos(user)

@app.route('/stars/<user>')
def handle_stars(user):
    return get_stars(user)


if __name__ == "__main__":
    main()
