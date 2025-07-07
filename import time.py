import time
import re
from textblob import TextBlob
from colorama import init, Fore, Style

init(autoreset=True)

history = []
sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}

def show_processing_animation():
    animation = "|/-\\"
    print("Analyzing", end="")
    for i in range(10):
        time.sleep(0.1)
        print(f"\rAnalyzing {animation[i % len(animation)]}", end="")
    print("\rAnalysis complete!   ")

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        sentiment = "positive"
        color = Fore.GREEN
    elif polarity < -0.1:
        sentiment = "negative"
        color = Fore.RED
    else:
        sentiment = "neutral"
        color = Fore.YELLOW
    
    print(f"{color}Sentiment: {sentiment.upper()} | Polarity Score: {polarity:.2f}")
    history.append((text, sentiment, polarity))
    sentiment_counts[sentiment] += 1

def execute_command(command):
    if command == "summary":
        print(Fore.CYAN + "📊 Sentiment Summary:")
        for k, v in sentiment_counts.items():
            print(f" - {k.capitalize()}: {v}")
    elif command == "reset":
        history.clear()
        for key in sentiment_counts:
            sentiment_counts[key] = 0
        print(Fore.CYAN + "🔄 Data has been reset.")
    elif command == "history":
        print(Fore.CYAN + "🕘 Conversation History:")
        for i, (msg, sentiment, score) in enumerate(history, 1):
            print(f"{i}. [{sentiment.title()} | {score:.2f}] → {msg}")
    elif command == "help":
        print(Fore.CYAN + "🛠️ Available Commands:\n - summary\n - reset\n - history\n - help\n - exit")
    else:
        print(Fore.RED + "Unknown command. Type 'help' to see available options.")

def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if re.match(r'^[A-Za-z]+$', name):
            return name
        print("❗ Name must contain only letters. Try again.")

def save_summary(name):
    filename = f"{name}_sentiment_analysis.txt"
    with open(filename, "w") as file:
        file.write(f"Sentiment Analysis Summary for {name}\n")
        file.write("-" * 40 + "\n")
        for k, v in sentiment_counts.items():
            file.write(f"{k.capitalize()}: {v}\n")
        file.write("\nFull History:\n")
        for i, (msg, sentiment, score) in enumerate(history, 1):
            file.write(f"{i}. [{sentiment} | {score:.2f}] → {msg}\n")
    print(Fore.GREEN + f"📄 Summary saved to {filename}")

def main():
    print(Fore.CYAN + "🤖 Welcome to the Spy-Themed AI Sentiment Analyzer!")
    username = get_valid_name()
    print(f"Hi {username}, type any sentence to analyze its sentiment.")
    print("You can also use commands like summary, reset, history, help, or type 'exit' to quit.\n")

    while True:
        user_input = input("🗨️ Your input: ").strip()
        if user_input.lower() == "exit":
            print("\n👋 Exiting... Here’s your final report:")
            execute_command("summary")
            save_summary(username)
            break
        elif user_input.lower() in ["summary", "reset", "history", "help"]:
            execute_command(user_input.lower())
        else:
            show_processing_animation()
            analyze_sentiment(user_input)

if __name__ == "__main__":
    main()
