print "Hello all! Talk to ancient Pigs with this Pig Latin thingymajig. Now you can easily through this simple translator without having to go through the masses of work yourself... \n" 
pyg = 'ay'

original = raw_input('Enter a word:  ')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print new_word
else:
    print "Dude?! What you be thinkin'? This ain't no word"
