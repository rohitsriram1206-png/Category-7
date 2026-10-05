# Crypt-Arithmetic Puzzle using CSP
# SEND + MORE = MONEY

from itertools import permutations


def solve_cryptarithmetic():
    letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']

    # Digits available
    digits = range(10)

    # Try every possible assignment
    for values in permutations(digits, len(letters)):

        # Create letter -> digit mapping
        assignment = dict(zip(letters, values))

        # Leading letters cannot be zero
        if assignment['S'] == 0 or assignment['M'] == 0:
            continue

        S = assignment['S']
        E = assignment['E']
        N = assignment['N']
        D = assignment['D']
        M = assignment['M']
        O = assignment['O']
        R = assignment['R']
        Y = assignment['Y']

        # Convert words into numbers
        SEND = 1000*S + 100*E + 10*N + D
        MORE = 1000*M + 100*O + 10*R + E
        MONEY = 10000*M + 1000*O + 100*N + 10*E + Y

        # Check the constraint
        if SEND + MORE == MONEY:
            print("Solution Found:")
            
            for letter, digit in assignment.items():
                print(letter, "=", digit)

            print("\nSEND =", SEND)
            print("MORE =", MORE)
            print("MONEY =", MONEY)

            return


    print("No solution exists.")


solve_cryptarithmetic()