class ProgrammingLanguage:

    def __init__(self, language = "", typing = "", reflection = bool(), year = int()):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.language}, {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}"

    def is_dynamic(self, typing):
        if typing == "Dynamic":
            return True
        elif typing == "Static":
            return False

    def dynamic_languages(self, list_store):
        lan = []
        for language in list_store:
            if self.is_dynamic(language[1]):
                 lan.append(language[0])

        return lan

