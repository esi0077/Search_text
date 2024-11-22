
# ░█████╗░██████╗░███╗░░░███╗██╗███╗░░██╗  ███████╗░██████╗███╗░░░███╗░█████╗░██╗██╗░░░░░██╗
# ██╔══██╗██╔══██╗████╗░████║██║████╗░██║  ██╔════╝██╔════╝████╗░████║██╔══██╗██║██║░░░░░██║
# ███████║██████╔╝██╔████╔██║██║██╔██╗██║  █████╗░░╚█████╗░██╔████╔██║███████║██║██║░░░░░██║
# ██╔══██║██╔══██╗██║╚██╔╝██║██║██║╚████║  ██╔══╝░░░╚═══██╗██║╚██╔╝██║██╔══██║██║██║░░░░░██║
# ██║░░██║██║░░██║██║░╚═╝░██║██║██║░╚███║  ███████╗██████╔╝██║░╚═╝░██║██║░░██║██║███████╗██║
# ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝  ╚══════╝╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝╚═╝
# github : esi0077
# email : armines765@gmail.com
# website : esi0077.github.io 


# customtkinter for gui 
# colorama for colors = used in last version not in gui version
# Import for file browsing by filedialog 

import customtkinter as ctk
import colorama
from tkinter import filedialog  

colorama.init()

