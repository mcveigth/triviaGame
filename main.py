if __name__ == '__main__':
    import game

    print("Welcome!\nto this trivia game!")
    numberOfQuestions = 10
    playerScore = 0
    trivia = game.Game(numberOfQuestions)
    triviaApi = game.requests.get("https://opentdb.com/api.php", params=trivia.set_parameters())

    for i in range(numberOfQuestions):
        num = game.Question(i, triviaApi)
        num.shuffle()
        trivia.questions = num
        print(num.question)
        trivia.display()
        print(f"debug purposes: {num.answer}")  # debug purposes
        answer = input("answer: ")
        # check if the answer is correct
        if num.check(answer) is True:
            playerScore += 1
    print(f'you got {playerScore} out of {numberOfQuestions}')
