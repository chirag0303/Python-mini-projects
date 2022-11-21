# Importing random module
import random

# Creating List of phrases that will form a story.

starter = ['A long time ago','About 100 years ago','In the 20 BC','Once upon a time','Many decades ago']

person1 = [' there was a person',' there lived a king',' there was a man',' there lived a farmer',
           ' there lived a worker']

name = ['Hector', 'Alexander','Ashoka', 'Chandragupta', 'Arjun']

time = ['One Sunday','One day', 'One full-moon night','One evening','One after-noon']

plot = ['he was passing by','he was going for a picnic to ','he was roaming around','he was exploring']

place = [' the village area',' the mountains', ' the garden', ' the jungle']

person2 = [' he saw a man', ' he saw a woman']

age = [' who seemed to be in late 20s', ' who seemed very old and feeble',' who seemed very worried']

work = [' searching something and suddenly vanished in the thin air.',
        ' digging a well on roadside ,when asked what are you doing got suddenly disappeared .',
        ' crying because of hunger so he gave him some food.',
        ' finding their child so he came forward to gave a helping hand.']

# Choosing a part from each list using random module to complete a story.

print(random.choice(starter)+random.choice(person1)," named ",random.choice(name),".",
      random.choice(time),"when",random.choice(plot) +random.choice(place)+random.choice(person2)+
	    random.choice(age)+random.choice(work))
