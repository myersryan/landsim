import random

numlist = []
handsize = 7
namelist = []
data = open("input.txt","r")
set= open("set.txt","r")
output = open("output.txt","a+")
cardlist = []
hand = []
setcount = 0
set1=[]
set2=[]
set3=[]
set4=[]
set5=[]
listofhands=[]

successcount=0

mull=0

with open('input.txt') as f:
    line_count = 0
    for line in f:
        line_count += 1

for i in range (0, line_count):
    line = data.readline()
    if len(line) > 1:
        num, name = line.split(" ", 1)
        name = name[:(len(name)-1)]
        namelist.append(name)
        numlist.append(num)
        for j in range (0, int(num)):
            cardlist.append(name)


with open('set.txt') as f:
    line_count = 0
    for line in f:
        line_count += 1

for i in range (0, line_count):
    line = set.readline()
    name = line[:(len(line)-1)]
    if (setcount == 1) and ("<" not in line):
        set1.append(name)
    if setcount == 2 and ("<" not in line):
        set2.append(name)
    if setcount == 3 and ("<" not in line):
        set3.append(name)
    if setcount == 4 and ("<" not in line):
        set4.append(name)
    if setcount == 5 and ("<" not in line):
        set5.append(name)
    if "<" in line:
        setcount = setcount + 1

card = [0,0,0,0,0,0,0]

for i in range (0,10000):
    ss1 = False
    ss2 = False
    ss3 = False
    ss4 = False
    hand = []
    landcount=0
    handsize = 7

    for i in range (0, handsize):
        card[i] = random.randint(1,60)


#determine if we have already drawn the same cards
    for i in range (0,handsize):
        for j in range (0,handsize):
            while (card[i] == card[j]) and (i!=j):
                card[i] = random.randint(1,60)

#convert the card to text and put it into our hand
    for i in range (0,handsize):
        hand.append(cardlist[card[i]])

#check set rules, checks for untapped green source
    for i in range (0,len(set1)):
        for j in range (0,len(hand)):
            if hand[j] == set1[i]:
                ss1=True

#checking to see if we have accel
    for i in range (0,len(set2)):
        for j in range (0,len(hand)):
            if hand[j] == set2[i]:
                #if our accel is mox diamond, check to see if we have a second land to pitch (any land)
                if hand[j] == "Mox Diamond":
                    for k in range (0,len(set4)):
                        for l in range (0,len(hand)):
                            if hand[l] == set4[k]:
                                landcount = landcount + 1
                    if landcount >1:
                        ss2=True
                else:
                    #if our accel is manabond or exploration, see if we have a second mana producing land for loam
                    for k in range (0,len(set5)):
                        for l in range (0,len(hand)):
                            if hand[l] == set5[k]:
                                landcount = landcount + 1
                    ss2=True

#checking to see if we have action
    for i in range (0,len(set3)):
        for j in range (0,len(hand)):
            if hand[j] == set3[i]:
                ss3=True

#ensure we have more then 1 land to play
    if landcount == 0:
        for i in range (0,len(set4)):
            for j in range (0,len(hand)):
                if hand[j] == set4[i]:
                    landcount=landcount+1
        if landcount > 1:
            ss4=True
    else: ss4=True

#if all sets are met success
    if (ss1 == True and ss2 == True and ss3 == True and ss4==True):
        successcount = successcount + 1
    else:
        ss1 = False
        ss2 = False
        ss3 = False
        ss4 = False
        hand = []
        landcount = 0
        handsize=6

        for i in range(0, handsize):
            card[i] = random.randint(1, 60)

        # determine if we have already drawn the same cards
        for i in range(0, handsize):
            for j in range(0, handsize):
                while (card[i] == card[j]) and (i != j):
                    card[i] = random.randint(1, 60)

        # convert the card to text and put it into our hand
        for i in range(0, handsize):
            hand.append(cardlist[card[i]])

        # check set rules, checks for untapped green source
        for i in range(0, len(set1)):
            for j in range(0, len(hand)):
                if hand[j] == set1[i]:
                    ss1 = True

        # checking to see if we have accel
        for i in range(0, len(set2)):
            for j in range(0, len(hand)):
                if hand[j] == set2[i]:
                    # if our accel is mox diamond, check to see if we have a second land to pitch (any land)
                    if hand[j] == "Mox Diamond":
                        for k in range(0, len(set4)):
                            for l in range(0, len(hand)):
                                if hand[l] == set4[k]:
                                    landcount = landcount + 1
                        if landcount > 1:
                            ss2 = True
                    else:
                        # if our accel is manabond or exploration, see if we have a second mana producing land for loam
                        for k in range(0, len(set5)):
                            for l in range(0, len(hand)):
                                if hand[l] == set5[k]:
                                    landcount = landcount + 1
                        ss2 = True

        # checking to see if we have action
        for i in range(0, len(set3)):
            for j in range(0, len(hand)):
                if hand[j] == set3[i]:
                    ss3 = True

        # ensure we have more then 1 land to play
        if landcount == 0:
            for i in range(0, len(set4)):
                for j in range(0, len(hand)):
                    if hand[j] == set4[i]:
                        landcount = landcount + 1
            if landcount > 1:
                ss4 = True
        else:
            ss4 = True
        if (ss1 == True and ss2 == True and ss3 == True and ss4 == True):
            successcount = successcount + 1
            mull=mull+1


print(successcount)
print(mull)


