import time
Intro = True
Escape = False
Rescued = False
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
        print("Andrea spends most of her time upgrading the space she lives in. But as time went on, things got dull.")
        time.sleep(6)
        print("Andrea now memorizes the dragons flying pattern and started to talk to the dog just to kill time. This even got to the point where she thought that she started to hear voices.")
        time.sleep(10)
        print("And they’re coming closer??  Andrea turns around to see a group of people walking through the gate of the great wall she built")
        time.sleep(8)
        print("Of course she’s taken aback. Are they here for her? Did she do something to upset Fate? ")
        time.sleep(5)
        print("The group is approaching her and she’s frozen in anxiety. What does she do?? ")
        time.sleep(4)
        print("When the group notices her, they stop before approaching slowly")
        time.sleep(4)
        print("They introduce themselves as Rey, Atlas, Priss and Luna. That’s when Andrea notices someone familiar in the group. ")
        time.sleep(7)
        print("It's Cosmos. Her old friend")
        Squad = input("Are you open to meet the others?")
        if Squad == "No" or Squad == "no":
            print('Andrea get confrontational. “Cosmos?! Who in the world are you with? How can you know they’re trustworthy??”')
            time.sleep(6)
            print("Cosmos tries to calm her down, but to no avail. Isolation made Andrea really paranoid")
            time.sleep(5)
            print('She keeps moving backwards while Cosmos tries to move towards her. ')
            time.sleep(4)
            print("When Cosmos plays into their childhood together, Andrea kind of opens up")
            time.sleep(5)
            print("“I know this is your home, but I can feel this place isn’t save at the moment. Please move with me to a saver place.” ")
            time.sleep(6)
            print("Cosmos offers their hand. Andrea hesitantly takes it.")
            time.sleep(4)
            print("Even if Cosmos left her at one moment, they’re back. They’ll protect her right? ")
            time.sleep(4)
            print("Meanwhile the others destroyed everything that looks suspicious and/or dangerous. One action opened the portal and the group left the End")
            time.sleep(6)
            print("Andrea stayed hesitant even after Cosmos assured her she’s save now. She ended up making a place around Cosmos’ where she stayed from that moment on.")

        if Squad == "Yes" or Squad == 'yes':
            Rescued = True
            Escape = True
            print('Andrea get confrontational. “Cosmos?! Who in the world are you with? How can you know they’re trustworthy??”')
            time.sleep(6) 
            print("Cosmos slowly walks up to her and tries to assure her.")
            time.sleep(4)
            print("These are their friends and they helped them find a way back to the End. The rest greets her. Andrea let’s her guard down.  ")
            time.sleep(6)
            print("Cosmos explains: . “I know this is your home, but I can feel this place isn’t save at the moment. Please move with me to a safer place. The Overworld is beautiful.” ")
            time.sleep(10)
            print("Andrea takes Cosmos’ hand. Everyone helps destroyed any leads that Fate has to Andrea. This opens the portal. ")
            
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
    print("With that help, she can get out! Right? ")
    time.sleep(4)
    print("How will you try to escape?")
    Plan = input("A. Plan your escape or B. Leave the moment you get the chance.")
    if Plan == 'a' or Plan == 'A':
        Escape = True
        print('She just needs a plan so Fate doesn’t know she’s gone. While being somewhere else, she’ll need to wear a disguise.')
        time.sleep(5)
        print("She also can’t be away for too long each time. That should be do-able.")
        time.sleep(3)
        print("Andrea spent the next time making the things she’ll need to stay under the radar. Then she sneaks around the End to find a naturally spawning portal to the Overworld")
        time.sleep(6)
        print(' A few attempts later, she finds a way out. But this isn’t a portal to the Overworld, but one to the Nether.')
        time.sleep(5)
        print("Luckily for her, there a few people nearby. A man with long dark hair, one purple eye & one brown one and someone with dark green eyes, purple hair that falls on their shoulders and a dark birthmark across their left eye and forehead. ")
        time.sleep(10)
        print("She explains the situation: Being from the End and wanting to go to the Overworld.")
        time.sleep(4)
        print("The pair nods and say they’re from the Overworld and they can take her there. Andrea agrees and follows the two to the correct portal.")
        time.sleep(5)
    elif Plan == 'B' or Plan == 'b':
        Escape = True
        print("Right! She can do this!!")
        time.sleep(2)
        print("Andrea grabs some important stuff and goes to the outer islands to find a way out. It’s now or never!")
        time.sleep(4)
        print("She runs around for a bit before finding a portal. Without hesitation, she jumps in. ")
        time.sleep(4)
        print("She lands near an announcement board. It took her a moment before her eyes got used to the brightness of the sun.")
        time.sleep(5)
        print("She quickly looks around before standing up. “Wow. This place looks so green.” She thinks by herself. ")
        time.sleep(5)
        print("Her eyes land on a house with a moss roof. Curiosity takes over and she heads over.")
        time.sleep(4)
        print("*knock knock* ")
        time.sleep(2)
        print("A person with shoulder-length purple hair, dark green eyes and a dark birthmark that stretches across their face, opens the door. ")
        time.sleep(5)
        print('They seem surprised to see Andrea at the door. “We haven’t met before.” They remark. ')
        time.sleep(4)
        print("Andrea just slowly nods before explaining she escaped from the End. They listen closely. ")
        time.sleep(4)
        print('When Andrea’s done explaining, the person nods understandably and introduces themselves as Rey. They even offer Andrea some space in their house.')
        time.sleep(8)
        House = input("Do you accept?")
        if House == "Yes" or House == "yes":
            print("Adrea accepts the space and together with Rey they try to figure out who sleeps where.")
            time.sleep(4)
            print("Andrea can't believe she's out!")

