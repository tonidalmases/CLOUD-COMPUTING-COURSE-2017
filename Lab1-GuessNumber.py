
# coding: utf-8

# In[2]:

import random
randomNumber = random.randrange(0,20)
print("Random between 0 and 20")
guessed=False
while guessed==False:
    userNumber=int(input("Introduce: "))
    if userNumber==randomNumber:
        guessed=True
        print("Excellent!")
    elif userNumber>randomNumber:
        print("A bit lower")
    elif userNumber<randomNumber:
        print("A bit higher")
print("You can!")


# In[ ]:



