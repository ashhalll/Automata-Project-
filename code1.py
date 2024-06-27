import re
import tkinter as tk
from tkinter import messagebox, Toplevel, Label, Entry, Button

class CustomInputDialog(Toplevel):
    def __init__(self, parent, pattern):
        super().__init__(parent)
        self.parent = parent
        self.pattern = pattern  # Pass the compiled pattern into the dialog
        self.title("Check Regex")
        self.geometry("300x150")
        self.resizable(False, False)
        self.create_widgets()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_widgets(self):
        Label(self, text="Enter text to check (or type 'exit' to quit):").pack(pady=10)
        self.entry = Entry(self, width=40)
        self.entry.pack(padx=10, pady=5)
        self.entry.bind("<Return>", self.on_submit)
        Button(self, text="Submit", command=self.on_submit).pack(pady=10)
        self.status_label = Label(self, text="")
        self.status_label.pack(pady=5)

    def on_submit(self, event=None):
        text = self.entry.get()
        if text.lower() == 'exit':
            self.destroy()
        else:
            self.check_text(text)

    def check_text(self, text):
        if text:
            matches = self.pattern.fullmatch(text)
            result = "matches" if matches else "does not match"
            self.status_label.config(text=f"The text '{text}' {result}")
            self.entry.delete(0, 'end')  # Clear the entry field for new input
            output_result_to_file(text, matches)

    def on_close(self):
        self.destroy()

def compile_regex():
    language_chars = lang_text.get("1.0",'end-1c')
    regex_pattern = f"[{re.escape(language_chars)}]*"
    try:
        global pattern
        pattern = re.compile(regex_pattern)
    except re.error as e:
        messagebox.showerror("Regex Error", str(e))
        return False
    return True

def find_matches():
    # Ensure the pattern is compiled before opening the dialog
    if not compile_regex():
        return
    dialog = CustomInputDialog(root, pattern)
    root.wait_window(dialog)  # Wait for the dialog to close

def output_result_to_file(text, is_match):
    match_result = "Match: Yes" if is_match else "Match: No"
    with open("search_results.txt", "a") as file:
        file.write(f"Regex: {text} - {match_result}\n")

def clear_entries():
    lang_text.delete('1.0', 'end')

def exit_application():
    root.destroy()

# GUI setup
root = tk.Tk()
root.title('RegEx-based Language Search Engine')
root.geometry("450x200")
root.configure(background='darkseagreen1')

button_style = {'font': ('Times New Roman', 12), 'bg': 'grey25', 'fg': 'white'}
label_style = {'font': ('Times New Roman', 12), 'background': 'red', 'foreground': "white"}

lang_label = tk.Label(root, text='Enter Language Characters:', **label_style)
lang_label.grid(row=0, column=0, padx=5, pady=10, sticky='w')

lang_text = tk.Text(root, height=2, width=40, font=('Times New Roman', 10))
lang_text.grid(row=0, column=1, padx=5, pady=10, sticky='we')

compile_button = tk.Button(root, text='Compile and Start', command=find_matches, **button_style)
compile_button.grid(row=1, column=1, padx=5, pady=5, sticky='we')

exit_button = tk.Button(root, text='Exit', command=exit_application, **button_style)
exit_button.grid(row=2, column=1, padx=5, pady=5, sticky='n')

root.mainloop()
