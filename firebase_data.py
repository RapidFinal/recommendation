import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import csv
import os


FILENAME = "test_data.csv"
try:
	os.remove(FILENAME)
except Exception as e:
	pass


cred = credentials.Certificate('service.json')
firebase_admin.initialize_app(cred, {
	'databaseURL': "https://jobme-212ee.firebaseio.com/"
	})


def firebase_fetch():
	print ("Fetching ")
	ref = db.reference('employeeInfo')
	category_ref = db.reference('categories')
	tags_ref = db.reference('tags')


	employee_output = ref.get()
	category_output = category_ref.get()
	tags_output = tags_ref.get()

	firstTime = True

	for each_user in employee_output:
		name_of_subcat = []
		name_of_tags = []
		to_write = []
		# print (each_user)
		details = employee_output[each_user]
		# print (details)
		categories = details["categories"]
		tagIds = details["tagIds"]
		liked = details["liked"]

		# Converting Sub category Ids to names
		for each_cat in categories:
			category = category_output[each_cat]

			subs = category["subCategories"]
			
			list_of_subcat_id =  categories[each_cat]
			list_of_subcat_id = list_of_subcat_id["subCategoryIds"]

			for each_sub_cat in list_of_subcat_id:
				subcat_data = subs[each_sub_cat]
				name = subcat_data['subCategoryName']
				name_of_subcat.append(name)

			# print (name_of_subcat)

		# Converting tagIds to names
		for each_tag in tagIds:
			tag = tags_output[each_tag]
			tag_name = tag["tagName"]
			name_of_tags.append(tag_name)
		# print (name_of_tags)

		to_write.append((each_user, name_of_tags, name_of_subcat, liked))

		with open(FILENAME,'a+') as out:
		    csv_out=csv.writer(out)
		    if firstTime: 
		    	csv_out.writerow(['id','skill_set', 'subcategory', 'liked'])
		    	firstTime = False
		    for row in to_write:
		        csv_out.writerow(row)
