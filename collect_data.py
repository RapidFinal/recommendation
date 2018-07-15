import numpy as np
import csv

# GENERATE THE DATASET FOR THE ALGORITHM WITH UID, TOP 3 SKILLS, SUB CATEGORY

subcategory = []
skills = []
output = []

# graphic_and_design = ["ux", "ui", "adobe-illustrator", "adobe-photo", "adobe-xd", "adobe-premiere-pro", "adobe-after-effect", "final-cut-pro",
# 				"adobe-muse"]

# marketing_and_advertisement = ["microsoft-office", "microsoft-word", "microsoft-excel", "microsoft-powerpoint", "management", "research", "digital-marketing",
# 				"integrated-marketing", "marketing-strategy", "marketing", "advertising", "social-media-marketing", "direct-marketing", 
# 				"market-planning"]

# writing_and_translation = ["translation", "editing", "blogging", "interpreting", "social-media", "creative-writing", "proofreading", "education" 
# 				, "technical-translation", "multilingual"]

# visual_and_sound = ["adobe-illustrator", "adobe-photoshop", "adobe-premiere-pro", "adobe-after-effect", "final-cut-pro",
#  				"adobe-muse", "adobe-illustrator", "digital-marketing", "adobe-lightroom", "photography", "cinematography", 
#  				"web-design", "concept-development", "3d-modeling", "fl-studio", "ableton"]

# web_and_programming = ["react-js", "javascript", "react-native", "wordpress", "php", "ios", "android", "data-science",
# 				"spring", "java", "c++", ".NET", "html", "css", "desktop-application"]

# consult_and_advise = ["consulting", "advising", "career-growth", "startup", "financial-modeling", "valuation", "investment-banking",
# 				"business-valuation"]

online_shop_management = ["admin", "data-entry", "accounting", "call-center", "salesman", "website-admin", "tax", "shop-management", 
			"telesale"]

f = open("subcat.txt","r") 
for line in f:
    subcategory.append(line)


for item1 in skill_list:
	for item2 in skill_list:
		for item3 in skill_list:
			if item1 != item2 and item2 != item3 and item1 != item3:
				skills.append((item1, item2, item3))

print(len(skills))
print(len(subcategory))

id_ = 0
for each_skillset in skills:
	for each_sub in subcategory:
		output.append((id_, each_skillset, each_sub))
		id_+=1

with open('online_shop_management.csv','w+') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['id','skill_set', 'subcategory'])
    for row in output:
        csv_out.writerow(row)	

print("Done")