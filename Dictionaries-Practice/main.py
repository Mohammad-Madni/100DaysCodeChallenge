#nested list with dictionaries for multiple values in a single key

#There can be nested list which mean lists in lists

# and there are nested dictionaries which are dict's in dictionary

# we can nest list in dict and dict in list

#Normal dictionary
countries = {
    "Pakistan" : "Islamabad",
    "China" : "Beijing",
    "Total_Debt" : 27
}

#Normal List
districts = ["Naushahro Feroze", "Sukkur", "Hyderabad"]

# Nesting a list in a dictionary
travel_log = {
    "France" : ["paris", "lilie" , "dijon"],
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting a list in a list
asian_countries = ["Pakistan","India",["Bangladesh,Srilanka"]]

# Nesting a Dict in a Dict
travel_log = {
    "France" : {"cities_visted": ["paris", "lilie", "dijon"], "No_times_visited" : 7},
    "Germany" : {"cities_visted": ["Berlin", "Hamburg", "Stuttgart"],"No_times_visited" : 5},
}

# Nesting Dict in a list
travel_log = [
    {
        "Country" : "France",
        "cities_visted": ["paris", "lilie", "dijon"],
        "No_times_visited" : 7},
    {
        "Country": "Germany",
        "cities_visted": ["Berlin", "Hamburg", "Stuttgart"],
        "No_times_visited" : 5},
]

# short program with dictionaries
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
def calculate(grades):
  for student in grades:

      value = student_scores[student]
      if value > 90:
          student_grades[student] = "Outstanding"
      elif value > 80:
          student_grades[student] = "Exceeds Expectations"
      elif value > 70:
          student_grades[student] = "Acceptable"
      elif value <= 70:
          student_grades[student] = "Fail"
calculate(student_scores)

# 🚨 Don't change the code below 👇
print(student_grades)

# Dictionary in list Program
country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log.
def add_new_country(name, visit, list_of_city):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = visit
  new_country["cities"] = list_of_city
  travel_log.append(new_country)
# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")







