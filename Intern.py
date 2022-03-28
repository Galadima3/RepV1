class HIIT:
    def __init__(self, name, Level, University, Specialization):
        self.name = name
        self.Level = Level
        self.Specialization = Specialization
        self.University = University

    
    def attendsLecture(self):
        print(f"{self.name} attends {self.Specialization} Lectures")

    def attendsWebinar(self):
        print(f"{self.name} attends Webinars")

    def fillsLogbook(self):
        print(f"{self.name} fills LogBook regularly")

    def interact(self):
        print(f"{self.name} interacts with other Interns")

    def fullDetails(self):
        print(f"Intern Full Details:\nName: {self.name}\nLevel: {self.Level}\nUniversity: {self.University}\nSpecialization: {self.Specialization}")

Name = input("Enter your Name: ")
Level = int(input("Enter your Level >> "))
University = input("What University do you attend? ")
specialization = input("What is your Area of Specialization? ")

Intern = HIIT(Name, Level, University, specialization)



Intern.attendsLecture()
Intern.attendsWebinar()
Intern.fillsLogbook()
Intern.interact()
print("\n")
Intern.fullDetails()
