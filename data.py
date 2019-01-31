import csv
import re
from itertools import zip_longest
# open the file in universal line ending mode 
file = open('datasets/business.csv', encoding="latin1")
important_attributes = ['attributes_Alcohol','attributes_Ambience']

def check_important_attr(header):
    for x in important_attributes:
        if (x == header):
            return True
    return False

	
with file as infile:
  # read the file as a dictionary for each row ({header : value})
    reader = csv.DictReader(infile)
    data = {}
    for row in reader:
        for header, value in row.items():
            try:
                data[header].append(value)			
            except KeyError:
                data[header] = [value]
				
########converts attributes_Alcohol################				
    attributes_Alcohol = data['attributes_Alcohol']
    for n,i in enumerate(attributes_Alcohol):
        if i == "beer_and_wine":
            attributes_Alcohol[n] = 1
        elif i == "full_bar":
            attributes_Alcohol[n] = 1
        else: 
            attributes_Alcohol[n] = 0   		
##################################################

#########converts attributes_ambience##############
    attributes_Ambience = data['attributes_Ambience']

    #break up into different parts of ambience
    attributes_casual = data['attributes_Ambience'].copy()
    attributes_romantic = data['attributes_Ambience'].copy() 
    attributes_intimate = data['attributes_Ambience'].copy()
    attributes_classy = data['attributes_Ambience'].copy()
    attributes_hipster = data['attributes_Ambience'].copy()
    attributes_touristy = data['attributes_Ambience'].copy()
    attributes_trendy = data['attributes_Ambience'].copy()
    attributes_upscale = data['attributes_Ambience'].copy()

	#####if empty, defaults to casual
    for n,i in enumerate(attributes_Ambience):
        if "'casual': False" in i:
            attributes_casual[n] = 0
        elif "'casual': True" in i:
            attributes_casual[n] = 1
        else: 
            attributes_casual[n] = 1

        if "'romantic': False" in i:
            attributes_romantic[n] = 0
        elif "'romantic': True" in i:
            attributes_romantic[n] = 1
        else: 
            attributes_romantic[n] = 1

        if "'intimate': False" in i:
            attributes_intimate[n] = 0
        elif "'intimate': True" in i:
            attributes_intimate[n] = 1
        else: 
            attributes_intimate[n] = 1

        if "'classy': False" in i:
            attributes_classy[n] = 0
        elif "'classy': True" in i:
            attributes_classy[n] = 1
        else: 
            attributes_classy[n] = 1

        if "'hipster': False" in i:
            attributes_hipster[n] = 0
        elif "'hipster': True" in i:
            attributes_hipster[n] = 1
        else: 
            attributes_hipster[n] = 1

        if "'touristy': False" in i:
            attributes_touristy[n] = 0
        elif "'touristy': True" in i:
            attributes_touristy[n] = 1
        else: 
            attributes_touristy[n] = 1

        if "'trendy': False" in i:
            attributes_trendy[n] = 0
        elif "'trendy': True" in i:
            attributes_trendy[n] = 1
        else: 
            attributes_trendy[n] = 1

        if "'upscale': False" in i:
            attributes_upscale[n] = 0
        elif "'upscale': True" in i:
            attributes_upscale[n] = 1
        else: 
            attributes_upscale[n] = 1

    #attributes_casual = data['attributes_casual']
	# to add any other attributes under ambience besides casual:
	# ex. attributes_trendy = data['attributes_trendy']
	#for n,i in enumerate(attributes_trendy):
    #    if "'trendy': False" in i:
    #        attributes_casual[n] = 0
    #    elif "'trendy': True" in i:
    #        attributes_casual[n] = 1
    #    else: 
    #        attributes_casual[n] = 1   make judgement call here


