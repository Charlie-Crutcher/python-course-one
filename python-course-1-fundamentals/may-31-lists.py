# What is a list?

# It is a built-in data structure that allows for a collection of a data in sequential order.

list_syntax = ["Square Brackets", "Commas Seperating Variables"]

# Lists may contain MULTIPLE DATATYPES in one list!

example = ["such as a string", "and an int", 12]

# They may also simply be initiliased without any contents

like_so = []

# a method can then be used to add contents to this list
# NOTE: When using 'append', it adds the element to the END of the list

like_so.append("the list now has contents")

# Contents can also be removed by using the .remove method:

like_so.remove("the list now has contents")

print(like_so)
print(list_syntax)

# Lists can also be combined (concatenated) together, in a similar fashion as two strings would.

like_so = like_so + example
print(like_so)

# If to add a single element using +, you must use it with brackets[]

like_so = like_so + ["Like this!"]
print(like_so)
