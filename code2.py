import re
import tkinter as tk
from tkinter import messagebox

def find_matches():
    # Clear previous matches
    text_entry.tag_remove("match", "1.0", "end")
    
    regex = regex_entry.get()
    text = text_entry.get('1.0', 'end-1c')
    
    if regex and text:
        matches = re.finditer(regex, text)
        for match in matches:
            start_index = f"1.0 + {match.start()} chars"
            end_index = f"1.0 + {match.end()} chars"
            text_entry.tag_add("match", start_index, end_index)
        text_entry.tag_config("match", foreground='black', background='red', font=('Arial', 10, 'bold'))
    save_to_file(regex, text)
    
def check_match():
    regex = regex_entry.get()
    text = text_entry.get('1.0','end-1c')
    if regex and text:
        if re.match(regex, text):
            messagebox.showinfo("Match Result", "Regex matches the whole text!")
        else:
            messagebox.showinfo("Match Result", "Regex does not match the whole text!")

def save_to_file(regex, text):
    with open("regex_and_text.txt", "w") as file:
        file.write("Regular Expression: ")
        file.write(regex + "\n")
        file.write("Text: ")
        file.write(text)
        
#styling
root = tk.Tk()
root.title('RegEx-based Text Search Engine')


root.geometry("500x300")
root.configure(background='darkseagreen1')

regex_label = tk.Label(root, text='Enter RegEx:', font=('Times New Roman', 12), background='palevioletred')
regex_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

text_label = tk.Label(root, text='Enter Text:', font=('Times New Roman', 12), background='lightblue')
text_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')

regex_entry = tk.Entry(root, width=50, font=('Times New Roman', 10))
regex_entry.grid(row=0, column=1, padx=5, pady=5, sticky='we')

text_entry = tk.Text(root, width=50, height=8, font=('Times New Roman', 10))
text_entry.grid(row=1, column=1, padx=5, pady=5, sticky='we')

find_button = tk.Button(root, text='Find Matches', command=find_matches, font=('Times New Roman', 12), bg='lightgreen')
find_button.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky='we')

check_button = tk.Button(root, text='Check Match', command=check_match, font=('Times New Roman', 12), bg='lightgreen')
check_button.grid(row=3, column=1, columnspan=2, padx=5, pady=5, sticky='we')

result_label = tk.Label(root, text='', font=('Times New Roman', 12), fg='green', background='darkseagreen1')
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
root.mainloop()