from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(f"{python} \n")

programming_language = ProgrammingLanguage()
dynamic_languages = programming_language.dynamic_languages([["Java", "Static", True, 1995], ["C++", "Static", False, 1983], ["Python", "Dynamic", True, 1991], ["Visual Basic", "Static", False, 1991], ["Ruby", "Dynamic", True, 1995]])

print("The dynamically typed languages are:")
for language in dynamic_languages:
    print(language)