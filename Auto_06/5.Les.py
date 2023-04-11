
class Dog:
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self. color = color

    def run(self):
        return 'I can run'

    def get_name(self):
        return f"Hello! My name is {self.name}"


dog1 = Dog('Bobik', 3, "brown")
print(dog1.get_name())
print(dog1.name)

