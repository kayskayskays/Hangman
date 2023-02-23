## Hangman Drawing Function ##
# i is an int from 0 to 10 where 10 is the complete hangman
def drawHangman(i):
    match i:
        case 0:
            return '          \n          \n          \n          \n          \n          \n=========='
        case 1:
            return '          \n  |       \n  |       \n  |       \n  |       \n  |       \n=========='
        case 2:
            return '  +---+   \n  |       \n  |       \n  |       \n  |       \n  |       \n=========='
        case 3:
            return '  +---+   \n  |/      \n  |       \n  |       \n  |       \n  |       \n=========='
        case 4:
            return '  +---+   \n  |/  |   \n  |       \n  |       \n  |       \n  |       \n=========='
        case 5:
            return '  +---+   \n  |/  |   \n  |   O   \n  |       \n  |       \n  |       \n=========='
        case 6:
            return '  +---+   \n  |/  |   \n  |   O   \n  |   |   \n  |       \n  |       \n=========='
        case 7:
            return '  +---+   \n  |/  |   \n  |   O   \n  |   |   \n  |  /    \n  |       \n=========='
        case 8:
            return '  +---+   \n  |/  |   \n  |   O   \n  |   |   \n  |  / \\  \n  |       \n=========='
        case 9:
            return '  +---+   \n  |/  |   \n  |   O   \n  |  /|   \n  |  / \\  \n  |       \n=========='
        case 10:
            return '  +---+   \n  |/  |   \n  |   O   \n  |  /|\\  \n  |  / \\  \n  |       \n=========='
        case _:
            return 'somebody fricked up while programming\n\n\n\n\n\n'

## Function to generate the entire message to display ##
def generateDisplay(word, guesses):
    # Sort correct and wrong guesses
    correct = []
    wrong = []
    for g in guesses:
        if g in word:
            correct.append(g)
        else:
            wrong.append(g)
    if len(wrong)>10:
        try:
            deathscreen = '  +---+\n  |/  |\n  |   O\n  |  /|\\\n  |  /'+chr(230)+'\\\n  |   '+chr(182)+'\n=========='
        except:
            deathscreen = '  +---+\n  |/  |\n  |   O\n  |  /|\\\n  |  /w\\\n  |   |\n=========='
        return deathscreen
    # Generate the guess line
    gLine = ''
    for w in word:
        if w in correct or not w.isalpha():
            gLine+=w+' '
        else:
            gLine+='_ '
    # Generate wrong line
    wLine = ''
    for w in sorted(wrong):
        wLine += w + ' '
    return drawHangman(len(wrong))+'\n'+gLine+'\n'+wLine
        

    
## TEST CODE ##
test  = ['a','b','d','h','e','p','w','l','m','n','o','q','r','s','t','w']
for i in range(0,len(test)+1):
    print(generateDisplay('help',test[0:i]))
    print("\n\n")