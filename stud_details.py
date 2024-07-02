class Student:
    def __init__(self, n, r, m1, m2, m3):
        self.name = n
        self.reg = r
        self.mark1 = float(m1)
        self.mark2 = float(m2)
        self.mark3 = float(m3)

    def avg(self):
        return (self.mark1 + self.mark2 + self.mark3) / 3

    def __str__(self):
        return f"Name: {self.name}, Reg: {self.reg}, Mark1: {self.mark1}, Mark2: {self.mark2}, Mark3: {self.mark3}, Avg: {self.avg():.2f}"

stud = {}
num = int(input("Enter number of students: "))
for i in range(num):
    n = input("Enter Name: ")
    r = input("Enter Reg: ")
    m1 = float(input("Enter M1: "))
    m2 = float(input("Enter M2: "))
    m3 = float(input("Enter M3: "))
    st = Student(n, r, m1, m2, m3)
    stud[r] = st

for reg, student in stud.items():
    print(student)

