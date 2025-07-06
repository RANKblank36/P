from textblob import TextBlob
import colorama 
from colorama import Fore, Style
import sys
import time

colorama.init(autoreset=True)

def show_animation():
    print(f"{Fore.MAGENTA}Analyzing sentiment", end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="")
        sys.stdout.flush()
    print()

    print(f"{Fore.CYAN}{Style.BRIGHT}Welcome to AI mood Detector!")
    name = input ("What's your name? ").strip().title()
    print(f"\nNice to meet you, {Fore.GREEN}{name}{Fore.RESET}! Let's detect the mood in your sentences.")
    print(f"Type'{Fore.YELLOW}exit{Fore.RESET}' anytime to quir. \n")

    while True:
        sentence = input(f"{Fore.BLUE}Your sentence: {Style.RESET_ALL}").strip()

        if sentence.lower() == "exit":
            print(f"\n{Fore.CYAN}Farewell, Agent {name}! Stay posotive :D")
            break

        if not sentence:
            print(f"{Fore.RED}Please enter something to analyze.\n")
            continue

        show_animation()

        blob = TextBlob(sentence)
        polarity = blob.sentiment.polarity

        if polarity > 0.75:
            print(f"{Fore.GREEN}Very Positive sentiment detected! (Score: {polarity:.2f})\n")
        elif 0.25 < polarity <= 0.75:
            print(f"{Fore.GREEN}Positive sentiment detected! (Score: {polarity:.2f})\n")
        elif -0.25 < polarity <= 0.25:
            print(f"{Fore.YELLOW}Neutral sentiment detected! (Score: {polarity:.2f})\n")
        elif 0.75 < polarity <= -0.25:
            print(f"{Fore.RED}Negative sentiment detected! (Score: {polarity:.2f})\n")
        else:
            print(f"{Fore.RED}Very Negative sentiment detected! (Score: {polarity:.2f})\n")
