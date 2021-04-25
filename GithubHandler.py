import requests
import flask
GH_name = "https://api.github.com/users"
NOT_FOUND = 404
LIMIT_REACHED = 477
ERROR_UNKNOWN = 488
LIMIT_WARNING = ("Warning: Limit of API requests for github was exceeded during processing."
                " You have to wait (or change your ip) before trying again.")
USER_ERROR = "User with that username doesn't exist."
LIMIT_ERROR = ("Limit of API requests for github has been exceeded."
                " You have to wait (or change your ip) before trying again.")
UNKNOWN_ERROR = "I did not expect that error"




#Function, which returns a Flask Response. It may have a json list of repositories, but if processing failed,
# it will have a error message instead.
def get_repos(user):
    user_info = request_user_info(user)
    validation = validate(user_info)
    if validation:
        return error_value(validation)
    repos = get_all_repositories(user, user_info['public_repos'])
    return flask.make_response(flask.jsonify(repos))

#Function, which returns a Flask Response. It may have a json with number of stars, but if processing failed,
# it will have a error message instead.
def get_stars(user):
    sum = 0
    user_info = request_user_info(user)
    validation = validate(user_info)
    if validation:
        return error_value(validation)
    repos = get_all_repositories(user, user_info['public_repos'])
    for rep in repos:
        try:
            number = rep['stargazers_count']
            sum += number
        except (KeyError, TypeError) as exc:
            return flask.make_response(flask.jsonify(
                {'stargazers': sum, 'warning': LIMIT_WARNING}))
    return flask.make_response(flask.jsonify({'stargazers': sum}))

#Function, which returns json with data about user from github API.
def request_user_info(user):
    info_r = requests.get(f'{GH_name}/{user}')
    json_d = info_r.json()
    return json_d

#Function, which checks if using github API was succesful. If it was, function returns False, else it returns a error code.
def validate(json_d):
    if 'message' in json_d:
        if json_d['message'] == 'Not Found':
            return NOT_FOUND
        elif 'limit' in json_d['message']:
            return LIMIT_REACHED
        else:
            return ERROR_UNKNOWN
    return False

#Function, which returns Flask Response with error message.
def error_value(error):
    if error == NOT_FOUND:
        return flask.make_response({'Error': USER_ERROR})
    elif error == LIMIT_REACHED:
        return flask.make_response(
            {"Error": LIMIT_ERROR})
    else:
        return flask.make_response({"Error": UNKNOWN_ERROR})

#Functions which go through pages of repositories from github API and returns a complete list of them.
def get_all_repositories(user, repos_number):
    result = []
    pages = (repos_number // 100) + 1
    for page in range(pages):
        repos_d = requests.get(f'{GH_name}/{user}/repos',
                               params={'per_page' : '100', 'page' : str(page + 1)}).json()
        if repos_d is dict:
            result.append(LIMIT_WARNING)
            return result
        result.extend(repos_d)
    return result
