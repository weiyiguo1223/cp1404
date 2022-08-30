class ProgrammingLanguage:
    def __int__(self,field,typing,reflection,year):
        self.name = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"


