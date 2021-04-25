import flask
import sys
from GithubHandler import get_repos, get_stars

app = flask.Flask(__name__)

def main(argv):
    args = simpleParse(argv)
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.run(**args)

#Very simple and lazy parse returning dict, searching for an argument and then treating next argv as its value
def simpleParse(argv):
    result = {}
    handled_arg = ["--port", "--host", "--debug"]
    for it in handled_arg:
        try:
            if it in argv:
                index = argv.index(it)
                if argv[index+1] not in handled_arg:
                    result[it[2:]] = argv[index+1]
        except IndexError as exc:
            pass
    return result


#This is my first web application written in Python, so to comply with tradition
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
    main(sys.argv[1:])
