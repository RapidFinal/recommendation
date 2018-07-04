import numpy as np
import csv

# GENERATE THE DATASET FOR THE ALGORITHM WITH UID, TOP 3 SKILLS, SUB CATEGORY

subcategory = []
skills = []
output = []

skill_list = ["c++", "python", "ux", "frontend", "vue", "react-native", "spring", "case-competitions", "data-science", "data-analytics",
				"finance", "microsoft-word", "microsoft-excel", "powerpoint", "machine-learning"]

f = open("subcat.txt","r") 
for line in f:
    subcategory.append(line)


for item1 in skill_list:
	for item2 in skill_list:
		for item3 in skill_list:
			if item1 != item2 and item2 != item3:
				skills.append((item1, item2, item3))

print(len(skills))
print(len(subcategory))

id_ = 0
for each_skillset in skills:
	for each_sub in subcategory:
		output.append((id_, each_skillset, each_sub))
		id_+=1

with open('data.csv','wb') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['id','skill_set', 'subcategory'])
    for row in output:
        csv_out.writerow(row)

print("Done")