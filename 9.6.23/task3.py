vowels = "aeiou"
while True:
    noOfNumber = 0
    noOfLowercase = 0
    noOfUppercase = 0
    noOfVowel = 0
    noOfConsonant = 0
    inputString = input("Enter your string: ")
    for letter in inputString:
      
      try:
        if int(letter):
          noOfNumber += 1
          
      except ValueError:
          if letter.lower() in vowels:
            noOfVowel += 1
          else:
            noOfConsonant += 1
          if letter.lower() == letter:
            noOfLowercase += 1
          else:
            noOfUppercase += 1
    
    print(f"""\n\nYour string {inputString} has:
{noOfNumber} number(s)
{noOfLowercase} lowercase letter(s)
{noOfUppercase} uppercase letter(s)
{noOfVowel} vowel(s)
{noOfConsonant} consonant(s)\n\n""")
