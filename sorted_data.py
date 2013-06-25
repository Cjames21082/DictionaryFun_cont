# Open file scores.txt
file_text = open("scores.txt")

# Read file line-by-line
file_lines = file_text.readlines()

# Close the file
file_text.close()

# Create dictionary key-value pair from each line-by-line
restaurant_ratings = {}

for line in file_lines:
	entry = line.strip('\n').split(":")
	restaurant_ratings[entry[0]] = entry[1]

# Sort dictionary by key, alphabetically and print ratings in alphabetical order
for key, value in sorted(restaurant_ratings.iteritems()):
	print "%s is rated at %s." % (key, value)