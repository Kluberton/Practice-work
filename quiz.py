from question import question

question_prompts = [
    "How far to the Ridgeline?\n(a) 1 mile\n(b) 3 feet\n(c) Forever\n(d) Doesn't matter how far\n\n",
    "How long does it take to get to the Ridgeline?\n(a) Forever\n(b) A blink\n(c) What is time?\n\n",
    "How many sharp things are at the Ridgeline?\n(a) All of them\n(b) 5\n(c) None, all dull\n\n"
]

questions = [
    question(question_prompts[0], "d"),
    question(question_prompts[1], "c"),
    question(question_prompts[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + " out of " + str(len(questions)) + " questions correct.")

run_test(questions)
