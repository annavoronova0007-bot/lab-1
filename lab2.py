class Faculty:
    def __init__(self, name_f: str):
        self.__name_f = name_f
        self.__students = {}  
        self.__departments = []

    @property
    def name_f(self):
        return self.__name_f

    @property
    def students(self):
        return self.__students

    @property
    def departments(self):
        return self.__departments

    def add_department(self, department):
        self.__departments.append(department)

    def enroll_student(self, student):
        if student.id in self.__students:
            print("Студент с таким ID уже существует на факультете")
            return False
        self.__students[student.id] = student
        print(f"Студент {student.name} зачислен на специальность '{student.specialization}'.")
        return True


class Department:
    def __init__(self, department_name: str, faculty: Faculty):
        self.__department = department_name
        self.__faculty = faculty
        self.__disciplines = []

    @property
    def department(self):
        return self.__department

    @property
    def faculty(self):
        return self.__faculty

    @property
    def disciplines(self):
        return self.__disciplines

    def add_discipline(self, discipline):
        self.__disciplines.append(discipline)


class Discipline:
    def __init__(self, discipline_name: str, department: Department, specializations: list):
        self.__name = discipline_name
        self.__department = department
        self.__specializations = specializations

    @property
    def department(self):
        return self.__department

    @property
    def name(self):
        return self.__name

    @property
    def specializations(self):
        return self.__specializations


class Student:
    def __init__(self, student_id: int, name: str, surname: str, faculty: Faculty, department: Department, specialization: str):
        self.__id = student_id
        self.__name = name
        self.__surname = surname
        self.__faculty = faculty
        self.__department = department
        self.__specialization = specialization
        self.__grades = {} 
        self.__active = True
        self.__semester = 1

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def specialization(self):
        return self.__specialization

    @property
    def grades(self):
        return self.__grades

    @property
    def active(self):
        return self.__active

    @property
    def semester(self):
        return self.__semester

    def expulsion(self):
        if not self.__active:
            print("Студент уже отчислен.")
        else:
            self.__active = False
            print(f"Студент {self.name} отчислен.")

    def enroll_to_discipline(self, discipline_name: str):
        if not self.__active:
            print("Студент отчислен и не может быть записан на дисциплину!")
        elif discipline_name in self.__grades:
            print("Студент уже изучает эту дисциплину!")
        else:
            self.__grades[discipline_name] = None
            print(f"Студент {self.name} записан на дисциплину '{discipline_name}'")

    def remove_from_discipline(self, discipline_name: str):
        if discipline_name not in self.__grades:
            print("Студент не записан на эту дисциплину!")
        else:
            del self.__grades[discipline_name]
            print(f"Студент {self.name} удален с дисциплины '{discipline_name}'")

    def set_grade(self, discipline: str, value: float):
        if not self.__active:
            print("Этот студент отчислен, ему нельзя выставлять оценки!")
        elif discipline not in self.__grades:
            print("Эту дисциплину студент не изучает!")
        elif value < 0 or value > 10:
            print("Оценка должна быть от 0 до 10!")
        else:
            self.__grades[discipline] = value
            print(f"Студенту {self.name} поставлена оценка {value} по дисциплине '{discipline}'")

    def promote(self):
        if not self.__active:
            print("Студент отчислен!")
            return
            
        if not self.__grades:
            print("Студент не изучает ни одной дисциплины!")
            return
            
        for disc, grade in self.__grades.items():
            if grade is None:
                print(f"Студент не сдал дисциплину '{disc}' (нет оценки)!")
                return
            if grade < 3:
                print(f"Студент не сдал дисциплину '{disc}' (оценка {grade})!")
                return
        
        self.__semester += 1
        self.__grades.clear()
        print(f"Студент {self.name} успешно переведен на {self.__semester} семестр!")


faculty = Faculty("Факультет Радиофизики и Компьютерных технологий")

d1 = Department("Кафедра радиофизики и цифровых медиа технологий", faculty)
d2 = Department("Кафедра физической электроники и нанотехнологий", faculty)
d3 = Department("Кафедра интеллектуальных систем", faculty)
d4 = Department("Кафедра системного анализа и компьютерного моделирования", faculty)
d5 = Department("Кафедра квантовой радиофизики и оптоэлектроники", faculty)
d6 = Department("Кафедра информатики и компьютерных систем", faculty)
d7 = Department("Кафедра кибербезопасности и информационных технологий", faculty)
d8 = Department("Кафедра физики и аэрокосмических технологий", faculty)

for dep in [d1, d2, d3, d4, d5, d6, d7, d8]:
    faculty.add_department(dep)

disc_python = Discipline("Программирование на Python", d6, ["прикладная информатика"])
d6.add_discipline(disc_python)

disc_crypto = Discipline("Микроконтролеры", d7, ["кибербезопасность"])
d7.add_discipline(disc_crypto)

