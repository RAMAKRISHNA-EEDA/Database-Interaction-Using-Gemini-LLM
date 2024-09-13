import sqlite3

try:
    connection = sqlite3.connect("student2.db")
    cursor = connection.cursor()

    table_info = """
    CREATE TABLE IF NOT EXISTS STUDENT (
        NAME VARCHAR(25),
        DEPARTMENT VARCHAR(25),
        COURSE VARCHAR(25),
        CGPA REAL
    );
    """

    cursor.execute(table_info)

    records = [
        ('Nitin', 'AIML', 'Deep Learning', 9.3),
        ('Abhiash', 'AIML', 'Deep Learning', 9.5),
        ('Omkar', 'CSE(AIML)', 'NLP', 8.6),
        ('Tarun', 'CSE', 'FCN', 8.2),
        ('Mani Teja', 'CSE(AIDS)', 'NLP', 8.8),
        ('Mani Deepak', 'CSE(AIDS)', 'RPA', 8.3),
        ('Abhi Ram', 'CSE', 'FCN', 9.6),
        ('Krishna', 'CSE(AIML)', 'NLP', 9.0),
        ('Ajith', 'CSE(AIDS)', 'FCN', 8.9),
        ('Phani', 'CSE', 'Deep Learning', 7.2),
        ('Ram', 'AIML', 'NLP', 9.6),
        ('Rakesh', 'AIML', 'RPA', 8.1),
        ('Srikanth', 'CSE(AIDS)', 'Deep Learning', 8.2),
        ('Sai Kumar', 'AIML', 'Deep Learning', 9.7),
        ('Harsha', 'CSE', 'RPA', 8.9),
        ('Nani', 'CSE', 'RPA', 7.2),
        ('Ashok', 'CSE(AIDS)', 'RPA', 8.4),
        ('Amit', 'AIML', 'Deep Learning', 9.3),
        ('Rahul', 'AIML', 'Deep Learning', 9.5),
        ('Om', 'CSE(AIML)', 'NLP', 8.6),
        ('Raj', 'CSE', 'FCN', 8.2),
        ('Teja', 'CSE(AIDS)', 'NLP', 8.8),
        ('Deepak', 'CSE(AIDS)', 'RPA', 8.3),
        ('Ram', 'CSE', 'FCN', 9.6),
        ('Krish', 'CSE(AIML)', 'NLP', 9.0),
        ('Ajay', 'CSE(AIDS)', 'FCN', 8.9),
        ('Pavan', 'CSE', 'Deep Learning', 7.2),
        ('Rajesh', 'AIML', 'NLP', 9.6),
        ('Rajat', 'AIML', 'RPA', 8.1),
        ('Kanth', 'CSE(AIDS)', 'Deep Learning', 8.2),
        ('Kumar', 'AIML', 'Deep Learning', 9.7),
        ('Harish', 'CSE', 'RPA', 8.9),
        ('Naga', 'CSE', 'RPA', 7.2),
        ('Ashish', 'CSE(AIDS)', 'RPA', 8.4),
        ('Vinay', 'AIML', 'Deep Learning', 9.3),
        ('Vivek', 'AIML', 'Deep Learning', 9.5),
        ('Manish', 'CSE(AIML)', 'NLP', 8.6),
        ('Karthik', 'CSE', 'FCN', 8.2),
        ('Vikram', 'CSE(AIDS)', 'NLP', 8.8),
        ('Vishal', 'CSE(AIDS)', 'RPA', 8.3),
        ('Varun', 'CSE', 'FCN', 9.6),
        ('Vijay', 'CSE(AIML)', 'NLP', 9.0),
        ('Vishnu', 'CSE(AIDS)', 'FCN', 8.9),
        ('Vineet', 'CSE', 'Deep Learning', 7.2),
        ('Aakash', 'AIML', 'Deep Learning', 9.3),
        ('Bhavya', 'AIML', 'Deep Learning', 9.5),
        ('Chaitanya', 'CSE(AIML)', 'NLP', 8.6),
        ('Dhruv', 'CSE', 'FCN', 8.2),
        ('Esha', 'CSE(AIDS)', 'NLP', 8.8),
        ('Fahad', 'CSE(AIDS)', 'RPA', 8.3),
        ('Gauri', 'CSE', 'FCN', 9.6),
        ('Himanshu', 'CSE(AIML)', 'NLP', 9.0),
        ('Ishita', 'CSE(AIDS)', 'FCN', 8.9),
        ('Jatin', 'CSE', 'Deep Learning', 7.2),
        ('Kajal', 'AIML', 'NLP', 9.6),
        ('Lakshya', 'AIML', 'RPA', 8.1),
        ('Manish', 'CSE(AIDS)', 'Deep Learning', 8.2),
        ('Neha', 'AIML', 'Deep Learning', 9.7),
        ('Ojas', 'CSE', 'RPA', 8.9),
        ('Prerna', 'CSE', 'RPA', 7.2),
        ('Quinton', 'CSE(AIDS)', 'RPA', 8.4),
        ('Rahul', 'AIML', 'Deep Learning', 9.3),
        ('Sneha', 'AIML', 'Deep Learning', 9.5),
        ('Tanvi', 'CSE(AIML)', 'NLP', 8.6),
        ('Utkarsh', 'CSE', 'FCN', 8.2),
        ('Vaishnavi', 'CSE(AIDS)', 'NLP', 8.8),
        ('Waris', 'CSE(AIDS)', 'RPA', 8.3),
        ('Xavier', 'CSE', 'FCN', 9.6),
        ('Yuvraj', 'CSE(AIML)', 'NLP', 9.0),
        ('Zara', 'CSE(AIDS)', 'FCN', 8.9),
        ('Aaditya', 'CSE', 'Deep Learning', 7.2),
        ('Bhavesh', 'AIML', 'NLP', 9.6),
        ('Chinmay', 'AIML', 'RPA', 8.1),
        ('Devansh', 'CSE(AIDS)', 'Deep Learning', 8.2),
        ('Eshika', 'AIML', 'Deep Learning', 9.7),
        ('Farhan', 'CSE', 'RPA', 8.9),
        ('Gaurav', 'CSE', 'RPA', 7.2),
        ('Harshita', 'CSE(AIDS)', 'RPA', 8.4),
        ('Ishan', 'AIML', 'Deep Learning', 9.3),
        ('Jhanvi', 'AIML', 'Deep Learning', 9.5),
        ('Karan', 'CSE(AIML)', 'NLP', 8.6),
        ('Lakshay', 'CSE', 'FCN', 8.2),
        ('Manya', 'CSE(AIDS)', 'NLP', 8.8),
        ('Nidhi', 'CSE(AIDS)', 'RPA', 8.3),
        ('Omkara', 'CSE', 'FCN', 9.6),
        ('Pooja', 'CSE(AIML)', 'NLP', 9.0),
        ('Qamar', 'CSE(AIDS)', 'FCN', 8.9),
        ('Rahil', 'CSE', 'Deep Learning', 7.2),
        ('Siddharth', 'AIML', 'NLP', 9.6),
        ('Tanmay', 'AIML', 'RPA', 8.1),
        ('Ujjwal', 'CSE(AIDS)', 'Deep Learning', 8.2),
        ('Vidhi', 'AIML', 'Deep Learning', 9.7),
        ('Yash', 'CSE', 'RPA', 8.9),
        ('Zoya', 'CSE', 'RPA', 7.2),
        ('Aarav', 'CSE(AIDS)', 'RPA', 8.4)
    ]

    for record in records:
        cursor.execute("INSERT INTO STUDENT VALUES (?, ?, ?, ?)", record)

    print("Records inserted successfully")

    print("The inserted records are:")
    data = cursor.execute("SELECT * FROM STUDENT")
    for row in data:
        print(row)

    connection.commit()

except sqlite3.Error as e:
    print("An error occurred:", e)

finally:
    if connection:
        connection.close()
