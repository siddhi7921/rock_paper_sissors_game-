# ✊ Rock, Paper, Scissors

<div align="center">

### 🎮 An Animated Rock, Paper, Scissors Game Built with Python & Tkinter

Choose your move. Challenge the computer. Be the first to reach **5 victories**! 🏆

</div>

---

## ✨ Features

* 🎨 Clean and interactive desktop interface
* 🎬 Animated computer move reveal
* 🤖 Randomized computer choices
* 🏆 First-to-5 match system
* 📊 Live score tracking
* ⚡ Fast and lightweight
* 💻 Command-line gameplay mode
* 🔄 Play again without restarting the application
* 🧠 Simple and well-structured game logic

---

## 📸 Preview

> An interactive desktop game where you choose **Rock**, **Paper**, or **Scissors**, while the computer makes a random move after a short animated reveal.

---

## 🛠️ Built With

* **Python**
* **Tkinter**
* **Random Module**

---

## 🚀 Getting Started

### Prerequisites

Make sure Python is installed on your computer.

Check your Python version:

```powershell
python --version
```

---

## ▶️ Run the Desktop Game

Open PowerShell or Command Prompt inside the project folder and run:

```powershell
python rock_paper_scissors.py
```

The game window will open automatically.

Choose:

* ✊ **Rock**
* ✋ **Paper**
* ✌️ **Scissors**

The computer will randomly select its move after a short animated reveal.

The **first player to reach 5 points wins the match**. 🏆

---

## 💻 Command-Line Mode

You can also play directly from PowerShell or Command Prompt.

Run:

```powershell
python rock_paper_scissors.py --cli
```

Then enter one of the following commands:

```text
rock
paper
scissors
```

To exit the game:

```text
quit
```

### Example

```text
Your move: rock
Computer chose: scissors

🎉 You win this round!
Score: You 1 - 0 Computer
```

---

## 🧠 How the Game Works

The computer randomly selects one of the three available moves:

```python
random.choice(["rock", "paper", "scissors"])
```

The game then compares your move with the computer's move.

### Rules

| Your Move   | Beats       |
| ----------- | ----------- |
| ✊ Rock      | ✌️ Scissors |
| ✌️ Scissors | ✋ Paper     |
| ✋ Paper     | ✊ Rock      |

If both players choose the same move, the round ends in a **draw**.

---

## 🏆 Winning System

Each match continues until one player reaches:

```text
5 Points
```

### Possible Outcomes

* 🎉 **Player Wins** — You reach 5 points first.
* 🤖 **Computer Wins** — The computer reaches 5 points first.
* 🤝 **Draw** — Both players choose the same move for a round.

---

## 📁 Project Structure

```text
Rock-Paper-Scissors/
│
├── rock_paper_scissors.py
├── README.md
└── LICENSE
```

---

## 🎯 Why This Project?

This project demonstrates fundamental Python programming concepts, including:

* Variables and data types
* Conditional statements
* Functions
* Random number generation
* Event-driven programming
* GUI development with Tkinter
* Command-line arguments
* Game state management

It is a simple project, but it combines **logic, interactivity, animation, and user interface design** into one complete application.

---

## 🔮 Future Improvements

Some possible upgrades for future versions:

* 🔊 Sound effects
* 🎵 Background music
* 🎨 Multiple themes
* 🌙 Dark mode
* 📈 Match history and statistics
* 🧠 Difficulty levels
* 🤖 Smarter AI opponent
* 🏅 Achievement system
* 🌐 Online multiplayer mode

---

## 🤝 Contributing

Contributions, suggestions, and improvements are always welcome!

1. Fork this repository
2. Create a new branch
3. Make your changes
4. Submit a Pull Request

---

## 📄 License

This project is available under the **MIT License**.

---

<div align="center">

### ⭐ If you enjoyed this project, consider giving the repository a star!

**Made with ❤️ using Python**

🎮 *Choose wisely. Play smart. Reach 5. Win the match.* 🏆

</div>
