import random

hang6 = """
   ============
   |   \\    ||
   |    \\   ||
   O     \\  ||
  /|\     \\ ||
 / | \     \\||
  / \       ||
  | |       ||
            ||
           /||\\
          //||\\\\
         // || \\\\
        //  ||  \\\\
 =======================
"""

hang5 = """
   ============
   |   \\    ||
   |    \\   ||
         \\  ||
          \\ ||
           \\||
            ||
            ||
            ||
           /||\\
          //||\\\\
         // || \\\\
        //  ||  \\\\
 =======================
"""

hang4 = """
   ============
            ||
            ||
            ||
            ||
            ||
            ||
            ||
            ||
           /||\\
          //||\\\\
         // || \\\\
        //  ||  \\\\
 =======================
"""

hang3 = """

            ||
            ||
            ||
            ||
            ||
            ||
            ||
            ||
           /||\\
          //||\\\\
         // || \\\\
        //  ||  \\\\
 =======================
"""

hang2 = """

            ||
            ||
            ||
            ||
            ||
            ||
            ||
            ||
           /||
          //||
         // || 
        //  ||  
 =======================
"""

hang1 = """

            ||
            ||
            ||
            ||
            ||
            ||
            ||
            ||
            ||
            || 
            ||   
            ||  
 =======================
"""

hang0 = """













 =======================
"""

hanglist = [hang6, hang5, hang4, hang3, hang2, hang1, hang0]

wordlist = ['water', 'grass', 'fire', 'ice', 'ipad', 'icetea', 'horizon', 'crosshair', 'noob', 'icecream', 'pigeon', 'pokemon', 'laptop', 'python', 'protocol']
guesses = []
secretword = wordlist[random.randrange(0, len(wordlist))]
allowed_mistakes = 6
Finish = False

while not Finish:
    for letter in secretword:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"Allowed mistakes Left {allowed_mistakes}, Next Guess: ")
    guesses.append(guess.lower())

    while len(guess) > 1:
        print(f"You only can use 1 character")
        guess = input(f"Allowed mistakes Left {allowed_mistakes}, Next Guess: ")

    if guess.lower() not in secretword.lower():
        allowed_mistakes -= 1
        print(hanglist[allowed_mistakes])

        if allowed_mistakes == 0:
            break

    Finish = True
    for letter in secretword:
        if letter.lower() not in guesses:
            Finish = False

if Finish:
    print(f"You win! the word was: {secretword}")
else:
    print(f"U lost noob! the word was: {secretword}")
    print(hang6)

