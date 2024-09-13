import sqlite3


connection = sqlite3.connect("student2.db")
cursor = connection.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS COURSE
             (COURSE_ID INTEGER PRIMARY KEY,
             COURSE_NAME TEXT NOT NULL,
             COURSE_TIME INTEGER NOT NULL,
             FACULTY TEXT NOT NULL,
             CREDITS INTEGER NOT NULL,
             DEPARTMENT TEXT NOT NULL);''')


courses_data = [
    (1, 'ML', 90, 'Dr. Smith', 4, 'AIML'),
    (2, 'NLP', 75, 'Dr. Johnson', 3, 'CSE'),
    (3, 'CV', 60, 'Dr. Brown', 3, 'AIML'),
    (4, 'DS', 45, 'Dr. White', 3, 'CSE'),
    (5, 'Deep Learning', 90, 'Dr. Lee', 4, 'AIML'),
    (6, 'Algorithm Design', 60, 'Dr. Black', 3, 'CSE'),
    (7, 'Database Systems', 75, 'Dr. Grey', 3, 'CSE'),
    (8, 'Web Development', 45, 'Dr. Green', 3, 'CSE'),
    (9, 'Operating Systems', 60, 'Dr. Red', 3, 'CSE'),
    (10, 'Computer Networks', 75, 'Dr. Blue', 3, 'CSE'),
    (11, 'Artificial Intelligence', 90, 'Dr. Yellow', 4, 'AIML'),
    (12, 'Software Engineering', 75, 'Dr. Purple', 3, 'CSE'),
    (13, 'Information Retrieval', 60, 'Dr. Orange', 3, 'CSE'),
    (14, 'Cybersecurity', 45, 'Dr. Pink', 3, 'CSE'),
    (15, 'Cloud Computing', 60, 'Dr. Violet', 3, 'CSE'),
    (16, 'Mobile App Development', 75, 'Dr. Cyan', 3, 'CSE'),
    (17, 'Big Data Analytics', 90, 'Dr. Magenta', 4, 'AIML'),
    (18, 'Human-Computer Interaction', 75, 'Dr. Brown', 3, 'CSE'),
    (19, 'Embedded Systems', 60, 'Dr. Grey', 3, 'CSE'),
    (20, 'Computer Graphics', 45, 'Dr. White', 3, 'CSE'),
    
]

cursor.executemany('INSERT INTO COURSE VALUES (?, ?, ?, ?, ?, ?)', courses_data)

print("Records inserted successfully!")


connection.commit()
connection.close()
