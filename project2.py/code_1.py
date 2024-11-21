import time
import random
import ast


questions = "questions.txt"
user_file = "users.txt"
Login_details = "logins.txt"
result= "results.txt"


def load_questions(category):
    with open(questions, "r") as file:
        content = file.read().strip()
       
        if content.startswith("questions ="):
            content = content[len("questions ="):].strip()
        questions_data = ast.literal_eval(content)  
        return questions_data.get(category, [])


def save_user(fullname, phone_number, username, password):
    with open(user_file, "a") as file:
        file.write(f"{fullname}|{phone_number}|{username}|{password}\n")


def verify_user(username, password):
    with open(user_file, "r") as file:
        for line in file:
            data = line.strip().split("|")
            if data[2] == username and data[3] == password:
                return True
    return False


def log_login(username, status):
    with open(Login_details, "a") as file:
        file.write(f"{time.ctime()}|{username}|{'Success' if status else 'Failure'}\n")


def save_result(username, score):
    with open(result, "a") as file:
        file.write(f"{time.ctime()}|{username}|{score}\n")


print("Welcome to the quiz")
time.sleep(2)
print("You are directing to the registration page")
time.sleep(2)

fullname = input("Enter your full name: ")
phone_number = input("Enter your phone number: ")
username = input("Enter your username: ")
password = input("Enter your password: ")


save_user(fullname, phone_number, username, password)

time.sleep(2)
print("You are directing to the login page")

login_username = input("Enter your username: ")
login_password = input("Enter your password: ")

if verify_user(login_username, login_password):
    log_login(login_username, True)
    print("Login successful!")
    
   
    print("Choose a category: General Knowledge, Technology, Sports")
    category = input("Enter category: ").strip()
    questions = load_questions(category)

    if not questions:
        print("No questions available for this category.")
    else:
        score = 0
        for question_data in random.sample(questions, min(5, len(questions))):  # Ask 5 random questions
            print(f"\n{question_data['question']}")
            for idx, option in enumerate(question_data["options"], start=1):
                print(f"{chr(idx + 64)}) {option}")
            answer = input("Your answer: ").strip().upper()
            if answer == question_data["answer"]:
                score += 1
                print("Correct!")
            else:
                print(f"Wrong! The correct answer was {question_data['answer']}.")

        print(f"\nQuiz completed. Your score: {score}/{len(questions)}")
        save_result(login_username, score)

else:
    log_login(login_username, False)
    print("Login failed. Incorrect username or password.")
