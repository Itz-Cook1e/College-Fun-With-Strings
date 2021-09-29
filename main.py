# Assignment:
# Write a program that prompts me to enter a string. (I will use something like "The quick brown fox jumps over the lazy dog"). Nobody really enjoys string manipulation, and if you search for ways to do this, you will find all kinds of shortcuts. 
# I'm asking that you not do that right now, because in every single job I've had, sooner or later I had to do some ugly string processing that had no shortcuts. It's good to know.
# Use only the following functions and methods: input, output, conditionals, and looping you have previously learned, plus the len function and the upper, lower, find, and slice methods.
# Take that string and print it out, using upper case for all vowels, and lower case for everything else ("thE qUIck brOwn...")
# Print out all of the 3-letter words (the, fox, the, dog)
# Note from ItzCook1e (me): Line 6 (Print out all of the 3-letter words) ended up contridicting their example program. I ended up doing their example.

# Make a function
def cappitalize(string1):
    cappitalized_end = ""
    for letter in string1:
        # See if letter is vowel
        if letter not in 'aeiouAEIOU':
            # Dont cappitalize if not vowel
            cappitalized_end = cappitalized_end + letter.lower()
        else:
            # Cappitalize if vowel
            cappitalized_end = cappitalized_end + letter.upper()
    return cappitalized_end

# Get user input
inputted_string = input('Please input a string: ')
# Use function on user input
end_result_string = cappitalize(inputted_string)
# Formatting and printing end result
print('New string:')
print(end_result_string)
print()

# Calculate length and split user input
length = [len(x) for x in inputted_string.split()]

# Make list of wordss from user input
words = [x for x in inputted_string.split()]
print('Words and their lengths:')
for word in words:
  # Print words and their lengths on different lines
  print(f'{word} {str(len(word))}')
  
# Comment with name, date, and assignment name redacted
