
# given an array of bills a customer will pay with
# you start with 0 money
# you need to give them exact change so you get 5 dollars

def solution(bills):
    fives = 0
    tens = 0
    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            tens += 1
            fives -= 1
        elif tens > 0:
            tens -= 1
            fives -= 1
        else:
            fives -= 3

        if fives < 0:
            return False

    return True
