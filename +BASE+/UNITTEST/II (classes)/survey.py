class Anon_survey():
    '''Анонімний збір відповіддей на поствленні запитання'''

    def __init__(self, question):
        '''Зберігає питання і гоговиться до збереження відповіддей'''
        self.question = question
        self.responses = []

    def show_question(self):
        '''Вивід запитання'''
        print(self.question)

    def store_response(self, new_responses):
        '''Зберігає одну відповідь на запитання'''
        self.responses.append(new_responses)

    def show_result(self):
        '''Виводить всі відповідді'''
        print('Survey results: ')
        for response in self.responses:
            print(f'- {response}')
