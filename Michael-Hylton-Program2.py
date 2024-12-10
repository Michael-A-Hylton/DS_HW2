"""
File: YourFirstName-YourLastName-Program2.py
Name: TODO
Course: DSA 230/CIS 492/CIS 593 Intro to Data Science I
Date: Fall 2024

"""
import random


def rollDice() -> list:
    """Simulates a dice poker roll by returning a list of 5 ints, where each is randomly uniformly chosen from [1,6]"""
    dice = []
    for dieNumber in range(5):
        thisDie = random.randint(1, 6)
        dice.append(thisDie)
    return dice


"""
Question #3: You have a function above, called `rollDice()`, which returns a list of 5 random ints between 
1 and 6, inclusive. Write a program with the following:

HINT: I would first make a function `countFrequencies(dice: list) -> dict` that counts the frequencies of each value 
in the roll. This will come in handy for a lot of these other functions. I would also recommend going back to the last 
part of lab2 and copying some code to make this function.
"""

def countFreq(dice:list) -> dict: 
    
    freq={"one":0,"two":0,"three":0,"four":0,"five":0,"six":0}
    i=0
    while i<(len(dice)):
        if dice[i]==1:
            freq["one"]+=1
        elif dice[i]==2:
            freq["two"]+=1
        elif dice[i]==3:
            freq["three"]+=1
        elif dice[i]==4:
            freq["four"]+=1
        elif dice[i]==5:
            freq["five"]+=1
        elif dice[i]==6:
            freq["six"]+=1
        i+=1
    
    return freq
            
            


"""

3a) A function `isFiveKind(dice: list) -> bool` that returns `True` if all five dice are the same value and
`False` otherwise.
"""

def isFiveKind(dice:list) ->bool:
    freq=countFreq(dice)
    
    for items in freq:
        
        if freq[items]==5:
            return True
        

    return False


"""
3b) A function `isFourKind(dice: list) -> bool` that returns `True` if four dice are the same value and 
`False` otherwise.
"""

def isFourKind(dice:list) ->bool:
    freq=countFreq(dice)
    
    for items in freq:
        
        if freq[items]==4:
            return True
        

    return False


"""
3c) A function `isFullHouse(dice: list) -> bool` that returns `True` if three dice are the same value AND two dice 
are the same value and `False` otherwise.
"""

def isFullHouse(dice:list) ->bool:

    freq=countFreq(dice)
    
    for items in freq:
        
        if freq[items]==3:
            for items in freq:
                if freq[items]==2:
                    return True
        

    return False

"""
3d) A function `isStraight(dice: list) -> bool` that returns `True` if all five dice can be ordered such that 
they are consecutively ascending and `False` otherwise.
"""

def isStraight(dice:list) ->bool:
    freq=countFreq(dice)
    if freq["one"]==1 and freq["two"]==1 and freq["three"]==1 and freq["four"]==1 and freq["five"]==1:
        return True
    if freq["two"]==1 and freq["three"]==1 and freq["four"]==1 and freq["five"]==1 and freq["six"]==1:
        return True
    else:
        return False


"""
3e) A function `isThreeKind(dice: list) -> bool` that returns `True` if three dice are the same value and 
`False` otherwise.
"""

def isThreeKind(dice:list) ->bool:
    freq=countFreq(dice)
    
    for items in freq:
        
        if freq[items]==3:
            return True
        

    return False



"""
3f) A function `isTwoPair(dice: list) -> bool` that returns `True` if there are two values that each appear twice and 
`False` otherwise.
"""

def isTwoPair(dice:list) ->bool:
    freq=countFreq(dice)
    success=0
    for items in freq:
        
        if freq[items]==2:
            success+=1

    if success>=2:
        return True
    else:
        return False



"""
3g) A function `isPair(dice: list) -> bool` that returns `True` if two dice are the same value and
`False` otherwise.
"""

