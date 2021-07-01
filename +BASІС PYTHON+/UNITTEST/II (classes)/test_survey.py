import sys
import unittest

sys.path.append('E:\\DOCK\\Python_M\\vеnv\\+LESSONS\\+BASE+\\UNITTEST\\II (classes)')
from survey import Anon_survey


# Перевірка на правильність збереження відповіддей через assertIn()

class Test_Anon_survey(unittest.TestCase):
    def test_store_single_rsp(self):
        """Перевірка правильності збереження одної відповідді"""
        question = 'What language is your first spoken?'
        my_surv = Anon_survey(question)
        my_surv.store_response('English')
        self.assertIn('English', my_surv.responses)

    def test_store_three_rsp(self):
        """Перевірка правильності збереження трьох відповіддей"""
        question = 'What language is your first spoken?'
        my_surv = Anon_survey(question)
        responses = ['English', 'Ukranian', 'Russian']  # Список трьох мов -  відповіддей на запитання question
        for response in responses:
            my_surv.store_response(response)

        for response in responses:
            self.assertIn(response, my_surv.responses)


if __name__ == '__main__':
    unittest.main()
