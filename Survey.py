from Question import Survey_Question
from Eligible_Questions import Eligible_Questions
from Last_Survey_Question import Last_Survey_Question
from Section_2_Question import Section_2_Question

survey_question_prompt = [
    "Hi, are you part of the SheCodes Plus Program?\n(a) Yes\n(b) No\n\n", 
    "Did you attend Wednesday's class?\n(a) Yes\n(b) No\n\n",
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
            print("Yay! you are eligible to complete this survey.\n------------Classes------------")
        else: 
            print("Sorry, you are not eligible to complete this survey.\n")
            stop = True
            exit()

run_test(last_survey_questions)


eligible_questions_prompt = [
    "How did you find Wednesday class?\n(a) I loved it!\n(b) I was ok with it\n(c) I was tired and did not want to be there\n\n", 
    "How did you find Saturday class?\n(a) I loved it!\n(b) I was ok with it\n(c) I was tired and did not want to be there\n\n",
    "Are the classes too long?\n(a) Yes\n(b) No\n\n",
]


eligible_questions = [
    Eligible_Questions(eligible_questions_prompt[0], "a"),
    Eligible_Questions(eligible_questions_prompt[1], "a"),
    Eligible_Questions(eligible_questions_prompt[2], "b"),
]


def run_test(eligible_questions):
    for question in eligible_questions:
        answer = input(question.prompt)
        if answer == question.answer :
            print("Next question:")
        else: 
            print("Shame! Please talk to LJ if you're having issues!")

run_test(eligible_questions)



section_2_questions_prompt = [
    "------------Program------------\nDo you like the program?\n(a) Yes\n(b) No\n\n",
    "Do you like the mentors?\n(a) Yes\n(b) No\n\n",
    "Do you like the girls in the class?\n(a) Yes\n(b) No\n\n",
]


section_2_questions = [
    Section_2_Question(section_2_questions_prompt[0], "a"),
    Section_2_Question(section_2_questions_prompt[1], "a"),
    Section_2_Question(section_2_questions_prompt[2], "a"),
]


def run_test(section_2_questions):
    for question in section_2_questions:
        section_answer = input(question.prompt)
        if section_answer == question.section_answer:
            print("Next question:")
        else: 
            print("Thank you for answering the questions honestly. Please talk to LJ if you're having issues.")

run_test(section_2_questions)



last_survey_question_prompt = [
    "------------Final question------------\nWill you recommend this program to your peers?\n(a) Yes\n(b) No\n\n",
]

last_survey_questions = [
    Last_Survey_Question(last_survey_question_prompt[0], "a"),
]

def run_test(last_survey_questions):
    for question in last_survey_questions:
        last_answer = input(question.prompt)
        if last_answer == question.last_answer :
            print("Yay! Glad to hear that you are enjoying the program so far! Thank you for completing the survey.\n------------Finished------------")
            exit()
        else: 
            print("Thank you for completing the survey. Sorry to hear that you are not loving the program so far. Again, please talk to LJ if you're having issues.\n------------Finished------------")
            stop = True
            exit()

run_test(last_survey_questions)
