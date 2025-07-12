import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}
jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def provide_recommendation():
    print(Fore.CYAN + "What kind of place do you want to visit? (beaches / mountains / cities)")
    choice = normalize_input(input("> "))
    if choice in destinations:
        suggestion = random.choice(destinations[choice])
        print(Fore.GREEN + f"How about visiting {suggestion}?")
        print("Do you like this suggestion? (yes/no)")
        response = normalize_input(input("> "))
        if response == "yes":
            print(Fore.YELLOW + "Great! Have a wonderful trip!")
        else:
            print("Let's try again.")
            provide_recommendation()
    else:
        print("Sorry, I didn't understand. Please choose from: beaches, mountains, or cities.")
        provide_recommendation()

def offer_packing_tips():
    print(Fore.CYAN + "Where are you going? (beaches / mountains / cities)")
    location = normalize_input(input("> "))
    print("How many days are you planning to stay?")
    try:
        days = int(input("> "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if location == "beaches":
        tips = ["swimsuit", "sunscreen", "flip-flops"]
    elif location == "mountains":
        tips = ["hiking boots", "jacket", "water bottle"]
    elif location == "cities":
        tips = ["comfortable shoes", "city map", "camera"]
    else:
        print("Sorry, I don't have tips for that destination.")
        return

    print(Fore.GREEN + f"For a {days}-day trip to the {location}, you should pack:")
    for item in tips:
        print(f"- {item}")

def tell_joke():
    print(Fore.MAGENTA + random.choice(jokes))

def display_help():
    print(Fore.BLUE + "Available commands:")
    print("-recommend : Get a travel destination recommendation")
    print("- pack     : Get packingtips for you trip")
    print("- joke     : Hear a travel related joke")
    print("- help     : Show this help menu")
    print("- exit     : Exit the chatbot")

def chat():
    print(Fore.YELLOW + "Hello! I'm yout Travel Assistant Bot.")
    display_help()

    while True:
        print(Fore.CYAN + "\nWhat would you like to do?")
        command = normalize_input(input("> "))

        if command == "recommend":
            provide_recommendation()
        elif command == "pack":
            offer_packing_tips()
        elif command == "joke":
            tell_joke()
        elif command == "help":
            display_help()
        elif command == "exit":
            print(Fore.YELLOW + "Goodbye! Safe travels!")
            break
        else:
            print(Fore.RED + "Sorry, I didn't understand that command. Type 'help' to see options.")

if __name__ == "__main__":
    chat()
