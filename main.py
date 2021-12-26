import random

def main():
    try:
        syllables = open('syllables.txt').readlines()
        suffixes = open('suffixes.txt').readlines()
        additions = open('additions.txt').readlines()
        temp = []
        for l in range(len(syllables)):
            temp.append(syllables[l].replace('\n', '').lower())
        syllables = temp.copy()
        temp.clear()

        for l in range(len(suffixes)):
            temp.append(suffixes[l].replace('\n', ''))
        suffixes = temp.copy()
        temp.clear()

        for l in range(len(additions)):
            temp.append(additions[l].replace('\n', ''))
        additions = temp.copy()
        

    except:
      print('Error reading the name files')
    print('Press enter to generate a name, or write exit and then press enter to quit: ')
    while(True):
        if input().lower() == "exit":
            exit()
        name(syllables, suffixes, additions)

def name(syllables, suffixes, additions):
    firstName = ''
    lastName = ''
    syls = random.randint(1,3)
    for i in range(syls):
        firstName += syllables[random.randint(0, len(syllables)-1)]
    firstName = firstName.capitalize()

    for i in range(syls):
        lastName += syllables[random.randint(0, len(syllables)-1)]
    
    lastName = lastName.capitalize()

    r = random.randint(0, 100)

    if r < 30:
        suffix = suffixes[random.randint(0, len(suffixes)-1)]
        lastName += suffix
    elif r < 40:
        lastName = additions[random.randint(0, len(additions)-1)]

    print(firstName + " " + lastName)

if __name__ == "__main__":
    main()