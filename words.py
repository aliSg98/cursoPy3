import random

def computerGuess(lowval, highval, randNum, count =0):
    if highval >= lowval:
        guess = lowval + (highval - lowval) // 2
        if guess == randNum:
            return count
        elif guess > randNum:
            count = count + 1
            return computerGuess(lowval, guess-1, randNum, count)
        else:
            count = count + 1
            return computerGuess(guess + 1, highval, randNum, count)
    else:
        return -1
#end of function

#generate random number between 1 and 101
randNum = random.randint(1,101)

#count = 0
#guess = -99

if __name__ == '__main__':

    print("Computer took "+ str(computerGuess(6,100,randNum))+ " steps!")
#print("Computer took "+ str(computerGuess(6,100,randNum))+ " steps!")