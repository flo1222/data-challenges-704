# pylint: disable=missing-docstring

# Warning:
# - One line of code for each method
# - Just look in the doc for the right method of the String class!

def add_comma(a_string):
    return a_string.replace(" ", ", ")

def belongs_to(a_string, a_word):
    return a_word in a_string

def count_repetition(a_string, a_substring):
    return a_string.count(a_substring)
    # example: count_repetition("000123000123", "0") => 6
print(count_repetition("000123000123", "0"))

def is_a_question(a_string):
    return '?' in a_string[-1]
    # example: is_a_question("How are you?") => True
print(is_a_question("How are you?"))

def remove_surrounding_whitespaces(a_string):
    return a_string.strip()
    # example: delete_surrounding_whitespaces("  hey yo  ") => "hey yo"
print(remove_surrounding_whitespaces("  hey yo  "))

def replace(initial_string, old_letter, new_letter):
    return initial_string.replace(old_letter, new_letter)
    # example: replace("casanova", "a", "o") => "cosonovo"
print(replace("casanova", "a", "o"))

def full_description_concatenation(first_name, last_name, age):
    return first_name.capitalize() + ' ' + last_name.capitalize() + ' is ' + str(age)
    # example: full_description_concatenation("john", "doe", 33) => "John Doe is 33"
print(full_description_concatenation("john", "doe", 33))

def full_description_formatting(first_name, last_name, age):
    return f"{first_name.capitalize()} {last_name.capitalize()} is {age}"
    # example: full_description_formatting("john", "doe", 33) => "John Doe is 33"