##################attributes_BestNights##################
# 1 for attributes_BikeParking=True
# 0 for attributes_BikeParking= False or empty 
#########################################################
    attributes_BestNights = data['attributes_BestNights']

    attributes_BestNights_M = data['attributes_BestNights'].copy()
    attributes_BestNights_Tu = data['attributes_BestNights'].copy() 
    attributes_BestNights_W = data['attributes_BestNights'].copy()
    attributes_BestNights_Th = data['attributes_BestNights'].copy()
    attributes_BestNights_F = data['attributes_BestNights'].copy() 
    attributes_BestNights_Sat = data['attributes_BestNights'].copy()
    attributes_BestNights_Sun = data['attributes_BestNights'].copy()

    for n,i in enumerate(attributes_BestNights):
        if "'monday': False" in i:
            attributes_BestNights_M[n] = 0
        elif "'monday': True" in i:
            attributes_BestNights_M[n] = 1
        else: 
            attributes_BestNights_M[n] = 1

        if "'tuesday': False" in i:
            attributes_BestNights_Tu[n] = 0
        elif "tuesday': True" in i:
            attributes_BestNights_Tu[n] = 1
        else: 
            attributes_BestNights_Tu[n] = 1

        if "wednesday': False" in i:
            attributes_BestNights_W[n] = 0
        elif "wednesday': True" in i:
            attributes_BestNights_W[n] = 1
        else: 
            attributes_BestNights_W[n] = 1

        if "thursday': False" in i:
            attributes_BestNights_Th[n] = 0
        elif "thursday': True" in i:
            attributes_BestNights_Th[n] = 1
        else: 
            attributes_BestNights_Th[n] = 1

        if "'friday': False" in i:
            attributes_BestNights_F[n] = 0
        elif "'friday': True" in i:
            attributes_BestNights_F[n] = 1
        else: 
            attributes_BestNights_F[n] = 1

        if "'saturday': False" in i:
            attributes_BestNights_Sat[n] = 0
        elif "'saturday': True" in i:
            attributes_BestNights_Sat[n] = 1
        else: 
            attributes_BestNights_Sat[n] = 1

        if "'sunday': False" in i:
            attributes_BestNights_Sun[n] = 0
        elif "'sunday': False" in i:
            attributes_BestNights_Sun[n] = 1
        else: 
            attributes_BestNights_Sun[n] = 1


##################attributes_BikeParking##################
# 1 for attributes_BikeParking=True
# 0 for attributes_BikeParking= False or empty 
#########################################################
    attributes_BikeParking = data['attributes_BikeParking']
    for n,i in enumerate(attributes_BikeParking):
        if i == "False":
            attributes_BikeParking[n] = 0
        elif i == "True":
            attributes_BikeParking[n] = 1
        else:
            attributes_BikeParking[n] = 0

##################attributes_Caters##################
# 1 for attributes_Caters=True
# 0 for attributes_Caters= False or empty 
#########################################################
    attributes_Caters = data['attributes_Caters']
    for n,i in enumerate(attributes_Caters):
        if i == "False":
            attributes_Caters[n] = 0
        elif i == "True":
            attributes_Caters[n] = 1
        else:
            attributes_Caters[n] = 0

##################attributes_HasTV##################
# 1 for attributes_HasTV=True
# 0 for attributes_HasTV= False or empty 
#########################################################
    attributes_HasTV = data['attributes_HasTV']
    for n,i in enumerate(attributes_HasTV):
        if i == "False":
            attributes_HasTV[n] = 0
        elif i == "True":
            attributes_HasTV[n] = 1
        else:
            attributes_HasTV[n] = 0

##################attributes_OutdoorSeating##################
# 1 for attributes_OutdoorSeating=True
# 0 for attributes_OutdoorSeating= False or empty 
#########################################################
    attributes_OutdoorSeating = data['attributes_OutdoorSeating']
    for n,i in enumerate(attributes_OutdoorSeating):
        if i == "False":
            attributes_OutdoorSeating[n] = 0
        elif i == "True":
            attributes_OutdoorSeating[n] = 1
        else:
            attributes_OutdoorSeating[n] = 0


##################attributes_RestaurantsTakeOut##################
# 1 for attributes_RestaurantsTakeOut=True
# 0 for attributes_RestaurantsTakeOut= False or empty 
#########################################################
    attributes_RestaurantsTakeOut = data['attributes_RestaurantsTakeOut']
    for n,i in enumerate(attributes_RestaurantsTakeOut):
        if i == "False":
            attributes_RestaurantsTakeOut[n] = 0
        elif i == "True":
            attributes_RestaurantsTakeOut[n] = 1
        else:
            attributes_RestaurantsTakeOut[n] = 0


##################attributes_WiFi##################
# 1 for attributes_WiFi=free
# 0 for attributes_WiFi=no or empty 
#########################################################
    attributes_WiFi = data['attributes_WiFi']
    for n,i in enumerate(attributes_WiFi):
        if i == "no":
            attributes_WiFi[n] = 0
        elif i == "free":
            attributes_WiFi[n] = 1
        else:
            attributes_WiFi[n] = 0




######################################################

############################STARS###########################
    attributes_stars = data['stars']
	
############################################################

