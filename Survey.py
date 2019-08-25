from Question import Survey_Question, Eligble_Questions, Last_Survey_Question, Last_Eligble_Question

survey_question_prompt = [
    "Hi, are you part of the SheCodes Plus Program?\n(a) Yes\n(b) No\n\n", 
    "Did you attend Wednesday's class?\n(a) Yes\n(b) No\n\n",
    "Did you attend Saturday's class?\n(a) Yes\n(b) No\n\n",
]


survey_questions = [
    Survey_Question(survey_question_prompt[0], "a"),
    Survey_Question(survey_question_prompt[1], "a"),
]

def run_test(survey_questions):
    for question in survey_questions:
        answer = input(question.prompt)
        if answer == question.answer :
            print("Next question:")
        else: 
            print("Sorry, you are not eligble to complete this survey.")
            stop = True
            exit()


run_test(survey_questions)


last_survey_question_prompt = [
    "Did you attend Saturday's class?\n(a) Yes\n(b) No\n\n",
]

last_survey_questions = [
    Last_Survey_Question(last_survey_question_prompt[0], "a"),
]

def run_test(last_survey_questions):
    for question in last_survey_questions:
        last_answer = input(question.prompt)
        if last_answer == question.last_answer :
            print("Great, you are eligble to complete this survey.\n")
        else: 
            print("Sorry, you are not eligble to complete this survey.\n")
            stop = True
            exit()

run_test(last_survey_questions)


eligble_questions_prompt = [
    "How did you find Wednesday class?\n(a) I loved it!\n(b) I was ok with it\n(c) I was tired and did not want to be there\n\n", 
    "How did you find Saturday class?\n(a) I loved it!\n(b) I was ok with it\n(c) I was tired and did not want to be there\n\n",
]


eligble_questions = [
    Eligble_Questions(eligble_questions_prompt[0], "a"),
    Eligble_Questions(eligble_questions_prompt[1], "a"),
]


def run_test(eligble_questions):
    for question in eligble_questions:
        answer = input(question.prompt)
        if answer == question.answer :
            print("Next question:")
        else: 
            print("Shame! Please talk to LJ if you're having issues!")
            stop = True
            exit()

run_test(eligble_questions)



last_eligble_questions_prompt = [
    "Do you like the mentors?\n(a) Yes\n(b) No\n\n",
]


last_eligble_questions = [
    Last_Eligble_Question(last_eligble_questions_prompt[0], "a"),
]


def run_test(last_eligble_questions):
    for question in last_eligble_questions:
        eligble_answer = input(question.prompt)
        if eligble_answer == question.eligble_answer:
            print("Thank you for answering the questions. Good to hear that you are loving the course so far!")
            exit()
        else: 
            print("Shame! Please talk to LJ if you're having issues!")
            stop = True
            exit()

run_test(last_eligble_questions)