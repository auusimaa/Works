# TIE-02101 Programming 1
# Arttu Uusimaa, arttu.uusimaa@tuni.fi, student number: 292395
# Solution to exercise 15.4
# A program that adds, subtracts and multiplies polynomials

# TODO funktioiden kommentit ja muutkin kommentit


class Polynomial:

    def __init__(self, polynomial):
        """
        Constructor
        :param polynomial: str, polynimial added to the memory slot
        """
        self.__polynomial = polynomial
        self.__terms = {}

    def terms(self, slot):
        """
        Divides the polynomial into terms and prints the polynomial in the selected memory slot
        :param slot: int, number of the memory slot
        :return: None
        """
        terms = self.__polynomial.split(";")

        # Divides terms int o coefficients and exponents

        for term in terms:
            term = term.strip()
            coef_and_exp = term.split(" ")
            coefficient = coef_and_exp[0]
            exponent = coef_and_exp[1]
            self.__terms[exponent] = coefficient

        # Prints the contents of the memory slot in descending exponent order

        print("Memory location ", slot, ":", sep="", end=" ")
        print(" + ".join("x^".join((str(v), str(k))) for k, v in sorted(self.__terms.items(), reverse=True)))

    def addition(self, polynomial2, slot1, slot2):
        """
        Adds two polynomials together
        :param polynomial2:
        :param slot1:
        :param slot2:
        :return:
        """

        self.terms(slot1)
        polynomial2.terms(slot2)

        for key in self.__terms:

            if key in polynomial2.__terms:
                coeff_1 = int(self.__terms[key])
                coeff_2 = int(polynomial2.__terms[key])
                sum_of_coeff = coeff_1 + coeff_2
                self.__terms[key] = sum_of_coeff

        for key in polynomial2.__terms:

            if key not in self.__terms:
                self.__terms[key] = polynomial2.__terms[key]

        print("The simplified result:")
        print(" + ".join("x^".join((str(v), str(k))) for k, v in sorted(self.__terms.items(), reverse=True)))

    def subtraction(self, polynomial2, slot1, slot2):
        """
        Subtracts two polynomials
        :param polynomial2: object, polynomial that is subtracted
        :param slot1: int, memory slot of the first polynomial
        :param slot2: int, memory slot of the second polynomial
        :return: None
        """

        self.terms(slot1)
        polynomial2.terms(slot2)

        for key in self.__terms:

            if key in polynomial2.__terms:
                coeff_1 = int(self.__terms[key])
                coeff_2 = int(polynomial2.__terms[key])
                difference = coeff_1 + (coeff_2 * -1)
                self.__terms[key] = difference

        for key in polynomial2.__terms:

            if key not in self.__terms:

                coeff_2 = polynomial2.__terms[key]
                coeff_2 = (int(coeff_2) * -1)
                polynomial2.__terms[key] = coeff_2
                self.__terms[key] = polynomial2.__terms[key]

        print("The simplified result:")
        print(" + ".join("x^".join((str(v), str(k))) for k, v in sorted(self.__terms.items(), reverse=True)))

    def multiplication(self, polynomial2, slot1, slot2):

        self.terms(slot1)
        polynomial2.terms(slot2)
        multiplied_polynomial = {}
        for key in self.__terms:

            for key2 in polynomial2.__terms:

                exponent1 = int(key)
                exponent2 = int(key2)
                coeff1 = int(self.__terms[key])
                coeff2 = int(polynomial2.__terms[key2])
                exponent3 = exponent2 + exponent1
                coeff3 = coeff2 * coeff1

                multiplied_polynomial[exponent3] = coeff3

        print("The simplified result:")
        print(" + ".join("x^".join((str(v), str(k))) for k, v in sorted(multiplied_polynomial.items(), reverse=True)))


def add_to_memory(file_name, calculator_memory):

    sourcefile = open(file_name, 'r')
    slot = 0

    for line in sourcefile:
        polynomial = Polynomial(line)
        calculator_memory[slot] = polynomial
        slot += 1

    return calculator_memory


def error_check(command):
    """
    Checks that the input is in correct format
    and if it is, splits it into usable parts
    :param command: str, user input
    :return: str, command inputted
    """

    # TODO

def main():

    polynomial_file = str(input("Enter file name: "))
    calculator_memory = {}

    try:
        add_to_memory(polynomial_file, calculator_memory)

        while True:
            command = str(input("> "))

            while False:
                error_check(command)

            parts = command.split(" ")
            slot1 = int(parts[0])
            operator = str(parts[1])
            slot2 = int(parts[2])

            polynomial1 = calculator_memory[int(slot1)]
            polynomial2 = calculator_memory[int(slot2)]

            if operator == '+':

                polynomial1.addition(polynomial2, slot1, slot2)

            elif operator == '-':

                polynomial1.subtraction(polynomial2, slot1, slot2)

            elif operator == '*':

                polynomial1.multiplication(polynomial2, slot1, slot2)

            elif command == 'quit':
                print("Bye bye!")
                return

    except OSError:
        print("Error in reading the file.")


main()

