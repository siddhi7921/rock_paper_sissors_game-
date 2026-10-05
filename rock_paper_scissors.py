"""A polished Rock, Paper, Scissors game with desktop and command-line modes."""

import argparse
import random
import time
import tkinter as tk
from tkinter import messagebox


CHOICES = ("rock", "paper", "scissors")
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
HAND_SIGNS = {
    "rock": "✊",
    "paper": "✋",
    "scissors": "✌",
}
CHOICE_COLORS = {
    "rock": "#ef6a62",
    "paper": "#4ab6a5",
    "scissors": "#f0b84b",
}


class RockPaperScissorsGame:
    """Create and run an animated first-to-five Rock, Paper, Scissors game."""

    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors - First to Five")
        self.root.geometry("900x640")
        self.root.minsize(760, 560)
        self.root.configure(bg="#111827")

        self.player_score = 0
        self.computer_score = 0
        self.round_number = 0
        self.is_animating = False
        self.animation_step = 0
        self.pending_choice = None
        self.animation_job = None

        self._build_interface()

    def _build_interface(self):
        header = tk.Frame(self.root, bg="#111827")
        header.pack(fill="x", padx=42, pady=(30, 12))

        tk.Label(
            header,
            text="ROCK  PAPER  SCISSORS",
            font=("Arial", 25, "bold"),
            fg="#f8fafc",
            bg="#111827",
        ).pack()
        tk.Label(
            header,
            text="FIRST TO FIVE WINS THE MATCH",
            font=("Arial", 10, "bold"),
            fg="#94a3b8",
            bg="#111827",
        ).pack(pady=(5, 0))

        scoreboard = tk.Frame(self.root, bg="#1f2937", highlightbackground="#334155", highlightthickness=1)
        scoreboard.pack(fill="x", padx=70, pady=(4, 22))
        for column in range(3):
            scoreboard.grid_columnconfigure(column, weight=1)

        self.player_score_label = self._score_label(scoreboard, "YOU", 0, "#67e8f9")
        self.player_score_label.grid(row=0, column=0, pady=14)
        tk.Label(scoreboard, text="VS", font=("Arial", 13, "bold"), fg="#94a3b8", bg="#1f2937").grid(row=0, column=1)
        self.computer_score_label = self._score_label(scoreboard, "COMPUTER", 0, "#fbbf24")
        self.computer_score_label.grid(row=0, column=2, pady=14)

        self.status_label = tk.Label(
            self.root,
            text="Choose your move to begin.",
            font=("Arial", 15, "bold"),
            fg="#e2e8f0",
            bg="#111827",
        )
        self.status_label.pack(pady=(0, 16))

        arena = tk.Frame(self.root, bg="#111827")
        arena.pack(fill="x", padx=70)
        for column in range(3):
            arena.grid_columnconfigure(column, weight=1)

        self.player_card = self._choice_card(arena, "YOUR MOVE", "?", "#38bdf8")
        self.player_card.grid(row=0, column=0, padx=10, sticky="ew")
        tk.Label(arena, text="VS", font=("Arial", 20, "bold"), fg="#64748b", bg="#111827").grid(row=0, column=1, padx=10)
        self.computer_card = self._choice_card(arena, "COMPUTER", "?", "#fbbf24")
        self.computer_card.grid(row=0, column=2, padx=10, sticky="ew")

        tk.Label(
            self.root,
            text="MAKE YOUR CHOICE",
            font=("Arial", 10, "bold"),
            fg="#94a3b8",
            bg="#111827",
        ).pack(pady=(26, 10))

        controls = tk.Frame(self.root, bg="#111827")
        controls.pack()
        self.choice_buttons = []
        for choice in CHOICES:
            button = tk.Button(
                controls,
                text="{}\n{}".format(HAND_SIGNS[choice], choice.upper()),
                command=lambda move=choice: self.play_round(move),
                font=("Segoe UI Emoji", 12, "bold"),
                fg="#0f172a",
                bg=CHOICE_COLORS[choice],
                activebackground="#f8fafc",
                activeforeground="#0f172a",
                bd=0,
                cursor="hand2",
                padx=24,
                pady=8,
                width=10,
            )
            button.pack(side="left", padx=7)
            self.choice_buttons.append(button)

        self.reset_button = tk.Button(
            self.root,
            text="New match",
            command=self.reset_game,
            font=("Arial", 10, "bold"),
            fg="#cbd5e1",
            bg="#111827",
            activebackground="#334155",
            activeforeground="#ffffff",
            bd=0,
            cursor="hand2",
        )
        self.reset_button.pack(pady=(22, 0))

    def _score_label(self, parent, name, score, color):
        frame = tk.Frame(parent, bg="#1f2937")
        tk.Label(frame, text=name, font=("Arial", 10, "bold"), fg="#94a3b8", bg="#1f2937").pack()
        number = tk.Label(frame, text=str(score), font=("Arial", 28, "bold"), fg=color, bg="#1f2937")
        number.pack()
        frame.score_number = number
        return frame

    def _choice_card(self, parent, title, choice, accent):
        card = tk.Frame(parent, bg="#1f2937", highlightbackground="#334155", highlightthickness=1, height=154)
        card.pack_propagate(False)
        tk.Label(card, text=title, font=("Arial", 10, "bold"), fg="#94a3b8", bg="#1f2937").pack(pady=(20, 8))
        value = tk.Label(card, text=choice, font=("Segoe UI Emoji", 28, "bold"), fg=accent, bg="#1f2937")
        value.pack()
        card.choice_value = value
        return card

    def play_round(self, player_choice):
        """Start a short animation, then compare both choices."""
        if self.is_animating:
            return

        self.is_animating = True
        self.pending_choice = player_choice
        self.animation_step = 0
        self._set_buttons_state("disabled")
        self._show_move(self.player_card, player_choice)
        self.status_label.config(text="Computer is thinking...", fg="#e2e8f0")
        self._animate_computer_choice()

    def _animate_computer_choice(self):
        previews = ("rock", "paper", "scissors", "rock", "paper", "scissors")
        if self.animation_step < len(previews):
            preview = previews[self.animation_step]
            self._show_move(self.computer_card, preview, "#cbd5e1")
            self.animation_step += 1
            self.animation_job = self.root.after(115, self._animate_computer_choice)
            return

        self.animation_job = None
        computer_choice = random.choice(CHOICES)
        self._show_move(self.computer_card, computer_choice)
        self._resolve_round(self.pending_choice, computer_choice)

    def _show_move(self, card, choice, color=None):
        """Show a hand sign and a readable move name in one game card."""
        card.choice_value.config(
            text="{}\n{}".format(HAND_SIGNS[choice], choice.upper()),
            fg=color or CHOICE_COLORS[choice],
        )

    def _resolve_round(self, player_choice, computer_choice):
        self.round_number += 1
        if player_choice == computer_choice:
            result = "DRAW! Both players chose {}.".format(player_choice.upper())
            color = "#e2e8f0"
        elif BEATS[player_choice] == computer_choice:
            self.player_score += 1
            result = "YOU WIN! {} beats {}.".format(player_choice.upper(), computer_choice.upper())
            color = "#67e8f9"
        else:
            self.computer_score += 1
            result = "COMPUTER WINS! {} beats {}.".format(computer_choice.upper(), player_choice.upper())
            color = "#fbbf24"

        self.player_score_label.score_number.config(text=str(self.player_score))
        self.computer_score_label.score_number.config(text=str(self.computer_score))
        self.status_label.config(text=result, fg=color)
        self.is_animating = False

        if self.player_score == 5 or self.computer_score == 5:
            self._finish_match()
        else:
            self._set_buttons_state("normal")

    def _finish_match(self):
        player_won = self.player_score == 5
        headline = "MATCH WON!" if player_won else "MATCH LOST"
        detail = "You reached five wins. Excellent play." if player_won else "The computer reached five wins this time."
        self.status_label.config(text=headline, fg="#67e8f9" if player_won else "#fbbf24")
        self.root.after(250, lambda: messagebox.showinfo(headline, detail + "\n\nStart a new match when you are ready."))

    def _set_buttons_state(self, state):
        for button in self.choice_buttons:
            button.config(state=state)

    def reset_game(self):
        """Reset every match value and return the interface to its starting state."""
        if self.animation_job is not None:
            self.root.after_cancel(self.animation_job)
            self.animation_job = None
        self.player_score = 0
        self.computer_score = 0
        self.round_number = 0
        self.is_animating = False
        self.player_score_label.score_number.config(text="0")
        self.computer_score_label.score_number.config(text="0")
        self.player_card.choice_value.config(text="?", fg="#38bdf8")
        self.computer_card.choice_value.config(text="?", fg="#fbbf24")
        self.status_label.config(text="New match. Choose your move.", fg="#e2e8f0")
        self._set_buttons_state("normal")


