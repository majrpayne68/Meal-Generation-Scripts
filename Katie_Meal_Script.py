# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from random import randint
from numpy import linalg
from collections import Counter
import numpy

# f = open('Test.txt', 'w')
# f.write("I have reset the content."
#         "Pray I do not reset it further")
# f.close()

# f = open("Test.txt", "r")
# print(f.read())


Line1 = "Monday: "
Line2 = "Tuesday: "
Line3 = "Wednesday: "
Line4 = "Thursday: "
Line5 = "Friday: "
Line6 = "Saturday: "
Line7 = "Sunday: "
# Create storage array for the days of the week
D = [Line1,Line2,Line3,Line4,Line5,Line6,Line7]

mylines = []
with open('Meal_List.txt','rt') as myfile:
    for myline in myfile:
        mylines.append(myline)
myrecipes = []
with open('My_Recipes.txt','rt') as myrecipefile:
    for myrecipe in myrecipefile:
        myrecipes.append(myrecipe)
# print(mylines)
# print(myrecipes)

days = 7
days = int(days)
Saved_Meals = numpy.size(mylines)
Meal_Rand = [1,1,1,1,1,1,1]
flag = False

while flag is False:
    Meal_Rand = [randint(1,(Saved_Meals-1)) for p in range(0,(days))]
    flag = len(set(Meal_Rand)) == len(Meal_Rand)


Meal_Storage = [mylines[Meal_Rand[0]],mylines[Meal_Rand[1]],mylines[Meal_Rand[2]],mylines[Meal_Rand[3]],mylines[Meal_Rand[4]],mylines[Meal_Rand[5]],mylines[Meal_Rand[6]]]
Recipe_Storage = [myrecipes[Meal_Rand[0]],myrecipes[Meal_Rand[1]],myrecipes[Meal_Rand[2]],myrecipes[Meal_Rand[3]],myrecipes[Meal_Rand[4]],myrecipes[Meal_Rand[5]],myrecipes[Meal_Rand[6]]]


# print(Meal_Storage)

f = open("Katie's Meal Plan.txt", 'w')
f.write('Dinner Schedule for Current Week')
f.writelines(("\n \n %s %s %s \n %s %s %s \n %s %s %s \n %s %s %s \n %s %s %s \n %s %s %s \n %s %s %s " 
              % (D[0], Meal_Storage[0], Recipe_Storage[0], D[1], Meal_Storage[1], 
                 Recipe_Storage[1], D[2], Meal_Storage[2], Recipe_Storage[2], D[3], 
                 Meal_Storage[3], Recipe_Storage[3], D[4], Meal_Storage[4], 
                 Recipe_Storage[4], D[5], Meal_Storage[5], Recipe_Storage[5], 
                 D[6], Meal_Storage[6], Recipe_Storage[6])))
f.close()

f = open("Katie's Meal Plan.txt",'r')
print(f.read())
