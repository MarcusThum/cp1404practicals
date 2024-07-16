class Project:
    def __init__(self, name, start, priority, estimate, completion):
        self.name = name
        self.start = start
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __str__(self):
        return f"{self.name}, start: {self.start}, priority: {self.priority}, estimate: {self.estimate}, completion: {self.completion}"