if Escape == True or Rescued == True:
    print(" ")
    print("How should Andrea live in the Overworld?")
    Live = input("A. Live freely. She escaped! or B. Still be cautious")
if Live == 'A' or Live == 'a':
    print("Now that Andrea is out of the End, she feels free!")
    time.sleep(3)
    print('Fate thinks she’s just stuck in the End! What can go wrong? ')
    time.sleep(3)
    print("The Overworld is a new place to explore. Andrea can’t stop feeling excited")
    time.sleep(4)
    print('While the sun kinda hurts her eyes, it doesn’t stop her.')
    time.sleep(3)
    if Rescued != True:
        print("She hears her old friend Cosmos lives nearby, she meets new people like Priss, Atlas and Luna. ")
        time.sleep(4)

    else:
        print("The builder in her immediately starts to work on her own place and everything seems well! ")
        time.sleep(8)
        print("But good things never lasts forever.")
        time.sleep(5)
        print(' ')
        print(' ')
        print(' ')
        print("Rey came running to Andrea, warning her")
        time.sleep(3)
        print("They tell her they saw Fate and turns out: he has been following Rey for a little bit now. ")
        time.sleep(5)
        print("That is when Fate appears behind Andrea and Rey freezes.")
        time.sleep(3)
        print("He leaps towards Andrea and takes hold of her. Rey tries to stop him, but gets kicked away before Fate teleports away with Andrea. ")
        time.sleep(5)
        print(".....")
        time.sleep(3)
        print("Fate found you. Now there is a new cell under the End island which now belongs to you.")

if Live == 'B' or Live == "b":
    print("While she’s technically “save” with not being in the End anymore, Fate could be anywhere. ")
    time.sleep(5)
    print("Andrea doesn’t want to know what would happen if Fate found out she’s gone")
    time.sleep(5)
    print("So while she will explore to her hearts content and meet as many new people as she can, she must keep an eye out for anything suspicious. ")
    time.sleep(10)
    print("So live moves on. And Andrea is really happy in her new home.")
    time.sleep(5)
    print(". The people in the village are so sweet and always help whenever she needs it")
    time.sleep(7)
    print("Andrea can imagine anything else.")
    time.sleep(4)
    Fight = input("Are you A. content with this ending or B. do you want to do something against Fate?")
    if Fight == 'A' or 'a':
        print('And while Fate isn’t technically gone, this is Andrea’s dream world.')
                
    if Fight == 'B' or 'b':
        print("But Fate never left the back of her head. It bothered her. Her new friends also showed concern for her. ")
        time.sleep(6)
        print("Rey asked about the End and if anyone knew if there is another portal towards the realm. Logically there should be one. ")
        time.sleep(7)
        print("So a group formed of Rey, Andrea, Atlas, Luna, Priss and Cosmos. The spent ages gathering information about the portal, where it could be and how to open it. ")
        time.sleep(10)
        print("The eyes of Ender are a huge part and after some trial and error, they found the way in. ")
        time.sleep(5)
        if Rescued != True:
            print("They broke every way Fate could blackmail Andrea.")
            print("They found the prisoner and broke them free")
            time.sleep(5)
            print("This opened the portal. With Fate not being able to use Andrea anymore, they build their own spots wherever they wanted.")
        else:
            print("They found the prisoner underneath the End Island and freed them.")
            time.sleep(4)
            print("This only impowered the portal to stay open. Connecting the Overworld and the End forever.")
            time.sleep(5)
            print("With Fate not being able to use Andrea anymore, they build their own spots wherever they wanted.")
    
            


