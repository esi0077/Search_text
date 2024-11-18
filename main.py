import colorama
colorama.init()

def read_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print(colorama.Fore.RED, f"The file '{file_name}' was not found. Please ensure the file name is correct.")
        return []


def search_word(lines, word):
    results = []
    for line_number, line in enumerate(lines, start=1):
        if word.lower() in line.lower(): 
            results.append((line_number, line.strip()))
    return results


def display_results(results, word):
    if results:
        print(colorama.Fore.GREEN, f"\nSearch results for the word '{colorama.Fore.RED}{word}{colorama.Fore.GREEN}':")
        for line_number, line in results:
            print(f"{colorama.Fore.GREEN}Line {line_number}: {colorama.Fore.RED}{line}{colorama.Fore.RESET}")
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
    print(colorama.Fore.BLUE, a)
    file_name = input("Enter the name of the text file to search: ")
    
    lines = read_file(file_name)
    if not lines:
        print(colorama.Fore.RED, "there is nothing here :(")
        return
    while True:
        word = input("\nEnter the word to search for or 'exit' to quit: ")
        if word.lower() == "exit":
            print(colorama.Fore.GREEN, "Exiting the program. Have a great day!")
            return
        
        results = search_word(lines, word)
        display_results(results, word)


# Run the main program
if __name__ == "__main__":
    main()
