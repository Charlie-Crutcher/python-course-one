# This code file discusses some new concepts learnt 29th May.

# Storing Variables or vars.
this_is_a_variable = "Which stores data for reuse."
variables_cannot_start_with_numbers = "But can have numbers after the first letter."

# Errors
syntax_error = "The syntax is incorrect (obviously)."
name_error = "Occurs when the Python interpreter sees a word it doesn't recognize."
example = "This could be calling a variable that was never defined."

# Number data types
an_integer_or_int_stores_whole_numbers = 23
a_float_gives_an_approximation = 2.32323
# However a decimal should be used when pinpoint accuracy is necessary, especially when using math.
decimal_accuracy = 23.2378217719825378162389612793

# When trying to perform arithmetic, an int cannot be used in conjunction with a float.
# However, python 3 automatically converts integers to floats as needed.

# Exponents or powers
exponent = 2 ** 10
this_meaning = "2 to the power of 10 (1024)."

# Modulo or the remaining amount after division
modulo = 4 % 2
print(modulo)
modulo_not_zero = 25 % 2
print(modulo_not_zero)

# String concatenation
combining_strings = "This is called "
concatenation = "String Concatenation"
combining = combining_strings + concatenation
print(combining)

# However, a string cannot be concatenated with an integer or float.
# To get around this, we can convert the data type to a string.
for_example = 23
lets_combine = "This number is: "
these_together = lets_combine + str(for_example)
print(these_together)

# Plus equals
# This can be used as a shorthand to update variables