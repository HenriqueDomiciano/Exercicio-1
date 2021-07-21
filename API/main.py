from flask import Flask,jsonify,request
from flask_restful import Api,Resource,reqparse
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
from models import DB
import os

app= Flask(__name__)
CORS(app)
api = Api(app)
auth = HTTPBasicAuth()

key = {'admin':os.environ['key']}

@auth.verify_password
def verify(username, password):
    if not(username and password):
        return False
    return key.get(username)==username,password

general_arg = reqparse.RequestParser()
general_arg.add_argument('table',type=str,help='The table you want to post your new data',required=True)
date_args = reqparse.RequestParser()
date_args.add_argument('date',type=str,help='The day',required=True)
country_args = reqparse.RequestParser()
country_args.add_argument('ISO',type=str,help = 'The iso with the country code')
country_args.add_argument('name',type =str,help = 'The name of the country')
country_args.add_argument('is_vaccine',type=str,help='Is vaccines or cases?',required=True)

class General(Resource):
    @auth.login_required
    def get(self):
        banco = DB()
        return banco.all_data()
    def post(self):
        args = general_arg.parse_args()
        banco=DB()
        try:
            if args['table']=='vaccines':
                files = request.files['file']
                banco.add_csv_vacinas(files)
                return jsonify({"Sucess":'True'})
            elif args['table']=='type_vaccines':
                files = request.files['file']
                banco.add_csv_type_vaccine(files)
                return jsonify({"Sucess":'True'})
            elif args['table']=='cases':
                files = request.files['file']
                banco.add_csv_cases_covid(files)
                return jsonify({"Sucess":'True'})
            else:
                return jsonify({"Sucess":'False'})
        except:
            return  jsonify({"Sucess":'False'})

class Country(Resource):
    @auth.login_required
    def get(self):
        args = country_args.parse_args()
        banco = DB()
        if args['is_vaccine']=='vaccines':
            if args['ISO']:
                return banco.get_country(args['ISO'],'dados') 
            elif args['name']:
                return banco.get_by_country_name(args['name'],'dados')
        else:
            return banco.get_country(args['ISO'],'cases')
class Date(Resource):
    @auth.login_required
    def get(self):
        args = date_args.parse_args()
        banco = DB()        
        return banco.get_by_date('dados',args['date'])

api.add_resource(General,'/General')
api.add_resource(Country,'/Country')
api.add_resource(Date,'/Date')

if __name__ == '__main__':
    app.run(debug =True)