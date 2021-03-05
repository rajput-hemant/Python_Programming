n = 18
guesses = 9
inp = None
while inp != n:
    inp = int(input("Guess The Number="))
    if int(inp) == 18:
        break
    if inp < 18:
        print("The number is greater than the number you guessed \nPlease Guess it Again!")
    else:
        print("The number is smaller than the number you guessed \nPlease Guess it Again!")
    guesses = guesses-1
    print("You have", guesses, "guesses left")
    if guesses == 0:
        print("GAME OVER!!!")
        break
if inp == n:
    print("Congrats you took", 9-guesses, "to guess the number")
