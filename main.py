import colorama
colorama.init()

def read_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print(colorama.Fore.RED, f"The file '{file_name}' was not found. Please ensure the file name is correct.")
        return []

def count_words(lines):
    word_count = 0
    for line in lines:
        word_count += len(line.split())
    return word_count

def search_word(lines, word):
    results = []
    word_count = 0
    for line_number, line in enumerate(lines, start=1):
        if word.lower() in line.lower(): 
            results.append((line_number, line.strip()))
            word_count += line.lower().split().count(word.lower())
    return results, word_count

def display_results(results, word, word_count, total_words):
    if results:
        percentage = (word_count / total_words) * 100 if total_words > 0 else 0
        print(colorama.Fore.GREEN, f"\nSearch results for the word '{colorama.Fore.RED}{word}{colorama.Fore.GREEN}':")
        for line_number, line in results:
            print(f"{colorama.Fore.GREEN}Line {line_number}: {colorama.Fore.RED}{line}{colorama.Fore.RESET}")
        print(colorama.Fore.YELLOW, f"\nThe word '{colorama.Fore.RED}{word}{colorama.Fore.YELLOW}' makes up {colorama.Fore.GREEN}{percentage:.2f}%{colorama.Fore.YELLOW} of the text.")
    else:
        print(colorama.Fore.RED, f"\nNo matches found for the word '{word}'.")

def main():
    a = """
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░  ████████╗██╗░░██╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗  ╚══██╔══╝██║░░██║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║  ░░░██║░░░███████║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║  ░░░██║░░░██╔══██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝  ░░░██║░░░██║░░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝

░█████╗░██████╗░███╗░░░███╗██╗███╗░░██╗  ░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗
██╔══██╗██╔══██╗████╗░████║██║████╗░██║  ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║
███████║██████╔╝██╔████╔██║██║██╔██╗██║  ╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║
██╔══██║██╔══██╗██║╚██╔╝██║██║██║╚████║  ░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║
██║░░██║██║░░██║██║░╚═╝░██║██║██║░╚███║  ██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝  ╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

███████╗███╗░░██╗░██████╗░██╗███╗░░██╗███████╗██╗
██╔════╝████╗░██║██╔════╝░██║████╗░██║██╔════╝██║
█████╗░░██╔██╗██║██║░░██╗░██║██╔██╗██║█████╗░░██║
██╔══╝░░██║╚████║██║░░╚██╗██║██║╚████║██╔══╝░░╚═╝
███████╗██║░╚███║╚██████╔╝██║██║░╚███║███████╗██╗
╚══════╝╚═╝░░╚══╝░╚═════╝░╚═╝╚═╝░░╚══╝╚══════╝╚═╝"""
    print(colorama.Fore.LIGHTBLUE_EX, a)
    file_name = input("Enter the name of the text file to search: ")
    
    lines = read_file(file_name)
    if not lines:
        print(colorama.Fore.RED, "There is nothing here :(")
        return
    
    total_words = count_words(lines)
    if total_words == 0:
        print(colorama.Fore.RED, "The file is empty.")
        return
    
    while True:
        word = input("\nEnter the word to search for or 'exit' to quit: ")
        if word.lower() == "exit":
            print(colorama.Fore.GREEN, "Exiting the program. Have a great day!")
            return
        
        results, word_count = search_word(lines, word)
        display_results(results, word, word_count, total_words)

# Run the main program
if __name__ == "__main__":
    main()
