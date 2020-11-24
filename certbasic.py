# Key Competencies:
#
#     Scalar Types, Operators and Control Flow - Define,
#       call and return from functions, create and break out of for and while loops,
#       use conditional branching, iterate lists and multiple lists (using zip).
#     Types (Strings, Collections, and Iteration) - Knowledge of scalar data types,
#       lists, dictionaries, sets, tuples, etc. Knowledge of iterable and mutable types.
#     Modular Program Design - Knowledge of modular design concept, import complete modules,
#       or individual classes. Understand the use-cases for object-oriented and procedural programming
#     Object-Oriented Programming - Understand when the use of classes is appropriate, create classes.
#       Initialize, modify, and retrieve class attributes.
#

import math  # math module name must prefix all its members
print('PI: '+str(math.pi))
piStr: str = '%.5f' % math.pi
print('PI STR: '+piStr)

from math import pi  # specifically 'pi' is now directly available
print('PI: '+str(pi))
piStr = '%.5f' % pi
print('PI STR: '+piStr)

from math import *  # sqrt is now directly available
print('PI SQRT: '+str(sqrt(pi)))
piStr = '%.5f' % sqrt(pi)
print('PI SQRT STR: '+piStr)

def docstring():
    """
    This is a function docstring
    You can also use:
    ''' Function Docstring '''
    """
    return pi

print(docstring.__doc__, docstring(), '\n')

#
# Exceptions
#
def spam(divideBy):
     try:
         return 42 / divideBy
     except ZeroDivisionError as e:
         print('Error: Invalid argument: {}'.format(e))
     finally:
         print("-- division finished --")
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))


from inheritance import *

me_undergraduate = Student("Noah N.", "O'Consequence")
me_graduate = StudentGraduate("Noah N.", "O'Consequence", 1993, 1999)
print("Undergrad: ", me_undergraduate.name())
print("Grad: ", me_graduate.name(), ", years attended: ", me_graduate.years_attended())

from inheritance2 import *

print("Rect Area: ", Rectangle(12.4, 28.7).area())
print("Circle Area: ", Circle(1234.56789).area())
print("Car: ", Car(151, "km/h"))
print("Boat: ", Boat(77))

import requests

year = 2011
name = 'UEFA Champions League'
urlPrefix = "https://jsonmock.hackerrank.com/api/football_competitions?name="+name+"&year="+str(year)+"&page="
response = requests.get(urlPrefix+str(1))
print(response.json())
team = response.json()['data'][0]['winner']
#team = 'Barcelona'
urlPrefix = "https://jsonmock.hackerrank.com/api/football_matches?year="+str(year)+"&team1=" + team + "&page="
response = requests.get(urlPrefix+str(1))
responseJson = response.json()
print(response.json())
totalPages = responseJson['total_pages']
pageNos = list(range(totalPages))
for pageNo in pageNos:
    print(str(pageNo))
print(pageNos)
totalGoals = 0
for pageNo in pageNos:
    url = urlPrefix+str(pageNo+1)
    print(url)
    response = requests.get(url)
    responseJson = response.json();
    data = responseJson['data']
    for i, match in enumerate(data):
        if (match['competition'] == name):
            print(match['team1'])
            totalGoals += int(match['team1goals'])
urlPrefix = "https://jsonmock.hackerrank.com/api/football_matches?year="+str(year)+"&team2=" + team + "&page="
response = requests.get(urlPrefix+str(1))
responseJson = response.json()
print(response.json())
totalPages = responseJson['total_pages']
pageNos = list(range(totalPages))
for pageNo in pageNos:
    print(str(pageNo))
print(pageNos)
for pageNo in pageNos:
    url = urlPrefix+str(pageNo+1)
    print(url)
    response = requests.get(url)
    responseJson = response.json();
    data = responseJson['data']
    for i, match in enumerate(data):
        if (match['competition'] == name):
            print(match['team2'])
            totalGoals += int(match['team2goals'])

print(totalGoals)

print('FUCK YOU')