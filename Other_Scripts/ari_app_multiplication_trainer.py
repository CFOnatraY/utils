def multiplication_training():
    name = input('What is your name?\n')
    print('Hi ' + name)

    favorite_color = input('What is your favorite color?\n')
    print(name + ' likes ' + favorite_color)

    number1 = input('Add a number 1:\n')
    number2 = input('Add a number 2:\n')
    user_answer = int(input('How many is ' + number1 + ' * ' + number2 + '?\n'))
    correct_answer = int(number1) * int(number2)
    is_correct = user_answer == correct_answer

    while not is_correct:
        print('Something is WRONG with your answer. Please, try again.')
        user_answer = int(input('Again, How many is ' + number1 + ' * ' + number2 + '?\n'))
        is_correct = user_answer == correct_answer

    print('¡CONGRATULATIONS! Your answer is RIGHT, is ' + str(user_answer) + ".")


multiplication_training()