#coding: utf-8

from flask import Flask, request
from flask_restful import Resource, Api
from operat_json import operate

app = Flask(__name__)
api = Api(app)

class ServiceApi(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        print request.headers
        get_json = request.form.to_dict()
        operate(get_json)
        return 'success'

api.add_resource(ServiceApi, '/')

if __name__ == '__main__':
    app.run(debug=True)




