class person:
    def __init__(self):
        self.name=input("Enter the name:")
        self.age=int(input("Enter Age:"))
    def print_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
p1=person()
p2=person()
p1.print_details()
p2.print_details()
