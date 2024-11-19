import customtkinter as ctk
import colorama

colorama.init()

def lesInnTekst(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def ord_teller(lines):
    word_count = 0
    for line in lines:
        word_count += len(line.split())
    return word_count

def sok_ord(lines, word):
    results = []
    word_count = 0
    for line_number, line in enumerate(lines, start=1):
        if word.lower() in line.lower():  
            results.append((line_number, line.strip()))
            word_count += line.lower().split().count(word.lower())
    return results, word_count

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

def av(window):
    window.quit()

def main():
    ctk.set_appearance_mode("dark") 
    ctk.set_default_color_theme("dark-blue")
    window = ctk.CTk()  
    window.title("Verktøy for tekstsøk")
    window.geometry("700x550")
    window.resizable(False, False)  
    window.configure(bg='black')


    title_label = ctk.CTkLabel(window, text="Søk i din tekst", font=("Arial", 24, "bold"), text_color="white")
    title_label.pack(pady=20)


    file_frame = ctk.CTkFrame(window)
    file_frame.pack(pady=10)

    file_label = ctk.CTkLabel(file_frame, text="Filnavn:", font=("Arial", 14), text_color="white" )
    file_label.pack(side="left", padx=10)


    file_entry = ctk.CTkEntry(file_frame, width=300, font=("Arial", 14), placeholder_text="filnavn", corner_radius=10, fg_color="transparent", text_color="white", border_width=0)
    file_entry.pack(side="left")

    word_frame = ctk.CTkFrame(window)
    word_frame.pack(pady=10)

    word_label = ctk.CTkLabel(word_frame, text="Ord å søke etter:", font=("Arial", 14), text_color="white" )
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

if __name__ == "__main__":
    main()
