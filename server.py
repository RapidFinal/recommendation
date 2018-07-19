from flask import Flask, render_template, request
import pickle
import json

app = Flask(__name__)

@app.route('/getRecommendation')
def getRecommendation():
    if 'uid' in request.args:
        uid = request.args.get('uid')
        return prediction(int(uid))
    else:
        return "No uid specified"


def prediction(firebase_id):
	model = load_model()
	data = pickle.load(open("list_data.sav", 'rb'))
	similar_users = []
	for i in model[firebase_id][1:]: # Removing the first one because it is itself
		similar_users.append(data.ix[i]["id"]) #anime.ix[i]["name"]

	json_string = json.dumps(similar_users)
	return json_string

def load_model():
	loaded_model = pickle.load(open("weights.sav", 'rb'))
	return loaded_model

if __name__=='__main__':
    app.run(debug=True)
