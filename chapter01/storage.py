# An example of a storage class

class StudentRecord:

    def __init__(self):
        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0
    
    def __repr__(self):
        return f"StudentRecord(firstName={self.firstName}, lastName={self.lastName})"


if __name__ == "__main__":
    a_student = StudentRecord()
    a_student.idNum = 1234
    a_student.firstName = "John"
    a_student.lastName = "Smith"
    a_student.classCode = 1
    a_student.gpa = 3.5
    print(a_student)

    b_student = StudentRecord()
    b_student.idNum = 4321
    b_student.firstName = "Jane"
    b_student.lastName = "Roberts"
    b_student.classCode = 4
    b_student.gpa = 4.0
    print(b_student)