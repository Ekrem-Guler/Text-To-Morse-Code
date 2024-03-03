# All letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Morse codes twice because there are two type of letters
morse_letters = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---"
                 ".--.", "--.-", ".-.", "...", "- ", "..-", "...-", ".--", "-..-", "-.--", "--..",
                 ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-."
                 "---", ".--.", "--.-", ".-.", "...", "- ", "..-", "...-", ".--", "-..-", "-.--", "--.."]


# Create a list for letter's morse meaning
to_morse = []

# A string for print out the list
morse_text = ''

# Get input
text = input("Enter your text please: ")

# Get morse codes of letters
for i in text:
    place_in_letter = letters.index(i)
    to_morse.append(morse_letters[place_in_letter])

# Make it a sentence
for a in to_morse:
    morse_text += f"{a} "


print(morse_text)
