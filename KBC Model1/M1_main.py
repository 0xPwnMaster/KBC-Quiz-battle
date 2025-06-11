from question import answer_sheet

print("Welcome to KBC")
running = False
cookies = 0
wanna_play = input("You wanna Play this Game [y/n]: ").strip().lower()
  
yes_responses = ["y", "yes", "yeah", "yup", "sure", "ok", "okay"]

def main():
    global cookies
    answers = [
        "Paris",
        "Mars",
        "William Shakespeare",
        "Pacific",
        "H2O",
        "Italy",
        "Mandarin",
        "Leonardo da Vinci",
        "2",
        "Lion",
        "A",
        "B",
        "B",
        "C",
        "A",
        "C",
        "D",
        "C",
        "C",
        "B"
    ]
    questions = [
        "What is the capital of France?: ",
        "Which planet is known as the Red Planet?",
        "Who wrote the play 'Romeo and Juliet'?",
        "What is the largest ocean on Earth?",
        "What is the chemical symbol for water?",
        "Which country is known for inventing pizza?",
        "Which language is the most spoken worldwide?",
        "Who painted the Mona Lisa?",
        "What is the smallest prime number?",
        "Which animal is known as the King of the Jungle?"
    ]

    for ans, Q in zip(answers, questions) :
        user_input = input(Q + " " ).lower().strip()
        
        if user_input == ans.lower():
            cookies += 1
            print(f"That's correct!\nYou now have {cookies} cookie(s) 🍪\n")
        else:
            print(f"Better luck next time! The correct answer was: {ans}\n")
    
    print(f"Game is Over! you have earned total {cookies} no. of cookies")
    view_answer_sheet()


# Asking if user wants to view answer  
def view_answer_sheet():
    user_input = input("Are you intrested in seeing answer sheet [y/n]: ").lower().strip()
    if user_input in yes_responses:
        answer_sheet()
    else:
        print("Thanks for playing! 🎉")
        return


# Checking wether user wanna play this game while also checking variation of yes input
if __name__ == "__main__":
    if wanna_play in yes_responses:
        print("🎮 Main game is running... Let's play! 🚀")
        main()
    else:
        print("No worries! Come back anytime when you're ready to challenge yourself 😊")