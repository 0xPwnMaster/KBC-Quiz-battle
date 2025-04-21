questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic", "B) Indian", "C) Pacific", "D) Arctic"],
        "answer": "C"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A) H2O", "B) CO2", "C) NaCl", "D) O2"],
        "answer": "A"
    },
    {
        "question": "Which country is known for inventing pizza?",
        "options": ["A) France", "B) Mexico", "C) Italy", "D) Greece"],
        "answer": "C"
    },
    {
        "question": "Which language is the most spoken worldwide?",
        "options": ["A) English", "B) Hindi", "C) Spanish", "D) Mandarin"],
        "answer": "D"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A) Vincent Van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Claude Monet"],
        "answer": "C"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
        "answer": "C"
    },
    {
        "question": "Which animal is known as the King of the Jungle?",
        "options": ["A) Tiger", "B) Lion", "C) Elephant", "D) Gorilla"],
        "answer": "B"
    }
]
def answer_sheet():
    for Q in questions:  
        for option in Q["options"]:       
            if Q["answer"] == option[0]:    
                print(Q["question"], "\n", option)

