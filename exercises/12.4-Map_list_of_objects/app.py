import datetime

def calculateAge(birthDate):
	today = datetime.date.today()
	age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
	return age

# print(calculateAge(datetime.datetime(1986,10,24)))

people = [
	{ "name": 'Joe', "birthDate": datetime.datetime(1986,10,24) },
	{ "name": 'Bob', "birthDate": datetime.datetime(1975,5,24) },
	{ "name": 'Erika', "birthDate": datetime.datetime(1989,6,12) },
	{ "name": 'Dylan', "birthDate": datetime.datetime(1999,12,14) },
	{ "name": 'Steve', "birthDate": datetime.datetime(2003,4,24) }
]

# name_list = list(map(lambda person : "Hello, my name is" + person["name"] + " and I am " + str(calculateAge(person["birthDate"])) + " years old", people))
# print(name_list)

# name_list = list(map(lambda person: "Hello, my name is " + person["name"] + " and I am " + str(calculateAge(person["birthDate"])) + " years old"  , people))
name_list = list(map(lambda person: "Hello, my name is " + person["name"] + " and I am " + str(calculateAge(person["birthDate"])) + " years old"  , people))
print(name_list)   

# greetings = []
# for person in people:
# 	age = calculate_year(person["birthDate"])
# 	greeting = f"Hello, my name is {person['name']} and I am {age} years old"
# 	greetings.append(greeting)

# print(greetings)