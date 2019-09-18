
from flask import jsonify, request
from synapsepy import Client, User
import pymongo
import json
# from config import Config
from flask_restful import Resource, Api
from flask import Flask

# from config import Config
app = Flask(__name__)
app.url_map.strict_slashes = False
api = Api(app)
# app.config.from_object('Config')

# app.config.from_object(Config)
from synapsepy import Client, User
#import pymongo
from pymongo import MongoClient

# client_id=Config.CLIENT_ID

#from app.models import UserInfo, Mercury


class Users(Resource):
	def get(self,user_id):
		#fething new user from the synapsefi
		response = client.get_user(user_id)

		#formatting respone 
		res_dict=response.__dict__

		#new user data posting using synapsefi
		user=res_dict['body']

		return user,201


	def patch(self,user_id):
		#user submitted request
		req_body = request.get_json()
		#get user
		user = client.get_user(user_id)

		#response body
		body = req_body

		response = user.update_info(body)

		return response,200

	def post(self,user_id=None):
		body = request.get_json()
		#check for virtual doc SSN DL
		#check for physical doc gov id

		# mongo connection 
		mongo_client = MongoClient('localhost', 27017)
		
		#Getting?creating  a Database for users
		db = mongo_client['users']
		users = db['users']
		#creating user
		response = client.create_user(body,"127.0.0.1")

		#formatting respone 
		res_dict=response.__dict__

		#new user data posting using synapsefi
		new_user=res_dict['body']

		db_entry = {	'user_id': new_user['_id'],
						'docuemnts_id' : new_user['documents'][0]['id'],
						'phone_numbers': new_user['phone_numbers'],
						'logins': new_user['logins'],
						'legal_names': new_user['legal_names'],
						'refresh_token': new_user['refresh_token'],
						'user_ip' : '127.0.0.1',
						'validated' : False,
						'accounts':[]
						 # 'user_ip': request.json['docuemnts'][0]['ip']
						}
		#store this to db response['id']
		users.insert_one(db_entry)
		 
		#getting the user 
		user = client.get_user(new_user['_id'])
		
		# #2FA AUthorization ( 3 stpes using fingerprints)
		#Step 1
		client.update_headers(fingerprint='123456')
		user.oauth()
		#Step 2
		user.select_2fa_device('test@synapsepay.com')
		#step 3
		user.confirm_2fa_pin('123456')
		
		return "success",200

class Account(Resource):
	def post(self,user_id):
		#following is expected in the req body
		# {
		# 	"nickname" : "whatever nickname",
		# 	"type": "SUBACCOUNT-US"
		# }
		#request body
		req_body = request.get_json()

		# mongo connection 
		mongo_client = MongoClient('localhost', 27017)
		
		#Getting/creating  a Database for users
		db = mongo_client['users']
		db_users = db['users']
		user_db = db_users.find_one({'user_id':user_id})
		#fething the user_id from the res
		#getting the user form user id using synapsefi api
		user = client.get_user(user_id)
		#creating account
		body = {
			  "type": req_body['type'],
			  "info": {
			    "nickname": req_body['nickname'],
			    "document_id": user_db['docuemnts_id']
			  }
			}

		response = user.create_node(body, idempotency_key=request.headers.get('idempotency_key'))
		#formatting respone
		for account in response.list_of_nodes:
			acc = account.body
			#new account data posting using synapsefi
			new_acc={acc['info']['nickname']:acc['_id']}

			#inserting to user accounts
			db_users.update_one({
				'user_id':user_id},
				{'$push':{'accounts':new_acc}})
			 
		new_account = response.list_of_nodes[0].body
		return  new_account,201
		
	def get(self,user_id):
		req_body = request.get_json()
		#fething new user from the synapsefi
		user = client.get_user(user_id)

		# mongo connection 
		mongo_client = MongoClient('localhost', 27017)
		
		#Getting/creating  a Database for users
		db = mongo_client['users']
		db_users = db['users']
		user_db = db_users.find_one({'user_id':user_id})
		subaccount_node_id = ""
		for account in user_db['accounts']:
			if account[req_body['nickname']]:
				subaccount_node_id = account[req_body['nickname']]
				break
		print(subaccount_node_id)
		node = user.get_node(subaccount_node_id, full_dehydrate=True, force_refresh=True)
		respose = node.body
		return respose,201

class Transaction(Resource):
	def post(self,user_id):
		req_body = request.get_json()

		user = client.get_user(user_id)
		# mongo connection 
		mongo_client = MongoClient('localhost', 27017)
		
		#Getting/creating  a Database for users
		db = mongo_client['users']
		db_users = db['users']
		user_db = db_users.find_one({'user_id':user_id})


		transfer_to = ""
		transfer_from = ""
		print(req_body)
		for acc1 in user_db['accounts']:
			if acc1.get(req_body['to_account']) :
				transfer_to = acc1.get(req_body['to_account'])
				break
		for acc2 in user_db['accounts']:
			if acc1.get(req_body['to_account']):
				transfer_from = acc1.get(req_body['to_account'])
				break

		node_id = transfer_from
		body = {
  				"to": {
					    "type": "SUBDEPOSIT-US",
					    "id": transfer_to
					  },
					  "amount": {
					    "amount": float(req_body['amount']),
					    "currency": "USD"
					  },
					  "extra": {
					    "ip": "127.0.0.1",
					    "note": "Notes"
				  }
				}
		user.create_trans(node_id, body)

		return 200


api.add_resource(Users ,'/users/<string:user_id>')
api.add_resource(Account,'/account/<string:user_id>')
api.add_resource(Transaction,'/transaction/<string:user_id>')


api.add_resource(User, '/user/<string:user_id>')

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=5000,debug=True)