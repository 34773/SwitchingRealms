import time
Intro = True

while Intro:
    print("Welcome to Switching Realms.")
    time.sleep(2)
    print("You'll be playing as Andrea, a citizen from the End.")
    time.sleep(2)
    print("Your choices will have consequences on her life.")
    time.sleep(2)
    Ready = input("Are you ready to begin? ")
    if Ready == "Yes" or Ready == "yes":
        print("Let's start")
        Intro = False
    elif Ready == "No" or Ready == "no":
        print("I assume you didn't understand what we're doing, so let me explain again.")
        time.sleep(2)
    else:
        print("I'm sorry. I didn't understand. So be sure, let me explain the game again.")
        time.sleep(2)

print("Andrea has been an End citizen her entire life. She lived with her friend and family around the main End Island.")
time.sleep(4)
print("One day a lot of them left through the gateways and main portal, leaving her the only one left on the island.")
time.sleep(4)
print("She didn’t mind at first, until she was locked there. One of the Deities of her world stood before her, closing the portal. ")
time.sleep(4)
print("When they noticed her, they asked a huge favor of her. To keep others away from the Island and keep an eye out on the prison that laid underneath. Andrea reluctantly accepts, now being called The Warden of the End.")
time.sleep(6)

choice1 = True
while choice1:
    print("Andrea doesn’t know how to feel about her new life. Being alone in the End.")
    print('How does she react?')
    Mood = input('A. "Mope around" or B. "Believe there is still hope" ? ')
    if Mood == 'A' or Mood == 'a':
        print("Andrea doesn’t really know what to do with herself. ")
        time.sleep(2)
        print("She walks around and checks the ends of the island. Nothing really is going on. ")
        time.sleep(3)
        print("She has her essentials, like a house and a farm. There is even a temple so she can call on the other Deities if needed. She just feels hopeless.")
        time.sleep(6)
        reaction = 1
        choice1 = False
    elif Mood == 'b' or Mood == 'B':
        print("Even with the circumstances, Andrea doesn’t give up. ")
        time.sleep(2)
        print("She starts to build up the surroundings to her liking.")
        time.sleep(2)
        print(". She builds walls for protection, updates the farms and builds extra things, like an armory. She even tries to call the other Deities. ")
        time.sleep(4)
        print("But nothing really happens during the first month")
        reaction = -1
        choice1 = False
    else:
        print("That wasn't a valid answer. Please try again.")
        time.sleep(2)

