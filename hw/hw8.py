import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Включаем поддержку внешних ключей
cursor.execute("PRAGMA foreign_keys = ON")

# Таблица студентов
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")

# Таблица курсов
cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    grade INTEGER,
    student_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id)
)
""")

conn.commit()



def add_student(name, age):
    cursor.execute(
        "INSERT INTO students (name, age) VALUES (?, ?)",
        (name, age)
    )
    conn.commit()
def add_course(title, grade, student_id):
    cursor.execute(
        "INSERT INTO courses (title, grade, student_id) VALUES (?, ?, ?)",
        (title, grade, student_id)
    )
    conn.commit()

def show_students_with_courses():
    cursor.execute("""
    SELECT students.name, courses.title, courses.grade
    FROM students
    LEFT JOIN courses ON students.id = courses.student_id
    """)

    rows = cursor.fetchall()
    for row in rows:
        print(f"Студент: {row[0]}, Курс: {row[1]}, Оценка: {row[2]}")



def aggregate_functions():
    cursor.execute("""
    SELECT 
        COUNT(*) AS total_courses,
        MAX(grade) AS max_grade,
        MIN(grade) AS min_grade,
        AVG(grade) AS avg_grade
    FROM courses
    """)

    result = cursor.fetchone()
    print(f"""
Всего курсов: {result[0]}
Максимальная оценка: {result[1]}
Минимальная оценка: {result[2]}
Средняя оценка: {round(result[3], 2)}
""")


def courses_per_student():
    cursor.execute("""
    SELECT students.name, COUNT(courses.id)
    FROM students
    LEFT JOIN courses ON students.id = courses.student_id
    GROUP BY students.name
    """)

    for name, count in cursor.fetchall():
        print(f"{name}: {count} курсов")


def students_with_high_grade(min_grade):
    cursor.execute("""
    SELECT name FROM students
    WHERE id IN (
        SELECT student_id FROM courses
        WHERE grade >= ?
    )
    """, (min_grade,))

    for row in cursor.fetchall():
        print(f"Студент с высокой оценкой: {row[0]}")


cursor.execute("""
CREATE VIEW IF NOT EXISTS student_courses_view AS
SELECT students.name, courses.title, courses.grade
FROM students
JOIN courses ON students.id = courses.student_id
""")
conn.commit()



def read_view():
    cursor.execute("SELECT * FROM student_courses_view")
    for row in cursor.fetchall():
        print(f"Студент: {row[0]}, Курс: {row[1]}, Оценка: {row[2]}")


add_student("eliza", 19)
add_student("kaila", 20)

add_course("Python", 90, 1)
add_course("SQL", 85, 1)
add_course("Python", 70, 2)

show_students_with_courses()
aggregate_functions()
courses_per_student()
students_with_high_grade(80)
read_view()
