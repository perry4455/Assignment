from addition import addition
from flask import Flask, request
from flask_restful import Resource, Api
app = Flask("adding two numbers")
api = Api(app)

class Adder(Resource):
    def get(self):
        args = request.args
        print (args) # For debugging
        
        a = int(args['a'])
        b = int(args['b'])
        print("a is",a)
        print("b is",b)
        db_utils = addition(a,b)
        cursor = db_utils.Add()

        return cursor


api.add_resource(Adder, '/add')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000)
    
