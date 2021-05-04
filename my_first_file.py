# Initial exercise
print("Hello World!")

# Number methods
my_number = 36041

print(type(my_number))
print(float(my_number))

# String methods

some_sentences = "I’m learning python for the very first time this morning! We’re having a great time."
the_same_sentences = '"I’m learning python for the very first time this morning! We’re having a great time."'
newline_sentences = "I’m learning python for the very first time this morning!\nWe’re having a great time."
uppercase_sentences = some_sentences.upper()
split_sentences = newline_sentences.rsplit("\n")

print(some_sentences)
print(the_same_sentences)
print(newline_sentences)
print(uppercase_sentences)
print(split_sentences)

# List methods

my_number_list = [ 1, 2, 69 ]
first_element = my_number_list[0]
my_number_list[2] = 3.14
third_element = my_number_list[2]

print(my_number_list)
print(first_element)
print(f"Changed the third element to {third_element}")

# Tuple methods

my_first_tuple = ( "This is", "my first", "tuple" )
is_hello_in_my_first_tuple = "hello" in my_first_tuple

print(my_first_tuple)
print(is_hello_in_my_first_tuple)

# Dictionary methods

my_first_dictionary = {
    "name": "Elwin",
    "python_skill_level": 2,
    "coffee_this_morning?": True,
    "password": "nonyabidness"
}

my_name = my_first_dictionary["name"]
my_python_skill_level = my_first_dictionary["python_skill_level"]
my_first_dictionary["python_skill_level"] += 1
my_languages = ("HTML", "CSS", "JavaScript", "Python", "Ruby", "C++")
my_first_dictionary["languages"] = my_languages

print(my_name)
print(f"My new Python skill level is {my_python_skill_level}")
print(my_first_dictionary)

# Set methods

my_favourite_foods = { "Percy Pigs", "Colin the Caterpillar", "Haribo Supermix" }

my_favourite_foods.remove("Haribo Supermix")
my_favourite_foods.add("Haribo Tangfastics")
set_length = len(my_favourite_foods)

print(my_favourite_foods)
print(set_length)