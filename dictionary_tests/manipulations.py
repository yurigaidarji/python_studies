programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])
print(programming_dictionary)

programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

#Editting a key content
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

#Loop through dictionary
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])

# Wiping dictionary
programming_dictionary = {}
print(programming_dictionary)

# Accessing nested values
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

#printing a list value inside an dictionary
print(travel_log["France"][1])

#printing a list value inside a list
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_log2 = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
#printing Stuttgart
print(travel_log2["Germany"]["cities_visited"][2])