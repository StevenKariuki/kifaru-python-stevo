#list ,conditions, loops
# GAME OF CARDS
#Cards =spade flower,diamond,heart

#1.create a list and store cards
#2.shuffle
#show the cards at index zero
#request for the next card to be first on the list.
#reshuffle
#we compare the cards
#if the cards matches u win and earn points
#if the cards don't match you loss and earn zero points

cards =["spades", "flower", "diamond", "heart"]
points = 0

import random
random.shuffle(cards)
print("The current card is", cards[0] )


requestedCard = str(input("Now guess the next card"))
print("=======RESHUFLING======")
random.shuffle(cards)
if requestedCard == cards[0]:
    print("=======CONGRATSYOU WON=====")
    print("The cards is : ",cards[0])
    points = points + 5
    print(f'Ypu earned {points} points')

else:
    print("=====LOST====")
    print("The cards was to be :", cards[0])    
    print("=========NEXT TURN===========")
    print("=============================")   

   


print("======GAME OVER=====")
print("he card was to be :", points) 




