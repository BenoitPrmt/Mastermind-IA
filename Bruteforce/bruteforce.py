LISTE_COULEURS = ("B" , "J" , "V" , "R")

class Bruteforce:
    def __init__(self, tries=8):
        self.tries = tries
        self.guesses = 0
        self.index = -1
        self.returned = []
        self.possible_solutions = []

        self.generate_possible_solutions()

    def update(self, guess, result):
        self.returned = (guess, result)
        # print(self.returned)

    def compare(self, solution, guess):
        retour = []

        for i in range(len(guess)):
            if solution[i] == guess[i]:
                retour.append("o")
            elif solution[i] in guess:
                retour.append("-")
            else:
                retour.append("x")

        return retour

    def generate_possible_solutions(self):
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        self.possible_solutions.append([LISTE_COULEURS[i], LISTE_COULEURS[j], LISTE_COULEURS[k], LISTE_COULEURS[l]])

    def guess(self):
        self.index += 1
        return self.possible_solutions[self.index]


if __name__ == "__main__":
    ia = Bruteforce()
    ia.generate_possible_solutions()
    ia.guess()