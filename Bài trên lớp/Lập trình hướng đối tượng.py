class Student:
    def __init__(self, name, age, lop):
        self.name = name
        self.age = age
        self.lop_hoc = lop
    def say_hello(self):
        print(f"Xin chào, tôi tên là {self.name}, năm nay {self.age}")
    def info(self):
        print(f"Thông tin của sinh viên {self.name}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Class: {self.lop_hoc}")
        if self.age < 0:
            print("Lỗi")
class Study(Student):
    def study(self):
        print(f"{self.name} đang học Python")

tuan_dung = Study("Nguyễn Tuấn Dũng", 18, "D25CQCC05-B")
tuan_dung.say_hello()
tuan_dung.info()
tuan_dung.study()
print(tuan_dung.lop_hoc)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   

    def show_balance(self):
        print(f"Số dư của {self.owner}: {self.__balance}")

acc_1 = BankAccount("Nguyễn Tuấn Dũng", 45000)
acc_1.show_balance()
#print(acc_1.__balance)  ---> Không hợp lệ