if __name__ == '__main__':
    import game
    print("Welcome!\nto this trivia game!")
    numberOfQuestions = 2
    playerScore = 0
    trivia = game.Game(numberOfQuestions)
    triviaApi = game.requests.get("https://opentdb.com/api.php", params=trivia.set_parameters())

    for i in range(numberOfQuestions):
        num = game.Question(i, triviaApi)
        num.shuffle()
        trivia.questions = num
        print(num.question)
        trivia.display()
        print(f"debug purposes: {num.answer}")
        answer = input("answer: ")
        if num.check(answer) is True:
            playerScore += 1
    print(playerScore)
