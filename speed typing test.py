import tkinter as tk
import random
import time

def start_typing():
    global start_time
    input_entry.config(state=tk.NORMAL)
    input_entry.delete(0, tk.END)
    text_to_type.config(state=tk.NORMAL)
    text_to_type.delete("1.0", tk.END)
    random_text = get_random_text()
    text_to_type.insert("1.0", random_text)
    input_entry.focus_set()
    start_time = time.time()

def get_random_text():
    words = ["Python", "is", "a", "high-level", "programming", "language", "used", "for", "web", "development",
             "data", "analysis", "artificial", "intelligence", "and", "more."]
    return " ".join(random.choices(words, k=15))

def end_typing(event=None):
    global start_time
    input_entry.config(state=tk.DISABLED)
    end_time = time.time()
    typed_text = input_entry.get()
    original_text = text_to_type.get("1.0", tk.END).strip()
    accuracy = calculate_accuracy(original_text, typed_text)
    time_taken = round(end_time - start_time, 2)
    wpm = calculate_wpm(typed_text, time_taken)
    result_label.config(text=f"Accuracy: {accuracy}% | Time: {time_taken} seconds | WPM: {wpm}")

def calculate_accuracy(original_text, typed_text):
    correct_count = sum(1 for a, b in zip(original_text, typed_text) if a == b)
    accuracy = (correct_count / len(original_text)) * 100
    return round(accuracy, 2)

def calculate_wpm(typed_text, time_taken):
    words_typed = len(typed_text.split())
    wpm = (words_typed / time_taken) * 60
    return round(wpm)

# Create the main window
root = tk.Tk()
root.title("Speed Typing Test")
root.geometry("500x250")

# Text to type label
text_to_type = tk.Text(root, wrap=tk.WORD, width=60, height=3)
text_to_type.insert("1.0", "Click 'Start' to begin typing the text below:")
text_to_type.config(state=tk.DISABLED)
text_to_type.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Input Entry
input_entry = tk.Entry(root, width=60)
input_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
input_entry.bind("<Return>", end_typing)

# Start button
start_button = tk.Button(root, text="Start", command=start_typing)
start_button.grid(row=2, column=0, padx=5, pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

root.mainloop()
