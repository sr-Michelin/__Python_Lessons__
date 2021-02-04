import sys
import unittest

sys.path.append('E:\\DOCK\\Python_M\\vеnv\\+LESSONS\\+BASE+\\UNITTEST\\II (classes)')
from survey import Anon_survey


# Метод setUp() вирішує два завдання: створює запитання і задає відповідді для тестування
# Кожен із цих атрибутів забезпечується префікс self, тому він може вживатися де завгодно в класі.
# Ця обставина спрощує два тестових методу, тому що їм вже не потрібно створювати екземпляр опитування або відповіді.


# Перевірка на правильність збереження відповіддей через assertIn()


class Test_Anon_survey(unittest.TestCase):
    def setUp(self):
        """Створення опиту і набору відповіддей для всіх тестових методів"""
        question = 'What language is your first spoken?'
        self.my_surv = Anon_survey(question)
        self.responses = ['English', 'Ukrainian', 'Russian']

    def test_store_single_rsp(self):
        """Перевірка правильності збереження одної відповідді"""
        self.my_surv.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_surv.responses)

    def test_store_three_rsp(self):
        """Перевірка правильності збереження трьох відповіддей"""
        for response in self.responses:
            self.my_surv.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_surv.responses)


if __name__ == '__main__':
    unittest.main()
