#vball.py
#this program simulates a volleyball game between two teams 4 different times
#the user enters the probability of the home team scoring a point on a serve 

import random

#main function that is created through top-design with smaller functions that simulate the game
def main():
    printIntro()
    probA, probB = getInput()
    winsA, winsB, totalScoreA, totalScoreB = simThreeGames(probA, probB)
    printSummary(winsA, winsB, totalScoreA, totalScoreB)

#prints introduction of program and explains overview of program's purpose
def printIntro():
    print("Welcome! This program simulates a game of volleyball between two")
    print("teams. The home team, Team A, and the opposing team, Team B. The")
    print("abilities of the home team are indicated by a probability (a number")
    print("between 0 and 1) that the team wins the point when serving. The home")
    print("team always has the first serve.\n")

#asks user for probability of home team scoring and creates probability of opposing team scoring
# a = home team probability
# b = opposing team probability 
def getInput():
    #exception handling in case user does not enter a number
    while True:
        try:
            print("Please enter a number between 0 and 1")
            a = eval(input("What is the probability that Team A will win the serve? "))
        except NameError:
            print("\nOops, it looks like you did not enter a number.")
            continue
        except SyntaxError:
            print("\nOops, it looks like you did not enter a number.")
            continue
        else:
            break
    b = 1 - a
    return a, b

#simulates one game of volleyball and returns prints out the score of each team
#totalScoreA and totalScoreB represent the total points scored for each team over the three games
#takes the probability of teamA and teamB and integrates them into playing each game
#returns the total points each team scored along with the amount of wins each team has 
def simThreeGames(probA, probB):
    winsA=winsB=0
    totalScoreA=0
    totalScoreB=0
    for i in range(3):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA+1
        else:
            winsB = winsB+1
        totalScoreA += scoreA
        totalScoreB += scoreB
    return winsA, winsB, totalScoreA, totalScoreB

#simulates one game of volleyball
#uses probabilities of team to help determine scores of both teams, returns the score of each team
def simOneGame(probA, probB):
    serving = "A"
    scoreA = 0
    scoreB = 0
    #the gameOver function takes the score of the game and determines if the game is over or not
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random.random()< probA:
                scoreA= scoreA +1
            else:
                serving = "B"
        else:
            if random.random()<probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    print("The score was",scoreA,"to",scoreB,"\n")
    return scoreA, scoreB 

#signals to program that game is over by returning true once requirements are satisfied 
def gameOver(a, b):
    return (a==15 and a-b>=2) or (b==15 and b-a>=2)

#prints the summary of wins and total score for both teams
def printSummary(winsA, winsB, totalScoreA, totalScoreB):
    print("\nThe home team won", winsA, "game(s).")
    print("\nThe opposing team won", winsB, "game(s).")
    print("\nThe home team scored a total of",totalScoreA, "points.")
    print("\nThe oppossing team scored a total of", totalScoreB, "points.")
    
    

#runs the main program to the console
main()
    