def isPair(dice:list) ->bool:
    freq=countFreq(dice)
    
    for items in freq:
        
        if freq[items]==2:
            return True
        

    return False


"""
3h) A function `playDicePoker(numRolls: int) -> dict` that rolls the dice `numRolls` amount of times and 
computes the number of `fiveKind`, `fourKind`, `fullHouse`, `straight`, `threeKind`, `twoPair`, `pair` and `bust` 
(i.e. none of the above), earned in that number of rolls. Return a dictionary with keys for the type of roll and 
values for that roll's count (i.e. after zero rolls, the dictionary is `handsWon = {"fiveKind" : 0, "fourKind" : 0, 
"fullHouse" : 0, "straight" : 0, "threeKind" : 0, "twoPair" : 0, "pair" : 0, "bust" : 0}`). NOTE: Each roll should 
only be counted once. That is to say a `fullHouse` is a just a `fullHouse`, and not also a `threeKind` and `pair`. 
This means the sum of all entries in the dictionary should total to `numRolls`.
"""

def playDicePoker(numRolls: int) -> dict:
    handsWon= {"numOfCurrRolls":0, "fiveOfKinds":0, "fourOfKinds":0, "fullHouses":0, "straights":0, "threeOfKinds":0,"twoPairs":0, "pairs":0, "busts":0}
    
    while int(handsWon["numOfCurrRolls"])<=int(numRolls):
        dice=rollDice()
        if isFiveKind(dice):
            handsWon["fiveOfKinds"]+=1
        elif isFourKind(dice):
            handsWon["fourOfKinds"]+=1
        elif isFullHouse(dice):
            handsWon["fullHouses"]+=1
        elif isStraight(dice):
            handsWon["straights"]+=1
        elif isThreeKind(dice):
            handsWon["threeOfKinds"]+=1
        elif isTwoPair(dice):
            handsWon["twoPairs"]+=1
        elif isPair(dice):
            handsWon["pairs"]+=1
        else:
            handsWon["busts"]+=1

        handsWon["numOfCurrRolls"]+=1
    return handsWon

"""
3i) A function `printResults(numRolls: int, handsWon: dict) -> None` that prints the total number of rolls, the 
total number of each type of roll, and the percentage observed of each type of roll.

HINT: If you enter a very large `numRolls` into the console (like >10,000), then, by the law of large numbers,
you should see probabilities that very closely match the probability distribution published on: 
https://en.wikipedia.org/wiki/Poker_dice.
"""

def printResults(numRolls: int, handsWon: dict) -> None:
    print("Number of Rolls:")
    print(numRolls)
    print("Total results: ")
    print(handsWon)
    numRolls=int(numRolls)
    stat={"statFiveoK":0,"statFouroK":0,"statFH":0,"statStra":0,"statToK":0,"statTP":0,"statPairs":0,"statBust":0,}
    stat["statFiveoK"]=handsWon["fiveOfKinds"]/numRolls
    stat["statFouroK"]=handsWon["fourOfKinds"]/numRolls
    stat["statFH"]=handsWon["fullHouses"]/numRolls
    stat["statStra"]=handsWon["straights"]/numRolls
    stat["statToK"]=handsWon["threeOfKinds"]/numRolls
    stat["statTP"]=handsWon["twoPairs"]/numRolls
    stat["statPairs"]=handsWon["pairs"]/numRolls
    stat["statBust"]=handsWon["busts"]/numRolls
    print("Total stats: " )
    print(stat)
"""
3j) Finally, write a script/main function that prompts the user how many times they'd like to play dice poker, passes
the user's input into the `playDicePoker(numRolls: int) -> dict` function, and finally passes the returned dictionary
into `printResults(numRolls: int, handsWon: dict) -> None`.
"""

    

def main():
    numRolls=input("How many times would you like to play dice poker: ")
    results=playDicePoker(numRolls)
    printResults(numRolls, results)
    testRoll = rollDice()
    print(testRoll)


main()
