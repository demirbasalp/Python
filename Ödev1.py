def multiplication_table_practice():
    number_to_practice = int(input("Enter the number you want to practice (1-10): "))
    correct_answers = 0
    for i in range(1, 11):
        user_answer = int(input(f"What is {i} x {number_to_practice}? "))

        if user_answer == i * number_to_practice:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong. The correct answer is {i * number_to_practice}.")

    accuracy = (correct_answers / 10) * 100
    print(f"\nYou got {correct_answers} out of 10 correct. Accuracy: {accuracy}%")

multiplication_table_practice()