# lese inn tekst = reading the text file using utf-8
def lesInnTekst(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

# bla gjennom fil = search in files (brows files)
# using filedialog in tk to browes file it only search for txt files and if its another type you get an error
def blaGjennomFil(file_entry):
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        # if file path dosent exist app will end the session
        file_entry.delete(0, "end")
        file_entry.insert(0, file_path)

# ord teller = counting how many words it find from the search
# counting the words by using a for loop so in each line it find the word and return a word count 
# each time it find word in line the count going to go up by 1 as i wrote += 
def ord_teller(lines):
    word_count = 0
    for line in lines:
        word_count += len(line.split())
    return word_count

# søk ord = searching for the word  
# searching for the word by using a result arry 
# it going to use the word_count from ord_teller function 
# it got a loop that going to find the line number (starts from 1 *we dont have line 0 XD*)
# if the word is in that line it going to append it in the result (write it in result)
# returning the result and amount
def sok_ord(lines, word):
    results = []
    word_count = 0
    for line_number, line in enumerate(lines, start=1):
        if word.lower() in line.lower():  
            results.append((line_number, line.strip()))
            word_count += line.lower().split().count(word.lower())
    return results, word_count

# print tekst  = printing the text after finding it - result going to print from this function
# getting the result , word and etc from returns and going to use them for printing
# used result text (tk function that can help us printing the result in a text box)
# printing back to back by using += that make the text back to back 
# using /n to line up results (it skip one line and type)
# if it dosent find any word then its going to print the "else" and end the search
def printTekst(results, word, word_count, total_words, result_text_widget):
    result_text_widget.delete(1.0, "end") 

    if results:
        percentage = (word_count / total_words) * 100 if total_words > 0 else 0

        result_text = f"\nSøkeresultater for ordet '{word}':\n"

        for line_number, line in results:
            result_text += f"Linje {line_number}: {line}\n"

        result_text += f"\nOrdet '{word}' utgjør {percentage:.2f}% av teksten."

        result_text += f"\n\n ( ͡❛ ͜ʖ ͡❛) 𝔱𝔥𝔞𝔫𝔨𝔰 𝔣𝔬𝔯 𝔲𝔰𝔦𝔫𝔤 𝔱𝔥𝔦𝔰 𝔞𝔭𝔭 ©̲𝟮𝟬𝟮𝟰"

        result_text_widget.insert("end", result_text)
    else:
        result_text_widget.insert("end", f"\nIngen treff funnet for ordet '{word}'.\n")

    result_text_widget.yview("end") 

# søk på klikk = search on click - search field for clicking on søk/search
# working with ui the function going to run on button click 
# using tk buttons and give this function to it 
# if your file dose not have any lines then you get an error 
# if python file dose not found the file then you get another reeor 
# if it exist then it print your result
def sok_pa_klikk(file_name, word, result_text_widget):
    lines = lesInnTekst(file_name)
    if not lines:
        result_text_widget.insert("end", "Filen eksisterer ikke eller er tom.\n")
        return

    total_words = ord_teller(lines)
    if total_words == 0:
        result_text_widget.insert("end", "Filen er tom.\n")
        return

    results, word_count = sok_ord(lines, word)
    printTekst(results, word, word_count, total_words, result_text_widget)

# av for avslutte = off button for closing the app
# just for closing the app, it using the window.quit that is a function in ctk/tk
def av(window):
    window.quit()

# if you click on enter then it will search for you 
# it helps the user to search as fast as they can 
# you dont need to use your mouse that much
def search_on_enter(event=None, file_entry=None, word_entry=None, result_text_widget=None):
    sok_pa_klikk(file_entry.get(), word_entry.get(), result_text_widget)

# main app gui (custom tkinter)
# the gui functions are not har you can just read docs file of the customtk
# CTK website : https://customtkinter.tomschimansky.com/documentation/
def main():
    # using dark mode
    ctk.set_appearance_mode("dark") 
    # using the main color as dark-blue
    ctk.set_default_color_theme("dark-blue")
    # define the ctk with ver window
    window = ctk.CTk()  
    # the title
    window.title("tekstsøk")
    # size of window
    window.geometry("700x550")
    # can person resize it ?
    window.resizable(False, False)  
    # background color
    window.configure(bg='black')
    # binding using enter function
    window.bind("<Return>", lambda event: search_on_enter(event, file_entry, word_entry, result_text_widget))

    # ---------------------  Buttons and actions --------------------------- #

    title_label = ctk.CTkLabel(window, text="Søk i din tekst", font=("Arial", 24, "bold"), text_color="white")
    title_label.pack(pady=20)

    file_frame = ctk.CTkFrame(window)
    file_frame.pack(pady=10)

    file_label = ctk.CTkLabel(file_frame, text="Filnavn:", font=("Arial", 14), text_color="white")
    file_label.pack(side="left", padx=10)

    file_entry = ctk.CTkEntry(file_frame, width=300, font=("Arial", 14), placeholder_text="filnavn", corner_radius=10, fg_color="transparent", text_color="white", border_width=0)
    file_entry.pack(side="left")

    browse_button = ctk.CTkButton(file_frame, text="Bla gjennom", font=("Arial", 12, "bold"), height=40, width=120, corner_radius=10, fg_color="#009933", text_color="white", border_width=0, command=lambda: blaGjennomFil(file_entry))
    browse_button.pack(side="left", padx=10)

    word_frame = ctk.CTkFrame(window)
    word_frame.pack(pady=10)

    word_label = ctk.CTkLabel(word_frame, text="Ord å søke etter:", font=("Arial", 14), text_color="white")
    word_label.pack(side="left", padx=10)

    word_entry = ctk.CTkEntry(word_frame, width=300, font=("Arial", 14), placeholder_text="søk etter ord", corner_radius=10, fg_color="transparent", text_color="white", border_width=0)
    word_entry.pack(side="left")

    button_frame = ctk.CTkFrame(window)
    button_frame.pack(pady=20)

    search_button = ctk.CTkButton(button_frame, text="Søk", font=("Arial", 14, "bold"), height=40, width=150, corner_radius=10, fg_color="#0066cc", text_color="white", border_width=0, command=lambda: sok_pa_klikk(file_entry.get(), word_entry.get(), result_text_widget))
    search_button.pack(side="left", padx=20)

    exit_button = ctk.CTkButton(button_frame, text="Avslutt", font=("Arial", 14, "bold"), height=40, width=150, corner_radius=10, fg_color="#cc0000", text_color="white", border_width=0, command=lambda: av(window))
    exit_button.pack(side="left")

    result_text_widget = ctk.CTkTextbox(window, height=200, width=600, font=("Arial", 14), corner_radius=10, text_color="white", border_width=0, state="normal")
    result_text_widget.pack(pady=10)

    window.mainloop()

# runing the main app 

if __name__ == "__main__":
    main()
