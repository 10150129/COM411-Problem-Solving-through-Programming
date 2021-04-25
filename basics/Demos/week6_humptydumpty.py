#text analysis

song = '''
Humpty Dumpty sat on the wall
Humpty Dumpty had a great, great fall and
All the king's horses and all the king's men
Couldn't put Humpty together again
Humpty Dumpty and Betty Louise
Stole a Sony and some Camembert cheese
And she said "Humpty baby
Take me to the river
Cause I like the way it runs
Take me to the river
You know I like the way it runs"
He said "ah, ooh, everything's going my way"
He said "maybe it's my lucky day"
I said "anything you want I can give"
She said "I want to take your picture, mm, just for me"
He said "anything"
She said "up there baby get on the wall babe"
Humpty Dumpty sat on the wall…
'''

#print(song)
#do some formatting to the song
#the word 'take', some have upper case other lower case, I want to make them all lower cases letters
lista = song.lower().replace("\"", "").replace("\'", "").replace(",", "").split()


print(set(lista))
#this will give you nice clean words with no comas 

word_dict = {}

for item in lista:
  word_dict[item] = word_dict.get(item, 0) + 1

print(word_dict)

