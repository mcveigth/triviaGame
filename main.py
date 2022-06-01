if __name__ == '__main__':
    import game
    print("Welcome!\n this is a ")
    numberOfQuestions = 4
    trivia = game.Game(numberOfQuestions)
    triviaApi = game.requests.get("https://opentdb.com/api.php", params=trivia.set_parameters())
    #while True:
    for i in range(numberOfQuestions):
        num = game.Question(i, triviaApi)
        num.shuffle()
        trivia.questions = num
        print(num.question)
        trivia.display()
        print(f"debug purposes: {num.answer}")
        answer = input("answer: ")
        num.check(answer)
