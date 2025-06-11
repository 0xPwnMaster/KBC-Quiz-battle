import json
from colorama import Fore, Style, init
import shutil

filePath = "KBC Model2 👍\question.json"

# File Handling
try:
    with open(filePath, 'r') as f:
        dataset = json.load(f)
except FileNotFoundError:
    print("File not Found")
except Exception as e:
    print(e)

cookies = 0
questions_count = 0
incorrect_count = 0

yes_responses = ["y", "yes", "yeah", "yup", "sure", "ok", "okay"]
no_responses = ["n", "no", "nope", "nah"]

def level_progression(questions_count, incorrect_count, cookies):
    continue_game = True
    if questions_count == 25:
        print(Fore.GREEN + Style.BRIGHT + f"\n🎉 Beginner Level Complete! You answered {questions_count - incorrect_count} correctly out of 25." + Style.RESET_ALL)
        if incorrect_count >= 20:
            print(Fore.YELLOW + Style.BRIGHT + "⚠️ That was close! You had many incorrect attempts." + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + f"You now have {cookies} cookies 🍪" + Style.RESET_ALL)
        print(Fore.MAGENTA + Style.BRIGHT + "Get ready to level up to the Pro Level 🔥" + Style.RESET_ALL)
        continue_game = ask_to_continue()

    elif questions_count == 50:
        print(Fore.GREEN + Style.BRIGHT + f"\n🚀 Pro Level Complete! You got {questions_count - incorrect_count} right out of 50." + Style.RESET_ALL)
        if incorrect_count >= 40:
            print(Fore.YELLOW + Style.BRIGHT + "⚠️ Heavy on the mistakes, but you made it through." + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + f"Total Cookies Collected: {cookies} 🍪" + Style.RESET_ALL)
        print(Fore.MAGENTA + Style.BRIGHT + "Next up... the final challenge: Hacker Level 💻⚔️" + Style.RESET_ALL)
        continue_game = ask_to_continue()

    elif questions_count == 75 and incorrect_count == 0:
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"\n🧠 Insane performance! You've conquered the Hacker Level with {cookies} cookies!" + Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "You're officially a Code Wizard 👑" + Style.RESET_ALL)
        continue_game = ask_to_continue()
    elif questions_count == 75:
        print(Fore.GREEN + Style.BRIGHT + f"\n🔥 Hacker Level Completed! You got {questions_count - incorrect_count} correct out of 75." + Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Still impressive! 🏆" + Style.RESET_ALL)
        continue_game = ask_to_continue()

    return continue_game

def ask_to_continue():
    response = input(Fore.LIGHTBLUE_EX + Style.BRIGHT + "Would you like to continue to the next level? [y/n]: " + Style.RESET_ALL).lower().strip()
    if response in yes_responses:
        return True
    elif response in no_responses:
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Thanks for playing! See you next time! 😊" + Style.RESET_ALL)
        return False
    else:
        print(Fore.YELLOW + "Invalid input, please enter 'y' or 'n'." + Style.RESET_ALL)
        return ask_to_continue()

def playing():
    global cookies
    global questions_count
    global incorrect_count

    columns = shutil.get_terminal_size().columns
    print(Fore.BLUE + Style.BRIGHT + "\n\n" + "⋆✨ WELCOME TO KBC! ✨⋆\n\n".center(columns))
    print(Fore.CYAN + Style.BRIGHT + "════ There are Different Levels of Difficulties ════".center(columns))
    print(
        Fore.GREEN + Style.BRIGHT + "Beginner".ljust(20) +
        Fore.YELLOW + Style.BRIGHT + "Pro".ljust(20) +
        Fore.RED + Style.BRIGHT + "Hacker"
    )
    user_input = input(Fore.LIGHTRED_EX + Style.BRIGHT + "Choose Level of difficulty: ").lower().strip()
    
    if user_input not in dataset:
        print(Fore.RED + Style.BRIGHT + "Invalid difficulty! Please choose Beginner, Pro, or Hacker." + Style.RESET_ALL)
        return True 

    level_question = dataset[user_input]

    for items in level_question:
        level_Q = items['question']
        level_opt = items['options']
        level_ans = items['answer']

        correct_answer = next((opt for opt in level_opt if opt.startswith(level_ans[0])), None)

        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + f"\nQuestions: {level_Q}\n" + Style.RESET_ALL)
        questions_count += 1

        for opt in level_opt:
            print(opt)

        user_answer = input("Enter Your Answer: ").strip().lower()
        print(f"You answered: {user_answer}")

        if user_answer and user_answer == correct_answer.lower().strip():
            cookies += 1
            print(Fore.GREEN + Style.BRIGHT + f"That's Correct, now you earned total {cookies} cookie(s) ;)\n No. of question attempts: {questions_count}" + Style.RESET_ALL)
        else:
            incorrect_count += 1
            print(Fore.RED + Style.BRIGHT + f"Better luck next time, The answer was: {correct_answer}\n No. of question attempts: {questions_count}" + Style.RESET_ALL)

        if not level_progression(questions_count, incorrect_count, cookies):
            return False  

    return True  

def main():
    init()
    asking = input("Do you wanna test your IQ [y/n]: ").lower().strip()
    if asking in yes_responses:
        while True:
            if not playing():
                break
    else:
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "No worries! Come back anytime when you're ready to challenge yourself 😊" + Style.RESET_ALL)

if __name__ == "__main__":
    main()