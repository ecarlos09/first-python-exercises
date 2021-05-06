my_hometown = "Hillingdon"
hometown_stats = {
    "location": 'London',
    "founded": '01/04/1965',
    "population": 306870,
    "area_sq_miles": 44,
}

def pop_density(population, area):
    return population/area

def inform_user(hometown="Somewhere", pop_density="undetermined!"):
    return f"{hometown}'s population density is {pop_density}."

print(inform_user(my_hometown, pop_density(hometown_stats["population"], hometown_stats["area_sq_miles"])))
    # Will print "Hillingdon's population density is 6974.318181818182."
print(inform_user())
    # Will print "Somewhere's population density is undetermined!"