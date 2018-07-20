from flask import Flask, render_template, request
import pickle
import json
import random

app = Flask(__name__)

@app.route('/getRecommendation')
def getRecommendation():
    if 'uid' in request.args:
        uid = request.args.get('uid')
        return prediction(uid)
    else:
        return "No uid specified"


def prediction(firebase_id):
	model = load_model()
	data = pickle.load(open("list_data.sav", 'rb'))
	similar_users = []
	random_list = []

	try:
		idd = data.index[data['id'] == firebase_id].tolist()[0]
	except IndexError as e:
		# print data
		random_list += random.sample(data["id"], 5)
		return json.dumps(random_list)

	for i in model[idd]: # Removing the first one because it is itself
		similar_users.append(data.ix[i]["id"]) 
	similar_users = [x for x in similar_users if x!= firebase_id]
	json_string = json.dumps(similar_users)
	return json_string

def load_model():
	loaded_model = pickle.load(open("weights.sav", 'rb'))
	return loaded_model

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)
