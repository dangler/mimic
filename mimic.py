__author__ = 'jeremiahd'

import json
import sys
from pprint import pprint

#flask
from flask import Flask
from flask import request
from flask import make_response

#json-schema
from jsonschema import validate

app = Flask(__name__)
responses = {}

def respond():

    # get body and response
    body = json.dumps(responses[request.path + ":" + request.method]['body'])
    status = responses[request.path + ":" + request.method]['status']

    # make a reponse
    response = make_response(body, status)

    # load headers
    for key, value in responses[request.path + ":" + request.method]['headers'].items():
        response.headers[key] = value

    return response


if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        contracts = json.load(f)

    with open("contract-schema.json") as f:
        schema = json.load(f)

    # validate contract list
    validate(contracts, schema)

    for contract in contracts:
        print("creating contract " + contract['request']['path'] + ":" + contract['request']['method'])
        app.add_url_rule(contract['request']['path'], contract['request']['path'], respond)
        responses[contract['request']['path'] + ":" + contract['request']['method']] = contract['response']

    app.run()