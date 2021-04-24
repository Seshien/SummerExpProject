import requests, json
import flask
GH_name = "https://api.github.com/users"
NOT_FOUND = 404
LIMIT_REACHED = 477
ERROR_UNKNOWN = 488
LIMIT_WARNING = """Warning: Limit of API requests for github was exceeded during processing. \n
                You have to wait (or change your ip) before trying again.
                """

def get_repos(user):
    user_info = request_user_info(user)
    validation = validate(user_info)
    if validation:
        return error_value(validation)
    repos = get_all_repositories(user, user_info['public_repos'])

    return flask.make_response(json.dumps(repos))


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
        except KeyError or TypeError as exc:
            return flask.make_response(json.dumps(
                [sum, LIMIT_WARNING]))
    return flask.make_response(json.dumps(sum))

def request_user_info(user):
    info_r = requests.get(f'{GH_name}/{user}')
    json_d = info_r.json()
    return json_d

def validate(json_d):
    if 'message' in json_d:
        if json_d['message'] == 'Not Found':
            return NOT_FOUND
        elif 'limit' in json_d['message']:
            return LIMIT_REACHED
        else:
            return ERROR_UNKNOWN
    return False

def error_value(error):
    if error == NOT_FOUND:
        return flask.make_response("Error: User with that username doesn't exist.")
    elif error == LIMIT_REACHED:
        return flask.make_response(
            """Error: Limit of API requests for github has been exceeded.\n
             You have to wait (or change your ip) before trying again.
            """
        )
    else:
        return flask.make_response(f"Error: I did not expect that error")

def get_all_repositories(user, repos_number):
    result = []
    for page in range(repos_number % 100 + 1):
        repos_d = requests.get(f'{GH_name}/{user}/repos',
                               params={'per_page' : '100', 'page' : str(page + 1)}).json()
        if repos_d is dict:
            result.append(LIMIT_WARNING)
            return result
        result.extend(repos_d)
    return result
