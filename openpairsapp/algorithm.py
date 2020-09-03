"""import time
from scipy.spatial.distance import euclidean
import sys

from .models import StudentDetail

class Response:
    
    def __init__(self, primary_key):
    
        people = StudentDetail.objects.all()
        self.full_name = people[primary_key].full_name 
        self.sex = people[primary_key].sex
        self.region = people[primary_key].region
        self.country = people[primary_key].country
        self.year_group = people[primary_key].year_group
        self.scores = [
            people[primary_key].temperature,
            people[primary_key].sleep,
            people[primary_key].sleep_school_time,
            people[primary_key].sleep_weekend_time,
            people[primary_key].wakeup_school_time,
            people[primary_key].wakeup_weekend_time,
            people[primary_key].sleep_light,
            people[primary_key].room_brightness_day,
            people[primary_key].room_brightness_night,
            people[primary_key].noise,
            people[primary_key].sleep_noise,
            people[primary_key].private_time,
            people[primary_key].meditate,
            people[primary_key].conversational,
            people[primary_key].sharing,
            people[primary_key].day_visitors,
            people[primary_key].night_visitors,
            people[primary_key].visiting_time,
            people[primary_key].quiet_space,
            people[primary_key].allergies,
            people[primary_key].room_decor,
            
        ]

people = StudentDetail.objects.all()
boys = [Response(i) for i in range(len(people)-1) if Response(i).sex=="Male"]
girls = [Response(i) for i in range(len(people)-1) if Response(i).sex=="Female"]

b_diction = {} 
boys_l = []
g_diction = {} 
girls_l = []

for i in range(len(boys)):
    for j in range(len(boys)):
        if j == i:#To avoid a comparism with one's self
            pass
        elif boys[i].year_group ==  boys[j].year_group:#y1s and y2s have to be roommates
            pass
        elif boys[i].country == boys[j].country:#people of the same country can't be roommates
            name = boys[j].full_name
            d = sys.maxsize #It makes the distance between them unbearable
            boys_l.append([name,d])
        else:
            name = boys[j].full_name
            d = euclidean(boys[i].scores,boys[j].scores)
            boys_l.append([name,d])
    boys_l.sort(key=lambda x : x[1]) #from mr max :) this line sorts the list by the dist number
    b_diction[boys[i].full_name] = boys_l
    boys_l = []

b_y1_dict = {}
b_y2_dict = {}

for b in boys: #Separates year 1s from year 2s
    if b.year_group == "Year One" or b.year_group == "Catalyst":
        b_y1_dict[b.full_name] = ""
    else:
        b_y2_dict[b.full_name] = ""

    
while True:
    for y1 in b_y1_dict.keys():
        if b_y1_dict[y1] == '' and b_diction[y1] != []: #while there is a free y1 who still has yet to propose to a y2:
            y2 = b_diction[y1].pop(0)[0] #That takes out the most prefered y2 from the year one's sorted list of preferences
            if b_y2_dict[y2] == '': #is that y2 not taken?
                b_y1_dict[y1] = y2 #The y2 becomes the y1's roommate
                b_y2_dict[y2] = y1 #The y1 becomes the y2's roommate
            else:
                y1o = b_y2_dict[y2]
                for tuple1 in b_diction[y2]:#increase index (keep going up the list) until you reach y1 or y1o
                    if tuple1[1] == y1: #if y1 is before y1o on the y2's list (y1, y2) become roommates
                        b_y1_dict[y1o] = ''
                        b_y1_dict[y1] = y2
                        b_y2_dict[y2] = y1
                        break
                    if tuple1[1] == y1o: #if y1o is before y1 on the y2's list(y1o, y2) stay roommates
                        break
        else:
            break

    if '' not in b_y1_dict.values():#Once everyone else has a pair
        break

#-------------------------------------------------------------------------------------------------#

for i in range(len(girls)):
    for j in range(len(girls)):
        if j == i:#To avoid a comparism with one's self
            pass
        elif girls[i].year_group ==  girls[j].year_group:#y1s and y2s have to be roommates
            pass
        elif girls[i].country == girls[j].country:#people of the same country can't be roommates
            name = girls[j].full_name
            d = sys.maxsize #It makes the distance between them unbearable
            girls_l.append([name,d])
        else:
            name = girls[j].full_name
            d = euclidean(girls[i].scores,girls[j].scores)
            girls_l.append([name,d])
    girls_l.sort(key=lambda x : x[1]) #from mr max :) this line sorts the list by the dist number
    g_diction[girls[i].full_name] = girls_l
    girls_l = []

g_y1_dict = {}
g_y2_dict = {}

for g in girls: #Separates year 1s from year 2s
    if g.year_group == "Year One" or g.year_group == "Catalyst":
        g_y1_dict[g.full_name] = ''
    else:
        g_y2_dict[g.full_name] = ''

while True:
    for y1 in g_y1_dict.keys():
        if g_y1_dict[y1] == '' and g_diction[y1] != []: #while there is a free y1 who still has yet to propose to a y2 and there is an available y2:
            y2 = g_diction[y1].pop(0)[0] #That takes out the most prefered y2 from the year one's sorted list of preferences
            if g_y2_dict[y2] == '': #is that y2 taken or not?
                g_y1_dict[y1] = y2 #The y2 becomes the y1's roommate
                g_y2_dict[y2] = y1 #The y1 becomes the y2's roommate
            else:
                y1o = g_y2_dict[y2]
                for tuple1 in g_diction[y2]:#increase index (keep going up the list) until you reach y1 or y1o
                    if tuple1[1] == y1: #if y1 is before y1o on the y2's list (y1, y2) become roommates
                        g_y1_dict[y1o] = ''
                        g_y1_dict[y1] = y2
                        g_y2_dict[y2] = y1
                        break
                    if tuple1[1] == y1o: #if y1o is before y1 on the y2's list(y1o, y2) stay roommates
                        break
        else:
            break
        
    if '' not in g_y1_dict.values():#Once everyone else has a pair
        break
# print(b_y1_dict)
# print(g_y1_dict)


#P.S.
#If right now, it is printing the list for girls, and I want the list for boys, or vice versa, all I have to do is to redefine the lists called girls and boys. Basically swapping what they are called. Line 21 and 22, just after the Response class
"""