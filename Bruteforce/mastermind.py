from random import randint
from bruteforce import Bruteforce

LISTE_COULEURS = ("B" , "J" , "V" , "R")

class MastermindBruteforce:
    def __init__(self, tries=8):
        self.tries = tries
        self.guesses = 0
        self.solution = []

    def generate_solution(self):
        self.solution = [LISTE_COULEURS[randint(0, len(LISTE_COULEURS)-1)] for _ in range(4)]

        print("Solution\n{}\n".format(self.solution))
        
    def compare(self, guess):
        retour = []
    
        for i in range(len(guess)):
            if self.solution[i] == guess[i]:
                retour.append("o")
            elif self.solution[i] in guess:
                retour.append("-")
            else:
                retour.append("x")
            
        return retour

    def ask_guess(self, ia):
        guess = ia.guess()
        return guess

    def play(self, ia):
        self.generate_solution()

        guess = ("A", "A", "A", "A")

        while not guess == self.solution or self.guesses == 500:

            guess = self.ask_guess(ia)

            self.guesses += 1

        print("Tours\tSolution\tDernière proposition")
        print("{}\t{}\t{}".format(self.guesses, self.solution, guess))

if __name__ == "__main__":
    mastermind = MastermindBruteforce()
    bf = Bruteforce()
    mastermind.play(bf)