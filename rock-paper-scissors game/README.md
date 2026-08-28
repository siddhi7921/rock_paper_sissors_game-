# Rock Paper Scissors

An animated desktop Rock, Paper, Scissors game made with Python and Tkinter.

## Run

Open a terminal in this folder and run:

```powershell
python rock_paper_scissors.py
```

Choose Rock, Paper, or Scissors. The computer makes a random move after a short animated reveal. The first player to reach five wins takes the match.

## Command-line mode

To play directly in PowerShell or Command Prompt, run:

```powershell
python rock_paper_scissors.py --cli
```

Type `rock`, `paper`, or `scissors` for each round. Type `quit` to leave the game.

## Game logic

- `random.choice()` gives the computer a random move.
- Conditional branches compare the two moves.
- Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.
