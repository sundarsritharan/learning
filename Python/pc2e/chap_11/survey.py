class AnonymousSurvey:
    """ Collect anonymous answer to a survey question. """

    def __init__(self,question):
        """store question, and prepare to store responses"""
        self.question = question
        self.responses = []

    def show_question(self):
        """show the survey question"""
        print(self.question)
    
    def store_response(self,new_response):
        """store a single response for the survey"""
        self.responses.append(new_response)

    def show_results(self):
        """show all responses that has been given """
        print("Survey results:")
        for response in self.responses:
            print(f" - {response}")