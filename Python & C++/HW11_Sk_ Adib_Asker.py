#Sk adib asker
#cs 100, section-103
# Trapdoors & Catapults. A digital version of Chutes & Ladders

import random

def getPlayerNames():
    ''' Prompt the two players for their names and return
        these two strings.'''
    print()
    player1 = input('Name of first player: ')
    player2 = input('Name of second player: ')

    return player1, player2

def getBoardInfo():
    ''' PROBLEM 1. FOLLOW THE EXAMPLE OF THE getPlayerNames() FUNCTION.
        WRITE CODE TO:        
        Prompt the user for three items: the number of spaces
        on the board, the number of trapdoors and the number of
        catapults. Return these three items as integers. You may
        assume that the user input is valid'''
    # PROBLEM 1 CODE HERE
    numSpaces = int(input("How many spaces on the board: "))
    numTraps = int(input("How many trapdoors on the board: "))
    numCatapults = int(input("How many catapults on the board: "))
    return numSpaces, numTraps, numCatapults

def boardSetup(boardSize, trapdoorNum, catapultNum):
    ''' Create and return two dictionaries. One dictionary should
        contain trapdoorNum space/destination pairs of trapdoors; the
        second should contain catapultNum space/destination pairs
        of catapults. All spaces should be greater than one and less
        than boardSize.'''
    trapdoors = {}
    catapults = {}

    # select trapdoorNum spaces at random to have trapdoors
    while len(trapdoors) < trapdoorNum:
        space = random.randint(2, boardSize-1)
        if space in trapdoors:
            continue

        # Select at random a destination space for the trapdoor.
        # The destination may be any value greater than or equal
        # to 1 and less than the current space        
        trapdoors[space] = random.randint(1, space-1)  

    # PROBLEM 2. FOLLOW THE PATTERN OF THE ABOVE LOOP. WRITE CODE TO:    
    # Select catapultNum spaces at random to have catapults. No space
    # may have both a trapdoor and a catapult. Neither the first nor
    # the last nor the next to last space may have a catapult.
    # PROBLEM 2 CODE HERE
    while len(catapults) < catapultNum:
        space = random.randint(2, boardSize-2)
        if space in catapults and space in trapdoors:
            continue

        # PROBLEM 3. FOLLOW THE PATTERN ABOVE. WRITE CODE TO:        
        # Select at random a destination space for the catapult. The
        # destination may be any space greater than the current space
        # and less that the last space
        # PROBLEM 3 CODE HERE
        catapults[space] = random.randint(1, space-1)
        
    # PROBLEM 4. RETURN THE trapdoors AND catapults DICTIONARIES
    # PROBLEM 4 CODE HERE
    return trapdoors, catapults

def rollDie():
    ''' roll a six sided die and return the value of the roll '''
    return random.randint(1, 6)

def playGame():
    # call getPlayerNames() to get names for each of the two players
    player1, player2 = getPlayerNames()
    
    # PROBLEM 5. FOLLOW THE PATTERN OF THE CODE THAT CALLS getPlayerNames()
    # WRITE CODE TO:    
    # Call getBoardInfo() to get values for boardSize, trapdoorNum and
    # catapultNum
    # PROBLEM 5 CODE HERE
    boardSize, trapdoorNum, catapultNum = getBoardInfo()
    # PROBLEM 6.  FOLLOW THE PATTERN OF THE CODE THAT CALLS getPlayerNames()
    # WRITE CODE TO:        
    # Call boardSetup() to get the two dictionaries giving the
    # space/destination pairs for trapdoors and catapults
    # PROBLEM 6 CODE HERE
    
    trapdoors, catapults = boardSetup(boardSize, trapdoorNum, catapultNum)
    
  
    # Initialize the board positions of the two players
    positions = {player1:1, player2:1} 

    # Set the initial player
    player = player1 

    # play continues until one player lands on the highest space
    while True:
        print()
        print(player, 'is on', positions[player])
        move = rollDie()
        print(player, 'rolls a', move)
        
        # move the current player if the move is not beyond the end
        # of the board. Print out the move.
        if positions[player] + move <= boardSize:
            positions[player] += move
            print(player, 'moves to', positions[player])

            # PROBLEM 7. WRITE CODE TO:
            # Check if the current player is on the last space, in which
            # case print a WINS! message and break out of the loop
            # PROBLEM 7 CODE HERE
            if positions[player] == boardSize:
                print(player, 'WINS!!!')
                break

            # check if the current player has landed on a trapdoor, in
            # which case move the player to the destination space and
            # print out a message saying what has happened.
            if positions[player] in trapdoors:
                positions[player] = trapdoors[positions[player]]
                print('Trapdoor!', player, 'falls to', positions[player])

            # PROBLEM 8. WRITE CODE TO MEET THIS SPECIFICATION
            # If the current player did not land on a trapdoor, check if 
            # the player landed on a catapult, in which case move the
            # player to the destination space and print out a message
            # saying what has happened.
            # PROBLEM 8 CODE HERE
            elif positions[player] in catapults:
                positions[player] = catapults[positions[player]]
                print("Catapult!", player, "falls to", positions[player])
            
        # The roll of the die moved the player beyond the end of the
        # board. Print out a message saying what happened.
        else:
            print('Off the board. Sorry, you lose your turn,', player)

        # PROBLEM 9. WRITE CODE TO:
        # switch current player
        # PROBLEM 9 CODE HERE
        if player == player1:
            player = player2
        else:
            player = player1
        
playGame()
