from langdetect import * # Used to detect languages ; Returns ISO Code
import pycountry # Used to convert ISO Code into language name


# Read .txt file
f = open("C:\\Users\\c261941\\Downloads\\Sample_EN.txt", "r")
text = (f.read())

# Detect text language
lang_code = detect(text)
# Below is to hardcode some ISO Code if needed for testing purposes
# lang_code = "fr"

# Convert ISO onto language name
try:
    lang_name = pycountry.languages.get(alpha_2=lang_code)
    language = lang_name.name
except AttributeError:
    language = None

print(language)

# Take actions based on language
if language == None:
    print("None")
else:
    print("Move email to sub-folder")


# Notes:
# If the text includes multiple languages,
# the one with the most characters seems to be the one recognised.
