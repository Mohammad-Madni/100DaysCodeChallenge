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