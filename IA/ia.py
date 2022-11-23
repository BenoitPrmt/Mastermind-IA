LISTE_COULEURS = ("B" , "J" , "V" , "R")

class IA:
    def __init__(self):
        self.index = -1
        self.next_guess = []
        self.possible_solutions = []

        self.generate_possible_solutions()

    def update(self, guess, result):
        for  i in range(len(guess)):
            if result[i] == "x":
                for solution in self.possible_solutions:
                    if solution[i] == guess[i]:
                        self.possible_solutions.remove(solution)
                        self.index = -1
            elif result[i] == "o":
                for solution in self.possible_solutions:
                    if solution[i] != guess[i]:
                        self.possible_solutions.remove(solution)
                        self.index = -1
                self.next_guess.append(guess[i])
            elif result[i] == "-":
                for solution in self.possible_solutions:
                    if solution[i] == guess[i]:
                        self.possible_solutions.remove(solution)
                        self.index = -1
                self.next_guess.append('?')

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
    ia = IA()
    ia.generate_possible_solutions()
    ia.guess()