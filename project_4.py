import random

player1Path = [[2, 4], [3, 4], [4, 4], [4, 3], [4, 2], [4, 1], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0], [0, 1], [0, 2],
               [0, 3], [0, 4], [1, 4], [1, 3], [1, 2], [1, 1], [2, 1], [3, 1], [3, 2], [3, 3], [2, 3], [5, 5]]

player2Path = [[4, 2], [4, 1], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 4], [2, 4],
               [3, 4], [4, 4], [4, 3], [3, 3], [2, 3], [1, 3], [1, 2], [1, 1], [2, 1], [3, 1], [3, 2], [5, 5]]

player3Path = [[2, 0], [1, 0], [0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 4], [2, 4], [3, 4], [4, 4], [4, 3], [4, 2],
               [4, 1], [4, 0], [3, 0], [3, 1], [3, 2], [3, 3], [2, 3], [1, 3], [1, 2], [1, 1], [2, 1], [5, 5]]

player4Path = [[0, 2], [0, 3], [0, 4], [1, 4], [2, 4], [3, 4], [4, 4], [4, 3], [4, 2], [4, 1], [4, 0], [3, 0], [2, 0],
               [1, 0], [0, 0], [0, 1], [1, 1], [2, 1], [3, 1], [3, 2], [3, 3], [2, 3], [1, 3], [1, 2], [5, 5]]

score = [0, 0, 0, 0]


class Player:
    def __init__(self):
        self.startingPosition = [[0, 0], [0, 0], [0, 0], [0, 0]]
        self.currentLocation = [[0, 0], [0, 0], [0, 0], [0, 0]]
        self.name = ""
        self.index = [0, 0, 0, 0]
        self.killed = 0

    def setIndex(self, pawnNumber, index):
        self.index[pawnNumber] = index

    def getIndex(self, pawnNumber):
        return self.index[pawnNumber]

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setKill(self, k):
        self.killed = k

    def getKill(self):
        return self.killed

    def setStartingPosition(self, x, y):
        for i in range(4):
            self.startingPosition[i][0] = x
            self.startingPosition[i][1] = y

    def getStartingLocation(self):
        return self.startingPosition

    def getCurrentLocation(self):
        return self.currentLocation

    def setCurrentLocation(self, p, x, y):
        self.currentLocation[p][0] = x
        self.currentLocation[p][1] = y


def getPawns(p, x, y):
    count = 0
    for i in range(4):
        if p.getCurrentLocation()[i][0] == x and p.getCurrentLocation()[i][1] == y:
            count += 1
    return count


