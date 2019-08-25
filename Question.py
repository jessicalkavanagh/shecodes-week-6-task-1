class Survey_Question: 
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Last_Survey_Question: 
    def __init__(self, prompt, last_answer):
        self.prompt = prompt
        self.last_answer = last_answer

class Eligble_Questions: 
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


class Last_Eligble_Question: 
    def __init__(self, prompt, eligble_answer):
        self.prompt = prompt
        self.eligble_answer = eligble_answer