class Employee:
    def __init__(self, name, surname):
     self.name = name
     self.surname = surname

    def work(self):
        return "I can work"

    def coding(self):
        return 'I can coding'

    def get_language(self):
        return f'My language is {self.language}'
