# Класс = чертеж дома (шаблон)
class House:
    def __init__(self, color, floors):
        self.color = color
        self.floors = floors
    
    def describe(self):
        return f"Дом цвета {self.color}, {self.floors} этажа"
    
    def l_house(self):
        l = {self.color:self.floors}
        return l
    
    
# Объекты = конкретные дома, построенные по чертежу
house1 = House("белый", 2)  # объект класса House
house2 = House("синий", 1)  # другой объект того же класса
print(House.l_house(house1))

'''🔄 Конструкторы: __new__, __init__, __del__

📝 Представление: __str__, __repr__, __format__

⚖️ Сравнение: __eq__, __ne__, __lt__, __gt__, __le__, __ge__

🧮 Математика: __add__, __sub__, __mul__, __truediv__, __mod__

🗂️ Коллекции: __len__, __getitem__, __setitem__, __contains__, __iter__

🔧 Вызов: __call__, __getattr__, __setattr__, __delattr__

class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades or []
    
    def __str__(self):
        return f"Студент: {self.name}"
    
    def __repr__(self):
        return f"Student('{self.name}', {self.grades})"
    
    def __len__(self):
        return len(self.grades)
    
    def __getitem__(self, index):
        return self.grades[index]
    
    def __contains__(self, grade):
        return grade in self.grades
    
    def __call__(self):
        return f"Средний балл: {sum(self.grades)/len(self.grades) if self.grades else 0}"
    
    def add_grade(self, grade):
        self.grades.append(grade)

# Использование
student = Student("Иван")
student.add_grade(5)
student.add_grade(4)
student.add_grade(5)

print(student)        # Студент: Иван
print(len(student))   # 3
print(student[1])     # 4 (второй элемент)
print(5 in student)   # True
print(student())  '''    # Средний балл: 4.666...