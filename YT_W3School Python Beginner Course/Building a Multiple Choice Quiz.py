from Questions_BMCQ import Question

question_prompts = [
    "What Colours are Apples \n (a) Red/Green\n (b) Green\n (c) Magenta\n\n",
    "What Colours are Bananas \n (a) Teal\n (b) White\n (c) Yellow",
    "What Colours are Strawberries \n (a)Maroon\n (b) Red\n (c) Brown\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def qa_user (questions):
    score = 0
    for question in questions:
        score = 0
        answer = input(question_prompts)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")

qa_user(questions)
