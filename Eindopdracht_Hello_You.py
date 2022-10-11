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
time.sleep(8)

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

print("Until one day")
if reaction > 0:
    print("Something happened to cheer Andrea up a tiny bit.")
    time.sleep(2)
    print("While she’d gotten a dog from who knows where, now another being was standing before her. ")
    time.sleep(4)
    print("This being introduced herself as Vereni, Goddess of Time. Andrea was confused at first and asked Vereni about what had happened. ")
    time.sleep(4)
    print("She explained that Fate had gone rogue and had overthrown everyone. Now they controlled everything and if someone disobeyed, consequences would happen. ")
    time.sleep(6)
    print("Andrea was a bit confused but didn’t ask any questions. Vereni asked if Andrea was okay and she just simply nodded. “If there is anything I can help with, let me know.” Vereni said.")
    time.sleep(8)
    help = input("Will you trust Vereni?")
    if help == 'Yes' or help == "yes":
        trust = True
        print("“I need your help right now.” Andrea softly answers. She then explains how she’s stuck in the End after Fates assignment. ")
        time.sleep(4)
        print('Vereni listens closely and to lift Andrea’s spirits, she gives her a spore blossom.')
    elif help == 'No' or help == 'no':
        trust = False
        print('Andrea stays quiet while Vereni disappears. ')
        time.sleep(2)
        print(' ')
        print("Andrea doesn’t really know what to do. ")
        time.sleep(2)
        print("How can she trust Vereni if she can’t trust Fate. They’re both Deities and if Vereni is telling the truth, then how can she be sure it isn’t a game to trick her?? ")
        time.sleep(5)
        print("Time slowly moves on. One month turns into two, turns into three. Nothing changes, nothing happens. ")
        time.sleep(4)
        print("Andrea is getting frustrated by the situation. While she has seen Vereni a couple of times after the first visit, she still doesn’t trust her")
        time.sleep(6)
        print("And Fate never showed up again either. What is she even supposed to be guarding?? And what is the use if there’s no one nearby?")
        time.sleep(6)
elif reaction < 0:
    print("Finally her prayers were heard. While she did get a dog from an unknown source, none of the other Deities had shown anything. ")
    time.sleep(4)
    print("Until Vereni, Goddess of Time chose to help Andrea. She explained how Fate had gone rogue and had made changes")
    time.sleep(4)
    print("Everyone has to obey them or else consequences would ensue.")
    time.sleep(2)
    print('Andrea now finally understood the situation. She had been chosen by Fate to protect something that was being held under the End Island')
    time.sleep(4)
    print('If she’d dare to disobey, then what would happen to her?')
    time.sleep(2)
    print("Vereni showed her concern about her follower and showed Andrea a way to another part of the End. There was a small building. ")
    time.sleep(4)
    print('Vereni explained this was supposed to be a safe space for Andrea. Andrea appreciated the gesture.')
    time.sleep(3)
    print('Vereni promised to check in more and gave Andrea a spore blossom for her troubles. ')

if reaction < 0 or trust == True:
    print('Over the coming time Andrea became more confident in herself. She knew there was a Goddess standing behind her who could help. ')
    time.sleep(6)
