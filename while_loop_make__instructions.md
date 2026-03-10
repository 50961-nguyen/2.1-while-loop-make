## Setup
1. Git Clone this repository in your Make Folder
2. Create a file called while_loop_make.py 

## Instructions
You are going to finish off your rock-paper-scissors game! I have provided code to get you started. Your job is to compare `computer_choice` and `move` to see who won. Track the number of wins, losses, and ties.

**Note**: you do NOT need to track anything for invalid moves. Just keep asking user to re-enter their move input until it is valid.

Once you can play one game, set up a while loop to continue playing until the user enters in the word 'quit'. (Again, think of the idiot trap... when do we want the user to enter into the loop?)

If the user wins, your program must print
```plaintext
f"You win! {move} <action> {computer_choice}"
```

If the computer wins, your program must print
```plaintext
f"You lose! {computer_choice} <action> {move}"
```

If it's a tie, print
```plaintext
f"It's a tie!"
```

The actions are as follows

- rock **smashes** scissors
- paper **covers** rock
- scissors **cuts** paper

## Starter Code
```python
"""
TODO: Add Header comments here
"""

import random

# TODO: Create counter variables, ask the user if they want to play here

# TODO: write a loop to enter while the user does not enter quit:

    # Not set yet, leave this part of the code alone
    computer_choice = None
    random_int = random.randint(1,3)

    if random_int == 1:
        computer_choice = "rock"
    elif random_int == 2:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"

    # TODO: ask for the user's move and validate it. Check your While Loop Investigate

    # TODO: after getting the user's valid move, check for win, loss, and ties using conditionals

    # TODO: At the very bottom of the loop body, ask the user if they want to play again.
    # Make sure you use the same variable name for the input that you did BEFORe entering the loop

# TODO: Print the results 
```

### Sample Output
    Welcome to Rock, Paper, Scissors!
    Type anything to play rps (or quit): play
    Enter rock paper or scissors: rock
    It's a tie!
    Type anything to continue playing rps (or quit): yes
    Enter rock paper or scissors: ROCKSSS
    Invalid move!
    Enter rock paper or scissors: rock
    You win! rock smashes scissors
    Type anything to continue playing rps (or quit): no
    Enter rock paper or scissors: paper
    You lose! scissors cuts paper
    Type anything to continue playing rps (or quit): Quit
    Number of wins: 1
    Number of losses: 1
    Number of ties: 1