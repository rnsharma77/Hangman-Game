import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Challenge")
        self.master.geometry("600x500")
        self.master.configure(bg="#34495E")  # Background color
        
        # Title label
        self.title_label = tk.Label(master, text="Hangman Challenge", font=("Helvetica", 18, "bold"), fg="#F1C40F", bg="#34495E")
        self.title_label.pack(pady=10)
        
        # Description label
        self.description_label = tk.Label(master, text="Guess the hidden word, one letter at a time. Good luck!", 
                                          font=("Helvetica", 12), fg="#ECF0F1", bg="#34495E")
        self.description_label.pack(pady=5)
        
        # Word to guess label
        self.word_label = tk.Label(master, text="_ _ _ _ _", font=("Helvetica", 24, "bold"), fg="#F39C12", bg="#34495E")
        self.word_label.pack(pady=20)
        
        # Entry field for letter guess
        self.letter_entry = tk.Entry(master, font=("Helvetica", 14), bg="#1ABC9C", fg="#ECF0F1", insertbackground="#ECF0F1")
        self.letter_entry.pack(pady=5)
        
        # Submit button for guesses
        self.guess_button = tk.Button(master, text="Submit Guess", font=("Helvetica", 12, "bold"), bg="#3498DB", fg="white", command=self.submit_guess)
        self.guess_button.pack(pady=5)
        
        # Incorrect guesses display
        self.incorrect_label = tk.Label(master, text="Incorrect guesses left: 5", font=("Helvetica", 14), fg="#E74C3C", bg="#34495E")
        self.incorrect_label.pack(pady=5)
        
        # Letters guessed so far
        self.guessed_letters_label = tk.Label(master, text="Guessed Letters: ", font=("Helvetica", 12), fg="#ECF0F1", bg="#34495E")
        self.guessed_letters_label.pack(pady=5)
        
        # Message label for updates
        self.message_label = tk.Label(master, text="", font=("Helvetica", 12), fg="#F1C40F", bg="#34495E")
        self.message_label.pack(pady=10)
        
        # Initialize game variables
        self.words = ['python', 'challenge', 'interface', 'game', 'programming']
        self.secret_word = random.choice(self.words).upper()
        self.display_word = ['_'] * len(self.secret_word)
        self.incorrect_guesses = 5
        self.guessed_letters = []

        # Update word display
        self.update_word_display()

    def submit_guess(self):
        guess = self.letter_entry.get().upper()
        if guess and len(guess) == 1 and guess.isalpha():
            if guess in self.guessed_letters:
                self.message_label.config(text=f"You've already guessed '{guess}'!")
            elif guess in self.secret_word:
                self.guessed_letters.append(guess)
                for i, letter in enumerate(self.secret_word):
                    if letter == guess:
                        self.display_word[i] = letter
                self.update_word_display()
                if '_' not in self.display_word:
                    self.message_label.config(text="Congratulations! You've guessed the word!")
                    self.guess_button.config(state=tk.DISABLED)
            else:
                self.guessed_letters.append(guess)
                self.incorrect_guesses -= 1
                self.incorrect_label.config(text=f"Incorrect guesses left: {self.incorrect_guesses}")
                if self.incorrect_guesses == 0:
                    self.message_label.config(text=f"Game over! The word was {self.secret_word}.")
                    self.guess_button.config(state=tk.DISABLED)
            self.guessed_letters_label.config(text="Guessed Letters: " + ', '.join(self.guessed_letters))
        else:
            messagebox.showwarning("Invalid input", "Please enter a valid letter.")
        self.letter_entry.delete(0, tk.END)

    def update_word_display(self):
        self.word_label.config(text=" ".join(self.display_word))

# Running the Hangman Game Application
if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGame(root)
    root.mainloop()
