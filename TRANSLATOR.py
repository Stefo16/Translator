# Every letter that is a vowel(a,e,i,o,u) will change to g or G

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"

        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a word or a phrase: ")))
