import pandas as pd
import pickle

def init():
	data = pd.read_csv("test_data.csv")
	data.index = data["id"]
	# data = data.drop(columns=["id"])
	data['subcategory'] = data["subcategory"].apply(lambda x: x.strip())

	# pd.get_dummies(data_2["skill_set"]).head() # Convert type to categorical values for ease
	data_features = pd.concat([pd.get_dummies(data[["subcategory"]]), pd.get_dummies(data[["skill_set"]]), 
		pd.get_dummies(data[["liked"]])], axis=1)

	from sklearn.preprocessing import MaxAbsScaler
	max_scaler = MaxAbsScaler()
	data_features = max_scaler.fit_transform(data_features)

	pickle.dump(data, open("list_data.sav","wb"))

	return data_features


def learn():
	features = init()
	print ("Learning")
	from sklearn.neighbors import NearestNeighbors

	neigh = NearestNeighbors(n_neighbors = 6, algorithm = 'ball_tree').fit(features)
	distances, indices = neigh.kneighbors(features)
	print ("Learned")
	pickle.dump(indices, open("weights.sav", 'wb'))