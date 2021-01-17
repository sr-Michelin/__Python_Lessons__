import sys

sys.path.append('E:\\DOCK\\Python_M\\vеnv\\+LESSONS\\+BASE+\\UNITTEST\\II (classes)')
from survey import Anon_survey

# задавання запитання
question = 'What language is your first spoken?'
my_surv = Anon_survey(question)

# вивід запитання і збереження відповідей
my_surv.show_question()
print('Enter "q" to quit\n')
while True:
    responce = input('Language: ')
    if responce == 'q':
        print('End of the program...')
        break
    my_surv.store_response(responce)

# вивід результатів опитування
print('_____________________________________________________')
print('Thank you to everyone who participated in the survey!')
my_surv.show_result()