#!/usr/bin/python
# -*- coding: utf-8 -*-

import random


# This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round."""
#
# The Player class is the parent class for all of the Players
# in this game

class Player:

    choices = ['Rock', 'Paper', 'Scissors']

    def __init__(self):
        self.yourChoice = self.choices
        self.computerChoice = self.randChoice()

    def randChoice(self):
        return int(random.randint(0, len(self.choices) - 1))

    def learn(self, yourChoice, computerChoice):
        self.yourChoice = yourChoice
        self.computerChoice = computerChoice


class RandomPlayer(Player):

    def choice(self):
        return int(self.randChoice())


class ReflectPlayer(Player):

    def choice(self):
        return int(self.computerChoice)


class RockPlayer(Player):

    def choice(self):
        return int(0)


class CyclePlayer(Player):

    def choice(self):
        if self.yourChoice == 0:
            return 1
        elif self.yourChoice == 1:
            return 2
        else:
            return 0


class HumanPlayer(Player):

    def choice(self):
        ch0 = '0 => ' + self.choices[0] + '\n'
        ch1 = '1 => ' + self.choices[1] + '\n'
        ch2 = '2 => ' + self.choices[2] + '\n'
        val = str(input(ch0 + ch1 + ch2))
        if val == '0' or val == '1' or val == '2':
            return int(val)
        elif val == 'exit':
            exit()
        else:
            string = 'bad input, please select number bellow'
            print string
            return self.choice()


class Game:

    def __init__(self, human, computer):
        self.human = human
        self.computer = computer
        self.yourScore = 0
        self.computerScore = 0
        self.roundNumber = 0

    def beats(self, one, two):
        return one == 0 and two == 2 or one == 2 and two == 1 or one \
            == 1 and two == 0

    def setRounds(self):
        val = input('Number of rounds: ')
        if val.isdigit():
            self.rounds = int(val)
        elif val == 'exit':
            exit()
        else:
            self.setRounds()

    def setRoundNumber(self):
        self.roundNumber += 1

    def getRoundTitle(self):
        string = '\n' + '=' * 15 + ' ROUND: ' + str(self.roundNumber) \
            + ' ' + '=' * 15
        print string

    def setName(self):
        val = input('Your name: ')
        if val == 'exit':
            exit()
        self.name = val

    def setRound(self):
        self.humanChoice = self.human.choice()
        self.computerChoice = self.computer.choice()
        if self.beats(self.humanChoice, self.computerChoice):
            self.yourScore += 1
            self.winner = self.name
        elif self.humanChoice == self.computerChoice:
            self.winner = 'TIE'
            string = '=' * 15 + ' TIE REPEATING ROUND ' + '=' * 15
            print string
            self.repeatRound()
        else:
            self.computerScore += 1
            self.winner = 'Computer'

        self.human.learn(self.humanChoice, self.computerChoice)
        self.computer.learn(self.computerChoice, self.humanChoice)

    def repeatRound(self):
        self.setRoundNumber()
        self.getRoundTitle()
        self.printRound()
        self.setRound()

    def printRound(self):
        string = self.computer.choices[self.computerChoice] \
            + '\nComputer choice is: ' \
            + self.computer.choices[self.computerChoice] \
            + '\nYour choice is: ' \
            + self.human.choices[self.humanChoice] \
            + '\nWinner of the round: ' + self.winner \
            + '\nYour score is: ' + str(self.yourScore) + ' / ' \
            + str(self.computerScore)
        print string

    def play_round(self):
        self.setRound()
        self.printRound()

    def getRepeatedRounds(self):
        return self.roundNumber - self.rounds

    def finalText(self):
        string = '=' * 15 + ' REPEATED ROUNDS: ' \
            + str(self.getRepeatedRounds()) + ' ' + '=' * 15 + '=' * 15 \
            + ' REGULAR ROUNDS: ' + str(self.rounds) + ' ' + '=' * 15 \
            + '=' * 15 + ' TOTAL ROUNDS: ' + str(self.roundNumber) \
            + ' ' + '=' * 15
        return string

    def finalResult(self):
        if self.yourScore == self.computerScore:
            string = '=' * 15 \
                + ' TIE, PLEASE PLAY A FINAL ROUND IN THIS GAME: ' \
                + '=' * 15 + '\n' + self.finalText()
            print string
            self.play_round()
            self.finalResult()
        elif self.yourScore > self.computerScore:
            string = '\n' + '=' * 15 + ' ABSOLUTE WINNER IS: ' \
                + self.name + ' ' + '=' * 15 + '\n' + self.finalText() \
                + 'FINAL RESULT' + self.name + ': ' \
                + str(self.yourScore) + 'Computer: ' \
                + str(self.computerScore)
            print string
        else:
            string = '\n' + self.finalText() \
                + 'ABSOLUTE WINNER IS: COMPUTER ' + '=' * 20 \
                + '\nFINAL RESULT' + 'Computer: ' \
                + str(self.computerScore) + self.name + ': ' \
                + str(self.yourScore)
            print string

    def play_game(self):
        self.setName()
        self.setRounds()
        n = self.rounds
        while n > 0:
            self.setRoundNumber()
            self.getRoundTitle()
            self.play_round()
            n -= 1

        self.finalResult()


humanPlayer = HumanPlayer()
computerPlayer = random.choice([RandomPlayer(), ReflectPlayer(),
                               CyclePlayer(), RockPlayer()])
game = Game(humanPlayer, computerPlayer)
game.play_game()