###########################noise_level######################
    attributes_noise = data['attributes_NoiseLevel']
    for n,i in enumerate(attributes_noise):
        if i == "quiet":
            attributes_noise[n] = 0
        elif i == "average":
            attributes_noise[n] = 1
        elif i == "loud": 
            attributes_noise[n] = 2
        elif i == "very_loud":	
            attributes_noise[n] = 3
        else:	#default average
            attributes_noise[n] = 1		

###############################attributes_RestaurantsGoodForGroups#############
    attributes_RestaurantsGoodForGroups = data['attributes_RestaurantsGoodForGroups']
    for n,i in enumerate(attributes_RestaurantsGoodForGroups):
        if i == "True":
            attributes_RestaurantsGoodForGroups[n] = 1
        elif i == "False":
            attributes_RestaurantsGoodForGroups[n] = 0
        else:
            attributes_RestaurantsGoodForGroups[n] = 0  
			
###############################is_open#############################################
    attributes_is_open =  data['is_open']
########################################################

######################categories ########################
    attributes_is_restaurant = data['categories']
    for n,i in enumerate(attributes_is_restaurant):
        if "Restaurants" in i:
            attributes_is_restaurant[n] = 1
        else:
            attributes_is_restaurant[n] = 0
#currently just looks at whether or not it is a restaurant. might consider breaking down categories more
###########################################################

#####################attributes_WheelchairAccessible#######################
    attributes_WheelchairAccessible = data['attributes_WheelchairAccessible']
    for n,i in enumerate(attributes_WheelchairAccessible):
        if i == "True":
            attributes_WheelchairAccessible[n] = 1
        elif i == "False":
            attributes_WheelchairAccessible[n] = 0
        else:			
            attributes_WheelchairAccessible[n] = 1
#####################################################


#######################attributes_RestaurantsPriceRange2#####################
    attributes_RestaurantsPriceRange2 = data['attributes_RestaurantsPriceRange2']
    for n,i in enumerate(attributes_RestaurantsPriceRange2):
        if i == '':
            attributes_RestaurantsPriceRange2[n] = '0'
####################################################################

######################restaurant reservations#############################
    attributes_RestaurantsReservations = data['attributes_RestaurantsReservations']
    for n,i in enumerate(attributes_RestaurantsReservations):
        if i == "True":
            attributes_RestaurantsReservations[n] = 1
        elif i == "False":
            attributes_RestaurantsReservations[n] = 0
        else:			
            attributes_RestaurantsReservations[n] = 0	
##############################################################################		


##########################attributes_RestaurantsDelivery#####################
    attributes_RestaurantsDelivery = data['attributes_RestaurantsDelivery']
    for n,i in enumerate(attributes_RestaurantsDelivery):
        if i == "True":
            attributes_RestaurantsDelivery[n] = 1
        elif i == "False":
            attributes_RestaurantsDelivery[n] = 0
        else:			
            attributes_RestaurantsDelivery[n] = 0
###############################################################################

#############################good for kids##############
    attributes_GoodForKids = data['attributes_GoodForKids']
    for n,i in enumerate(attributes_GoodForKids):
        if i == "True":
            attributes_GoodForKids[n] = 1
        elif i == "False":
            attributes_GoodForKids[n] = 0
        else:			
            attributes_GoodForKids[n] = 0
###########################################################

######################attributes_BusinessAcceptsCreditCards###########
    attributes_BusinessAcceptsCreditCards = data['attributes_BusinessAcceptsCreditCards']
    for n,i in enumerate(attributes_BusinessAcceptsCreditCards):
        if i == "True":
            attributes_BusinessAcceptsCreditCards[n] = 1
        elif i == "False":
            attributes_BusinessAcceptsCreditCards[n] = 0
        else:			
            attributes_BusinessAcceptsCreditCards[n] = 1    
######################################################################

####################attributes_BusinessParking########################
    attributes_BusinessParking = data['attributes_BusinessParking']
    for n,i in enumerate(attributes_BusinessParking):
        if "'street': True" in i:
            attributes_BusinessParking[n] = 1
        elif "'lot': True" in i:
            attributes_BusinessParking[n] = 1
        elif "'garage': True" in i:
            attributes_BusinessParking[n] = 1
        else: 
            attributes_BusinessParking[n] = 0