def printBoard(p1, p2, p3, p4, turn):
    print("-----------------")
    for i in range(5):
        print("|", end="")
        for j in range(5):
            pawnPresent = 0

            # For Blue Pawns
            if p1.getStartingLocation()[0][0] == j and p1.getStartingLocation()[0][1] == i:
                pawnPresent = 1
                pawnCount = getPawns(p1, j, i)
                if turn == 5 or turn == 1:
                    print("\033[0;30m\033[1;44m" + str(pawnCount) + "♜ \033[0;0m", end="")
                elif turn == 1:
                    newPawnCount = getPawns(p1, j, i)
                    if newPawnCount > 0:
                        print("\033[0;30m\033[1;44m" + str(newPawnCount) + "♜ \033[0;0m", end="")
                    else:
                        print("\033[1;44m   \033[0;0m", end="")
                elif turn == 2:
                    newPawnCount = getPawns(p2, j, i)
                    if newPawnCount > 0:
                        print("\033[0;30m\033[1;44m" + str(newPawnCount) + "♜ \033[0;0m", end="")
                    else:
                        print("\033[1;44m   \033[0;0m", end="")
                elif turn == 3:
                    newPawnCount = getPawns(p3, j, i)
                    if newPawnCount > 0:
                        print("\033[0;30m\033[1;42m" + str(newPawnCount) + "♜ \033[0;0m", end="")
                    else:
                        print("\033[1;44m   \033[0;0m", end="")
                elif turn == 4:
                    newPawnCount = getPawns(p4, j, i)
                    if newPawnCount > 0:
                        print("\033[0;30m\033[1;44m" + str(newPawnCount) + "♜ \033[0;0m", end="")
                    else:
                        print("\033[1;44m   \033[0;0m", end="")
            if getPawns(p1, j, i) > 0 and not (
                    j == p1.getStartingLocation()[0][0] and i == p1.getStartingLocation()[0][1]) \
                    and not (
                    j == p2.getStartingLocation()[0][0] and i == p2.getStartingLocation()[0][1]) \
                    and not (
                    j == p3.getStartingLocation()[0][0] and i == p3.getStartingLocation()[0][1]) \
                    and not (
                    j == p4.getStartingLocation()[0][0] and i == p4.getStartingLocation()[0][1]):
                pawnPresent = 1
                pawnCount = getPawns(p1, j, i)
                print("\033[0;34m" + str(pawnCount) + "♜ \033[0;0m", end="")

            # For Green Pawns
            if p2.getStartingLocation()[0][0] == j and p2.getStartingLocation()[0][1] == i:
                pawnPresent = 1
                pawnCount = getPawns(p2, j, i)
                if turn == 5 or turn == 2:
                    print("\033[0;30m\033[1;42m" + str(pawnCount) + "♜ \033[0;0m", end="")
                elif turn == 1:
                    newPawnCount = getPawns(p1, j, i)
                    if newPawnCount > 0:
                        print("\033[0;30m\033[1;42m" + str(newPawnCount) + "♜ \033[0;0m", end="")
                    else:
                        print("\033[1;42m   \033[0;0m", end="")
                elif turn == 2:
                    newPawnCount = getPawns(p2, j, i)
                    if newPawnCount > 0:
                        print("\033[0;30m\033[1;42m" + str(newPawnCount) + "♜ \033[0;0m", end="")
                    else:
                        print("\033[1;42m   \033[0;0m", end="")
                elif turn == 3:
                    newPawnCount = getPawns(p3, j, i)
                    if newPawnCount > 0:
                        print("\033[0;30m\033[1;42m" + str(newPawnCount) + "♜ \033[0;0m", end="")
                    else:
                        print("\033[1;42m   \033[0;0m", end="")
                elif turn == 4:
                    newPawnCount = getPawns(p4, j, i)
                    if newPawnCount > 0:
                        print("\033[0;30m\033[1;42m" + str(newPawnCount) + "♜ \033[0;0m", end="")
                    else:
                        print("\033[1;42m   \033[0;0m", end="")
            if getPawns(p2, j, i) > 0 and not (
                    j == p1.getStartingLocation()[0][0] and i == p1.getStartingLocation()[0][1]) \
                    and not (
                    j == p2.getStartingLocation()[0][0] and i == p2.getStartingLocation()[0][1]) \
                    and not (
                    j == p3.getStartingLocation()[0][0] and i == p3.getStartingLocation()[0][1]) \
                    and not (
                    j == p4.getStartingLocation()[0][0] and i == p4.getStartingLocation()[0][1]):
                pawnPresent = 1
                pawnCount = getPawns(p2, j, i)
                print("\033[0;32m" + str(pawnCount) + "♜ \033[0;0m", end="")

            # For Pink Pawns
            if p3.getStartingLocation()[0][0] == j and p3.getStartingLocation()[0][1] == i:
                pawnPresent = 1
                pawnCount = getPawns(p3, j, i)
                if turn == 5 or turn == 3:
                    print("\033[0;30m\033[1;45m" + str(pawnCount) + "♜ \033[0;0m", end="")
                elif turn == 1:
                    newPawnCount = getPawns(p1, j, i)
                    if newPawnCount > 0:
                        print("\033[0;30m\033[1;45m" + str(newPawnCount) + "♜ \033[0;0m", end="")
                    else:
                        print("\033[1;45m   \033[0;0m", end="")
                elif turn == 2:
                    newPawnCount = getPawns(p2, j, i)
                    if newPawnCount > 0:
                        print("\033[0;30m\033[1;45m" + str(newPawnCount) + "♜ \033[0;0m", end="")
                    else:
                        print("\033[1;45m   \033[0;0m", end="")
                elif turn == 3:
                    newPawnCount = getPawns(p3, j, i)
                    if newPawnCount > 0:
                        print("\033[0;30m\033[1;45m" + str(newPawnCount) + "♜ \033[0;0m", end="")
                    else:
                        print("\033[1;45m   \033[0;0m", end="")
                elif turn == 4:
                    newPawnCount = getPawns(p4, j, i)
                    if newPawnCount > 0:
                        print("\033[0;30m\033[1;45m" + str(newPawnCount) + "♜ \033[0;0m", end="")
                    else:
                        print("\033[1;45m   \033[0;0m", end="")
            if getPawns(p3, j, i) > 0 and not (
                    j == p1.getStartingLocation()[0][0] and i == p1.getStartingLocation()[0][1]) \
                    and not (
                    j == p2.getStartingLocation()[0][0] and i == p2.getStartingLocation()[0][1]) \
                    and not (
                    j == p3.getStartingLocation()[0][0] and i == p3.getStartingLocation()[0][1]) \
                    and not (
                    j == p4.getStartingLocation()[0][0] and i == p4.getStartingLocation()[0][1]):
                pawnPresent = 1
                pawnCount = getPawns(p3, j, i)
                print("\033[0;35m" + str(pawnCount) + "♜ \033[0;0m", end="")

            # For Yellow Pawns
            if p4.getStartingLocation()[0][0] == j and p4.getStartingLocation()[0][1] == i:
                pawnPresent = 1
                pawnCount = getPawns(p4, j, i)
                if turn == 5 or turn == 4:
                    print("\033[0;30m\033[1;43m" + str(pawnCount) + "♜ \033[0;0m", end="")
                elif turn == 1:
                    newPawnCount = getPawns(p1, j, i)
                    if newPawnCount > 0:
                        print("\033[0;30m\033[1;43m" + str(newPawnCount) + "♜ \033[0;0m", end="")
                    else:
                        print("\033[1;43m   \033[0;0m", end="")
                elif turn == 2:
                    newPawnCount = getPawns(p2, j, i)
                    if newPawnCount > 0:
                        print("\033[0;30m\033[1;43m" + str(newPawnCount) + "♜ \033[0;0m", end="")
                    else:
                        print("\033[1;43m   \033[0;0m", end="")
                elif turn == 3:
                    newPawnCount = getPawns(p3, j, i)
                    if newPawnCount > 0:
                        print("\033[0;30m\033[1;43m" + str(newPawnCount) + "♜ \033[0;0m", end="")
                    else:
                        print("\033[1;43m   \033[0;0m", end="")
                elif turn == 4:
                    newPawnCount = getPawns(p4, j, i)
                    if newPawnCount > 0:
                        print("\033[0;30m\033[1;43m" + str(newPawnCount) + "♜ \033[0;0m", end="")
                    else:
                        print("\033[1;43m   \033[0;0m", end="")
            if getPawns(p4, j, i) > 0 and not (
                    j == p1.getStartingLocation()[0][0] and i == p1.getStartingLocation()[0][1]) \
                    and not (
                    j == p2.getStartingLocation()[0][0] and i == p2.getStartingLocation()[0][1]) \
                    and not (
                    j == p3.getStartingLocation()[0][0] and i == p3.getStartingLocation()[0][1]) \
                    and not (
                    j == p4.getStartingLocation()[0][0] and i == p4.getStartingLocation()[0][1]):
                pawnPresent = 1
                pawnCount = getPawns(p4, j, i)
                print("\033[0;33m" + str(pawnCount) + "♜ \033[0;0m", end="")

            if j == 2 and i == 2:
                pawnPresent = 1
                print("\033[1;41m   \033[0;0m", end="")
            if pawnPresent == 0:
                print(" - ", end="")

        print("|")
    print("-----------------\n")


