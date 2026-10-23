from marvel import Avengers

avengers_qs = [
    "Q1: Who is Iron Man?\n A: Tony Stark\n B: Bruce Wayne\n C: Alfred Pennyworth\n",
    "Q2: Is Black Widow part of the Avengers team?\n A: Yes\n B: No\n C: Part Timer\n",
    "Q3: What team is Captain America on?\n A: Avengers\n B: Hydra\n C:S.H.I.E.L.D"
]

avengers_as = [
    Avengers(avengers_qs[0], "A"),
    Avengers(avengers_qs[1], "A"),
    Avengers(avengers_qs[2], "A")
]

def quiz(avengers_quiz):
    score = 0
    for q in avengers_quiz:
        answer = input(f"Answer: {q.question}")
        if answer.upper() == q.answer:
            score += 1
    print(f"Correct! you have {score}/{len(avengers_quiz)}")

quiz(avengers_as)