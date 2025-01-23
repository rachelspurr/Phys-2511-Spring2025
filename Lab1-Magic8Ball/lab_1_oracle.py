# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 20:42:55 2025

@author: Rach
"""

import random
import time

while True:
    
    question = input("Ask The Unclear Oracle any yes or no question, if you dare: ")
    
    if question == "":
        print("Hasta la vista... baby.") # my dad thought it would be funny to add this
        time.sleep(2)
        print("I'll be back.")
        break
    
    # this is the part where i make it look like the oracle is searching for the answer
    print("Ahh... so you wish to know the answer to the question " + question)
    time.sleep(2)
    print("Please allow the oracle a moment to consult higher dimensional beings from the multiverse on possible likely outcomes to your query...")
    time.sleep(3)
    print("...")
    time.sleep(2)
    print("Interesting... Interesting!...")
    time.sleep(1)
    print("The Unclear Oracle says...")
    time.sleep(0.5)
    
    x = random.randint(1,20)
    if x==1:
        print("I'm 100% sure that there's a 50% chance the answer is yes.")
    elif x==2:
        print("I wanna say yes, but the voices in my head are screaming no.")
    elif x==3:
        print("Sources say only in your dreams, sucker!")
    elif x==4:
        print("The stars say yes, but only if the moon winks at you tonight.")
    elif x==5:
        print("That was the dumbest question ever and I refuse to answer that.")
    elif x==6:
        print("Yes, but it comes with a free side of existential dread.")
    elif x==7:
        print("Nope, but I admire your enthusiasm!")
    elif x==8:
        print("Absolutely yes! Unless you wanted the answer to be yes, then the answer is no. :)")
    elif x==9:
        print("The universe says no, but I say yes! Who will you trust?")
    elif x==10:
        print("Yes, but only if you promise not to tell my mother.")
    elif x==11:
        print("The answer is yes, but with an asterisk and fine print that I won't explain.")
    elif x==12:
        print("I'm leaning toward yes, but my crystal ball just fell asleep so honestly who knows.")
    elif x==13:
        print("The answer to this question is too complex for your feeble human mind to comprehend.")
    elif x==14:
        print("Yes, but it's a secret... shhhh!!")
    elif x==15:
        print("Drop and give me 20 and I might just tell you the answer you wanna hear!")
    elif x==16:
        print("No, but it looks like theres a coupon available for a half yes if you'd like to use it.")
    elif x==17:
        print("*whips out a magic 8-ball* Uhhh... *shakes* Reply hazy, try again!... Wait that's a stupid answer...")
    elif x==18:
        print("No because the answer took a wrong turn and got lost :(")
    elif x==19:
        print("No, but I hear the answer might change during a full moon.")
    elif x==20:
        print("Sure! But it'll cost you one imaginary gold coin.")