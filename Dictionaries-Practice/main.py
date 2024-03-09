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
