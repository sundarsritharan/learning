import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """ test for the class AnonymousSurvey"""

    def setUp(self):
        """set up the survey and add some responses to be used across the class"""
        question = "What language did you first learn?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Tamil','Telugu']
        

    
    def test_store_single_response(self):
        """test that a single response is stored successfully"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_multiple_responses(self):
        """tets that multiple responses can be stored successfully"""
        for my_response in self.responses:
            self.my_survey.store_response(my_response)
        for respone in self.responses:
            self.assertIn(respone,self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()