def gameFunction(currentRoll, pawnNumber, player, currentPlayer):
    pawnNumber -= 1
    if player.getIndex(pawnNumber) + currentRoll > 24:
        player.setIndex(pawnNumber, player.getIndex(pawnNumber) - currentRoll)
        print("\033[1;36mYou rolled to high...")
        print("Turn has been skipped\033[0;0m")
        return

    elif player.getIndex(pawnNumber) + currentRoll == 24:
        print("\033[1;36mOne of your pawns has escaped!")
        player.setIndex(pawnNumber, 24)
        score[currentPlayer - 1] += 1
        return

    while currentRoll > 0:
        print(currentRoll)
        print(player.getIndex(pawnNumber))
        print(pawnNumber)
        if player.getIndex(pawnNumber) == 15 and player.getKill() == 0:
            player.setIndex(pawnNumber, 0)
        else:
            player.setIndex(pawnNumber, player.getIndex(pawnNumber) + 1)
        currentRoll -= 1

    if currentPlayer == 1:
        player.setCurrentLocation(pawnNumber, player1Path[player.getIndex(pawnNumber)][0],
                                  player1Path[player.getIndex(pawnNumber)][1])
    elif currentPlayer == 2:
        player.setCurrentLocation(pawnNumber, player2Path[player.getIndex(pawnNumber)][0],
                                  player2Path[player.getIndex(pawnNumber)][1])
    elif currentPlayer == 3:
        player.setCurrentLocation(pawnNumber, player3Path[player.getIndex(pawnNumber)][0],
                                  player3Path[player.getIndex(pawnNumber)][1])
    elif currentPlayer == 4:
        player.setCurrentLocation(pawnNumber, player4Path[player.getIndex(pawnNumber)][0],
                                  player4Path[player.getIndex(pawnNumber)][1])

    location = player.getCurrentLocation()[pawnNumber]
    if location != [2, 4] and location != [4, 2] and location != [2, 0] and location != [0, 2]:
        if checkKill(currentPlayer, location, player):
            return 1
    return 0