#######################attributes_RestaurantsAttire###################
    attributes_RestaurantsAttire = data['attributes_RestaurantsAttire']
    for n,i in enumerate(attributes_RestaurantsAttire):
        if "casual" in i:
            attributes_RestaurantsAttire[n] = 0
        elif "dressy" in i:
            attributes_RestaurantsAttire[n] = 1
        else: 
            attributes_RestaurantsAttire[n] = 0
##############################################################

############################review_count##########################
    review_count = data['review_count']
    for n,i in enumerate(review_count):
        if int(i) < 150:
            review_count[n] = 1
        elif int(i)>= 150 and int(i) < 250:
            review_count[n] = 2
        elif int(i)>= 250 and int(i) < 500:
            review_count[n] = 3
        else: 
            review_count[n] = 4			
#classify number of reviews left for a restaurant into 4 categories. based off visualization of data to see distribution of review counts
####################################################################

###############################good for what number of meals (dessert, lunch, dinner, etc.)#####################################
    attributes_GoodForMeal = data['attributes_GoodForMeal']
	#for data visualization purposes
    count_0 = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    for n,i in enumerate(attributes_GoodForMeal):
        count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("True"), i))
        if count == 0:
             count_0 += 1
        if count == 1:
             count_1 += 1
        if count == 2:
             count_2 += 1
        if count == 3:
             count_3 += 1
        if count == 4:
             count_4 += 1
        if count >= 5:
             count_5 += 1
        attributes_GoodForMeal[n] = count
	#print to see distribution of goodformeal attribute
    #print (count_0)
    #print (count_1)
    #print (count_2)
    #print (count_3)
    #print (count_4)
    #print (count_5)
############################################################

######################attributes_RestaurantsTableService#############
    attributes_RestaurantsTableService = data['attributes_RestaurantsTableService']
    for n,i in enumerate(attributes_RestaurantsTableService):
        if i == "True":
            attributes_RestaurantsTableService[n] = 1
        elif i == "False":
            attributes_RestaurantsTableService[n] = 0
        else:			
            attributes_RestaurantsTableService[n] = 0  
###business id
    business_id = data['business_id']

    d = [
    attributes_Alcohol, attributes_casual, attributes_romantic, attributes_intimate, attributes_classy, 
    attributes_hipster, attributes_touristy, attributes_trendy, attributes_upscale, attributes_BestNights_M, 
    attributes_BestNights_Tu,  attributes_BestNights_W, attributes_BestNights_Th, attributes_BestNights_F,  attributes_BestNights_Sat, attributes_BestNights_Sun,
    attributes_BikeParking, 
    attributes_Caters, attributes_HasTV, attributes_OutdoorSeating, attributes_RestaurantsTakeOut, attributes_WiFi,
    attributes_stars, attributes_noise, attributes_RestaurantsGoodForGroups, attributes_is_open, attributes_is_restaurant, 
    attributes_WheelchairAccessible, attributes_RestaurantsPriceRange2, attributes_RestaurantsReservations, attributes_RestaurantsDelivery, attributes_GoodForKids, 
    attributes_BusinessAcceptsCreditCards, attributes_BusinessParking, attributes_RestaurantsAttire, review_count, attributes_GoodForMeal, 
    attributes_RestaurantsTableService, business_id
    ]
    export_data = zip_longest(*d, fillvalue = '')
    with open('datasets/business_attributes.csv', 'w', encoding="latin1", newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(("attributes_Alcohol", "attributes_casual", "attributes_romantic", "attributes_intimate", "attributes_classy", 
        "attributes_hipster", "attributes_touristy", "attributes_trendy", "attributes_upscale", 
        "attributes_BestNights_M", "attributes_BestNights_Tu", "attributes_BestNights_W", "attributes_BestNights_Th", "attributes_BestNights_F",  "attributes_BestNights_Sat", "attributes_BestNights_Sun", 
        "attributes_BikeParking", 
        "attributes_Caters", "attributes_HasTV", "attributes_OutdoorSeating", "attributes_RestaurantsTakeOut", "attributes_WiFi",
         "attributes_stars", "attributes_NoiseLevel", "attributes_RestaurantsGoodForGroups", "is_open", "is_restaurant", 
         "attributes_WheelchairAccessible", "attributes_RestaurantsPriceRange2", "attributes_RestaurantsReservations", "attributes_RestaurantsDelivery", "attributes_GoodForKids", 
         "attributes_BusinessAcceptsCreditCards", "attributes_BusinessParking", "attributes_RestaurantsAttire", "review_count", "attributes_GoodForMeal",
         "attributes_RestaurantsTableService", "business_id"))
        wr.writerows(export_data)				
   
			
