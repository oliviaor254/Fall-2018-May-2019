import numpy
word = ''
vowels = ['a','A','E','e','I','i','o','O','u','U','y','Y']      #list of vowels
while word != 'STOP':
    word = input('Enter a word to convert to Pig Latin (STOP to cancel): ')
    if word == 'STOP':
        break
    if word[0] in vowels:   #Checks if first letter is in vowels
        string = word + 'yay'

    else:
        ending = word[0]+'ay'
        string = word[1:]+ending
    print(string)

#Challenge Attempt
Punctual = ['.',',','!','?',';',':']
sentence = ''
while sentence != 'STOP':
    more_words = []
    another = ''
    sentence = input('Enter a sentence to convert to Pig Latin (single word STOP to cancel): ')
    more_words = list(sentence.split(' '))
    for a in range(len(more_words)):
        if more_words[a][-1] in Punctual:
            another = more_words[a][-1]
            more_words[a] = more_words[a][0:-1]
        if more_words[a][0] in vowels:
            more_words[a] = more_words[a]+'yay'+another
        else:
            ends = more_words[a][0] + 'ay'+another
            stripe = more_words[a][1:] + ends
            more_words[a] = stripe
    if sentence == 'STOP':
        break
    print(' '.join(more_words))