def checkKill(currentPlayer, location, p1):
    for i in range(1, 5):
        if i != currentPlayer:
            n = str(i)
            player = eval("player" + n)
            for x in range(4):
                other = player.getCurrentLocation()[x]
                if location == other:
                    xx = player.getStartingLocation()[0][0]
                    yy = player.getStartingLocation()[0][1]
                    name = player.getName()
                    player.setCurrentLocation(x, xx, yy)
                    p1.setKill(1)
                    print(f"\033[91m\nA coin belonging to {name} has been killed!\033[0;0m\n")
                    return True
    return False


player1 = Player()
player1.setStartingPosition(2, 4)
player1.setCurrentLocation(0, 2, 4)
player1.setCurrentLocation(1, 2, 4)
player1.setCurrentLocation(2, 2, 4)
player1.setCurrentLocation(3, 2, 4)

player2 = Player()
player2.setStartingPosition(4, 2)
player2.setCurrentLocation(0, 4, 2)
player2.setCurrentLocation(1, 4, 2)
player2.setCurrentLocation(2, 4, 2)
player2.setCurrentLocation(3, 4, 2)

player3 = Player()
player3.setStartingPosition(2, 0)
player3.setCurrentLocation(0, 2, 0)
player3.setCurrentLocation(1, 2, 0)
player3.setCurrentLocation(2, 2, 0)
player3.setCurrentLocation(3, 2, 0)

player4 = Player()
player4.setStartingPosition(0, 2)
player4.setCurrentLocation(0, 0, 2)
player4.setCurrentLocation(1, 0, 2)
player4.setCurrentLocation(2, 0, 2)
player4.setCurrentLocation(3, 0, 2)

# main game

player1.setName(input("\033[1;34m(1) Input Player 1 Name: "))
player2.setName(input("\033[1;32m(2) Input Player 2 Name: "))
player3.setName(input("\033[1;35m(3) Input Player 3 Name: "))
player4.setName(input("\033[1;33m(4) Input Player 4 Name: \033[0;0m"))

print("\nGame has started!\n")
printBoard(player1, player2, player3, player4, 5)
print("=================\n")
players = [player1, player2, player3, player4]
currentPlayer = 1
while True:
    if currentPlayer > 4:
        currentPlayer = 1
    if currentPlayer == 1:
        print("\n\033[1;34mNow blue (Player 1) plays...")
    elif currentPlayer == 2:
        print("\n\033[1;32mNow green (Player 2) plays...")
    elif currentPlayer == 3:
        print("\n\033[1;35mNow pink (Player 3) plays...")
    elif currentPlayer == 4:
        print("\n\033[1;33mNow yellow (Player 4) plays...")
    player = eval("player" + str(currentPlayer))
    name = player.getName()
    print(f"This is {name}'s board:\033[0;0m\n")
    printBoard(player1, player2, player3, player4, currentPlayer)
    pawnNum = int(input(f"(1) Move coin at [{player.getCurrentLocation()[0][0]},{player.getCurrentLocation()[0][1]}]\n"
                        f"(2) Move coin at [{player.getCurrentLocation()[1][0]},{player.getCurrentLocation()[1][1]}]\n"
                        f"(3) Move coin at [{player.getCurrentLocation()[2][0]},{player.getCurrentLocation()[2][1]}]\n"
                        f"(4) Move coin at [{player.getCurrentLocation()[3][0]},{player.getCurrentLocation()[3][1]}]\n"
                        "Enter Choice: "))
    # input("\n33[5\nPress enter to roll dice!\033[0;0m\n")
    diceRoll = random.randint(1, 4)
    diceRoll = int(input("\nPress enter to roll dice:"))
    print(f"{name} rolled a {diceRoll}!\n")
    kill = gameFunction(diceRoll, pawnNum, player, currentPlayer)
    printBoard(player1, player2, player3, player4, currentPlayer)
    print("     - Current score - ")
    print("\033[1;34m ♜: " + str(score[0]) + " \033[1;32m ♜: " + str(score[1]) + " \033[1;35m ♜: " + str(
        score[2]) + " \033[1;33m ♜: " + str(score[3]) + "\033[0;0m")

    if diceRoll == 4:
        print("\n\033[1;36m       SUPERSHOT!")
        print("Usually u don't get lucky when you do, u need to roll")
        print("the dice again, cause who wants to stop the luck? 🤔\033[0;0m")
    elif kill == 1:
        print("\n\033[1;36m       THE RAGE IS ON!")
        print("You get an extra turn cause every small")
        print("victory needs to be celebrated 👑\033[0;0m")
    else:
        print("\n ====== End of turn ====== ")
        currentPlayer += 1
