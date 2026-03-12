def quiz_by_aki(questions):
    score = 0
    counter_false_answers = 0
    counter_true_answers = 0
    for i, j in questions.items():
        print(i)
        ans = input("Введите свой ответ: ")
        if ans == j:
            print("К вам прибавляется 20 очков!")
            score += 100 / len(questions)
            counter_true_answers += 1
        else:
            print("Неверный ответ!")
            counter_false_answers += 1
    print("*********** Вы получили", score, "очков ***********")
    print("*********** Правильных ответов:", counter_true_answers, "из", len(questions), "***********")
    print("*********** Неправильных ответов:", counter_false_answers, "из", len(questions), "***********")
    print("*********** Процент правильных ответов", f"{score}%", "***********")
    if score >= 80:
        print("Да вы Эйнштейн! Хорошего вечера!")
    else:
        print("Не очень! В следующий раз, приходите с новыми силами!")

def check(ans_to_start_quiz):
    if ans_to_start_quiz == "Да" or ans_to_start_quiz == "да" or ans_to_start_quiz == "Yes" or ans_to_start_quiz == "yes":
        return True
    else:
        return False
print("Привет! Готовы к quiz?")
ans_to_start_quiz = input()
if check(ans_to_start_quiz) == False:
    print("Увидимся в следующий раз!")
    exit()
questions = {
    "999 в степени 0. Сколько?": "1",
    "Столица Люксембурга?": "Люксембург",
    "6 + 67 + 67 + 7": "147",
    "Вышел зайчик на крыльцо... Продолжи.": "Почесать свое яйцо",
    "HTML - это язык?": "Нет"
}
quiz_by_aki(questions)


