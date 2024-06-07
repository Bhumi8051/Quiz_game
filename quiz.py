from urllib import response
import requests
import random

print("Welcome to my Computer quiz!")
name = input ("Enter your name :")
print(name)
playing=input("Do you want to play?  ")
if playing.lower() != "yes":
    quit()

print("Please answer the following questions correctly to pass the quiz.")
print("Good luck!")

print()

score=0

#func to fetch questions from api
def fetch_questions(category,difficulty='medium',num_questions=20):
    url = f'https://opentdb.com/api.php?amount={num_questions}&category={category}&difficulty={difficulty}&type=multiple'
    response = requests.get(url)
            #above line sends http get requests to the constructed url using request.get function from request liberary and ans response me save hoga 
    if response.status_code!= 200:
        raise Exception("Error fetching questions")
    data = response.json()
    return data['results']


#func to ask questions
def ask_questions(topic,questions):
    score = 0
    print(f"\n --{topic}Quiz--\n")
    for index, question_data in enumerate(questions,1):
        
        question = question_data['question']
        correct_answer = question_data['correct_answer']
        options =question_data['incorrect_answers']+[correct_answer]
        random.shuffle(options)
        
        #display the questions and options  
        print(f"question {index}: {question}")
        for i, option in enumerate(options, 1):
            print(f"{i}.{option}")
        
        """ ans ko loop ke andar lana hoga then vo har ek question ke bad input le gi 
        try block convert the users input to an index and checks the corresponding ans
        except handle errors"""
        
        #user's ans after each question, kyuki loop structure me change kiya he it is now inside the questions loop 
        ans = input("Your answer (enter the number):")
        try:
                ans_index = int(ans) - 1
                if options[ans_index].lower() == correct_answer.lower():
                    print("Correct!")
                    score += 1
                else:
                    print("Wrong!")
        except (ValueError, IndexError):
                print("Invalid answer. Skipping question.")
    # display total score after all ques 
    print(f"\nYour total score for {topic} quiz is: {score} out of {len(questions)}")

#now finally the main function 
def main():
    print("choose a category:")
    print("1. General Knowledge")
    print("2. Science & Nature")
    print("3. Science: Computers")
    
    
    category_choice = input("enter the number of your choice: ")
    category_map = {
        '1':'9',
        '2':'17',
        '3':'18'
    }

    category = category_map.get(category_choice)
    if not category:
        print("Invalid choice. Exiting.")
        return

    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    if difficulty not in ['easy', 'medium', 'hard']:
        difficulty = 'medium'  # Default to medium if invalid choice

    questions = fetch_questions(category, difficulty)
    topic_names = {
        '9': 'General Knowledge',
        '17': 'Science & Nature',
        '18': 'Science: Computers',
        # Add more mappings as needed
    }
    ask_questions(topic_names[category], questions)

if __name__ == "__main__":
    main()

print("congratulations on completing the quiz")

