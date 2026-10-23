from dc import Justice_League

dc_q = [
    "Q1: Who has an under water city ?\n A: Aquaman\n B: Niomi\n C: Johnny Depp\n",
    "Q2: Is Batman part of the Avengers team?\n A: Yes\n B: Part Timer\n C: No\n",
    "Q3: What does JL mean?\n A: Just Like\n B: Jel Leer\n C: Justice League\n"
]

dc_a = [
    Justice_League(dc_q[0], "A"),
    Justice_League(dc_q[1], "B"),
    Justice_League(dc_q[2], "C")
]

def quiz(dc):
    score = 0
    for q in dc:
        answer = input(f"Answer: {q.question}")
        if answer.upper() == q.answer:
            score += 1
    print(f"Well Done! You have scored {score}/{len(dc)}")

quiz(dc_a)