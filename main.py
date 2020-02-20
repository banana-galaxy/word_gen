import string, sys, random

#print(f"list length: {len(sys.argv)}")
if len(sys.argv) > 1:
    try:
        length = int(sys.argv[1])
    except ValueError:
        print("Please enter a number")
        quit()
else:
    print("Please add a word length as an argument")
    quit()

word = ""
cons = random.randint(0,1)
i = 0

while i < length:
    #print(i)
    if not cons:
        letter = random.choice(list("aeiou"))
        word += letter
        cons = 1
        i += 1
    else:
        count = 0
        amount = random.randint(1, 2)
        while count < amount and i < length:
            #print(x)
            vowel = True
            while vowel:
                letter = random.choice(list(string.ascii_lowercase))
                if not letter in list("aeiou"):
                    vowel = False
            word += letter
            i += 1
            count += 1
        cons = 0

print(word)