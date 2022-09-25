

class ProgrammingLanguage:
    '''Show information of the program language '''
    def __init__(self,field,typing,reflection,year):
        self.name = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"