disc_math = Discipline("Математический анализ", d3, ["кибербезопасность", "прикладная информатика", "радиофизика","интеллектуальная электроника"])
d3.add_discipline(disc_math)


while True:
    print("\nМЕНЮ")
    print("1. Зачисление студента на специальность")
    print("2. Отчисление студента")
    print("3. Добавление студента на дисциплину")
    print("4. Удаление студента с дисциплины")
    print("5. Выставление отметки")
    print("6. Перевод на следующий семестр")
    print("7. Ведомость успеваемости студента (в файл)")
    print("8. Ведомость по дисциплине (в файл)")
    print("9. Завершение программы")
    
    choice_str = input("Ваш выбор (номер): ")
    
    if not choice_str.isdigit():
        print("Введите число!")
        continue
        
    choice = int(choice_str)

    if choice == 9:
        print("Завершение программы...")
        break

    student = None
    if choice in [2, 3, 4, 5, 6, 7]:
        id_str = input("Введите ID студента: ")
        
        if not id_str.isdigit():
            print("ID должен быть числом!")
            continue
            
        search_id = int(id_str)
        student = faculty.students.get(search_id)
        
        if student is None:
            print("Студент с таким ID не найден!")
            continue

    if choice == 1:
        id_str = input("Введите ID студента: ")
        if not id_str.isdigit():
            print("ID должен быть числом!")
            continue
            
        s_id = int(id_str)
        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        
        print("Доступные специальности: кибербезопасность, прикладная информатика, радиофизика и интеллектуальная электроника")
        spec = input("Введите специальность: ")
        
        dep = d7 if spec.lower() == "кибербезопасность" else d6
        new_student = Student(s_id, name, surname, faculty, dep, spec)
        faculty.enroll_student(new_student)

    elif choice == 2:
        student.expulsion()

    elif choice == 3:
        disc_name = input("Введите название дисциплины: ")
        target_disc = None
        
        for dep in faculty.departments:
            for d in dep.disciplines:
                if d.name.lower() == disc_name.lower():
                    target_disc = d
                    break
        
        if not target_disc:
            print("Такая дисциплина не читается ни на одной кафедре.")
        elif student.specialization not in target_disc.specializations:
            print(f"Дисциплина '{disc_name}' не читается для специальности '{student.specialization}'.")
        else:
            student.enroll_to_discipline(target_disc.name)

    elif choice == 4:
        disc_name = input("Введите название дисциплины: ")
        student.remove_from_discipline(disc_name)

    elif choice == 5:
        disc_name = input("Введите название дисциплины: ")
        grade_str = input("Введите оценку (0-10): ")
        
        if not grade_str.replace('.', '', 1).isdigit():
            print("Ошибка: Оценка должна быть числом!")
            continue
            
        grade = float(grade_str)
        student.set_grade(disc_name, grade)

    elif choice == 6:
        student.promote()

    elif choice == 7:
        filename = f"student_{student.id}_report.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"ВЕДОМОСТЬ СТУДЕНТА: {student.name} {student.surname}\n")
            f.write(f"ID: {student.id}\n")
            f.write(f"Специальность: {student.specialization}\n")
            f.write(f"Семестр: {student.semester}\n")
            f.write(f"Статус: {'Активен' if student.active else 'Отчислен'}\n")
            
            total_score = 0
            count = 0
            for disc, grade in student.grades.items():
                f.write(f"Дисциплина: {disc} | Оценка: {grade if grade is not None else 'Нет'}\n")
                if grade is not None:
                    total_score += grade
                    count += 1
            
            avg = total_score / count if count > 0 else 0
            f.write(f"Средний балл: {round(avg, 2)}\n")
        print(f"Ведомость сохранена в файл '{filename}'.")

    elif choice == 8:
        disc_name = input("Введите название дисциплины для отчета: ")
        target_disc = None
        for dep in faculty.departments:
            for d in dep.disciplines:
                if d.name.lower() == disc_name.lower():
                    target_disc = d
                    break
        
        if not target_disc:
            print("Такая дисциплина не найдена.")
            continue

        filename = f"discipline_{target_disc.name}_report.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f" ВЕДОМОСТЬ ПО ДИСЦИПЛИНЕ: {target_disc.name}\n")
            f.write(f"Читающая кафедра: {target_disc.department.department}\n")
            
            total_score = 0
            count = 0
            for s in faculty.students.values():
                if target_disc.name in s.grades:
                    grade = s.grades[target_disc.name]
                    f.write(f"Студент: {s.name} {s.surname} | Оценка: {grade if grade is not None else 'Нет'}\n")
                    if grade is not None:
                        total_score += grade
                        count += 1
            
            avg = total_score / count if count > 0 else 0
            f.write(f"Средний балл по дисциплине: {round(avg, 2)}\n")
        print(f"Ведомость сохранена в файл '{filename}'.")

    else:
        print("Неверный пункт меню.")

    
    
    
    





        


    

    
    
        