def run_command_line_game():
    """Play a first-to-five match from PowerShell or Command Prompt."""
    player_score = 0
    computer_score = 0

    print("\n" + "=" * 48)
    print("       ROCK PAPER SCISSORS - FIRST TO FIVE")
    print("=" * 48)
    print("Type rock, paper, or scissors. Type quit to exit.\n")

    while player_score < 5 and computer_score < 5:
        try:
            move = input("Choose rock, paper, or scissors: ").strip().lower()
        except EOFError:
            print("\nNo terminal input detected. Thanks for playing.")
            return
        if move in {"quit", "exit", "q"}:
            print("Thanks for playing.")
            return
        if move not in CHOICES:
            print("Please type rock, paper, scissors, or quit.\n")
            continue

        print("Computer is choosing", end="", flush=True)
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        computer_move = random.choice(CHOICES)
        print("\nComputer chose: {} {}".format(HAND_SIGNS[computer_move], computer_move.upper()))
        print("You chose:      {} {}".format(HAND_SIGNS[move], move.upper()))

        if move == computer_move:
            print("DRAW! Both players chose {}.".format(move.upper()))
        elif BEATS[move] == computer_move:
            player_score += 1
            print("YOU WIN! {} beats {}.".format(move.upper(), computer_move.upper()))
        else:
            computer_score += 1
            print("COMPUTER WINS! {} beats {}.".format(computer_move.upper(), move.upper()))

        print("Score - You: {} | Computer: {}\n".format(player_score, computer_score))

    if player_score == 5:
        print("MATCH WON! You reached five wins.")
    else:
        print("MATCH LOST. The computer reached five wins.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Play Rock, Paper, Scissors.")
    parser.add_argument("--cli", action="store_true", help="play in the terminal instead of the desktop window")
    arguments = parser.parse_args()

    if arguments.cli:
        run_command_line_game()
    else:
        try:
            app = tk.Tk()
            RockPaperScissorsGame(app)
            app.mainloop()
        except (tk.TclError, Exception) as exc:
            print("Desktop window unavailable ({}); starting terminal mode.\n".format(exc))
            run_command_line_game()
