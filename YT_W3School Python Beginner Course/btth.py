from btth_qa import Btth_questions

btth_qs = [
    "Q1. what donghua is Xiao Yan from:\nA: Soul Land \nB: Battle Through The Heavens \nC: Demon Hunter",
    "Q2. who is Gu Xun'er to Xiao Yan in the end:\nA: Wife \nB: Enemy \nC: Sister",
    "Q3. who was sealed inside Xiao Yan's ring:\nAa: Queen Medusa \nB: It Was a Fake Ring \nC: Yao Lao",
    "Q4. where did Xiao Yan and Yun Yun/Yun Zhi first meet:\nA: Yan Clan \nB: Magic Beast Mountain Range \nC: Banquet",
    "Q5. What is the name of Queen Medusa's Daughter:\nA: Cai Lin \nB:  Xiao Xiao \nC: Xiao Gu"
]

btth_answers = [
    Btth_questions(btth_qs[0], "B"),
    Btth_questions(btth_qs[1], "A"),
    Btth_questions(btth_qs[2], "C"),
    Btth_questions(btth_qs[3], "B"),
    Btth_questions(btth_qs[4], "B")
]

def quiz(Btth_questions):
    scores = 0
    for btth_answers in Btth_questions:
        answers =  input("Answer: " + btth_answers)
    if answers == btth_answers:
        scores += 1
        print(f"Correct! you have got {scores}/{len(btth_answers)}.")

quiz(Btth_questions)
