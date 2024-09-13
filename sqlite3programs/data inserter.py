import sqlite3
from datetime import date, time

# Function to create a database and connect to it
def create_database(db_name):
    conn = sqlite3.connect(db_name)
    return conn

# Function to create tables in the database
def create_tables(conn):
    cursor = conn.cursor()

    # Create a table for person
    cursor.execute('''CREATE TABLE IF NOT EXISTS person
                     (id INTEGER PRIMARY KEY,
                     firstName VARCHAR,
                     middleName VARCHAR,
                     surname VARCHAR,
                     email VARCHAR,
                     contactNumber BIGINT,
                     dateOfBirth DATE,
                     gender VARCHAR,
                     emergencyContactNumber BIGINT,
                     addressId INT,
                     FOREIGN KEY(addressId) REFERENCES address(id))''')

    # Create a table for address
    cursor.execute('''CREATE TABLE IF NOT EXISTS address
                     (id INTEGER PRIMARY KEY,
                     country VARCHAR,
                     state VARCHAR,
                     city VARCHAR,
                     street VARCHAR,
                     house_number VARCHAR)''')

    # Create a table for staff_type
    cursor.execute('''CREATE TABLE IF NOT EXISTS staff_type
                     (id INTEGER PRIMARY KEY,
                     type VARCHAR)''')

    # Create a table for staff_grade
    cursor.execute('''CREATE TABLE IF NOT EXISTS staff_grade
                     (id INTEGER PRIMARY KEY,
                     grade VARCHAR)''')

    # Create a table for staff_category
    cursor.execute('''CREATE TABLE IF NOT EXISTS staff_category
                     (id INTEGER PRIMARY KEY)''')

    # Create a table for staff
    cursor.execute('''CREATE TABLE IF NOT EXISTS staff
                     (id INTEGER PRIMARY KEY,
                     staffCategoryId INT,
                     staffTypeId INT,
                     staffGradeId INT,
                     personId INT,
                     FOREIGN KEY(staffCategoryId) REFERENCES staff_category(id),
                     FOREIGN KEY(staffTypeId) REFERENCES staff_type(id),
                     FOREIGN KEY(staffGradeId) REFERENCES staff_grade(id),
                     FOREIGN KEY(personId) REFERENCES person(id))''')

    # Create a table for er_shift
    cursor.execute('''CREATE TABLE IF NOT EXISTS er_shift
                     (id INTEGER PRIMARY KEY,
                     name VARCHAR,
                     startTime TIME,
                     endTime TIME,
                     inchargeStaffId INT,
                     FOREIGN KEY(inchargeStaffId) REFERENCES staff(id))''')

    # Create a table for patient
    cursor.execute('''CREATE TABLE IF NOT EXISTS patient
                     (id INTEGER PRIMARY KEY,
                     personId INT,
                     admittedBy INT,
                     supervisedBy INT,
                     bedId INT,
                     medicationId INT,
                     admittedDate DATE,
                     age INT,
                     FOREIGN KEY(personId) REFERENCES person(id),
                     FOREIGN KEY(admittedBy) REFERENCES staff(id),
                     FOREIGN KEY(supervisedBy) REFERENCES staff(id),
                     FOREIGN KEY(bedId) REFERENCES bed(id),
                     FOREIGN KEY(medicationId) REFERENCES medication(id))''')

    # Create a table for medication
    cursor.execute('''CREATE TABLE IF NOT EXISTS medication
                     (id INTEGER PRIMARY KEY,
                     name VARCHAR,
                     dosage DECIMAL)''')

    # Create a table for bed
    cursor.execute('''CREATE TABLE IF NOT EXISTS bed
                     (id INTEGER PRIMARY KEY,
                     bedNo INT UNIQUE,
                     supervisedBy INT,
                     FOREIGN KEY(supervisedBy) REFERENCES staff(id))''')

    conn.commit()

# Function to insert data into the address table
def insert_address_data(conn):
    cursor = conn.cursor()
    addresses = [
        ('USA', 'California', 'Los Angeles', 'Main St', '123'),
        ('USA', 'California', 'San Francisco', 'Broadway', '456'),
        ('USA', 'New York', 'New York City', '5th Ave', '789'),
        ('Canada', 'Ontario', 'Toronto', 'Queen St', '1011'),
        ('Canada', 'British Columbia', 'Vancouver', 'Robson St', '1213'),
        ('UK', 'England', 'London', 'Oxford St', '1415'),
        ('France', 'Île-de-France', 'Paris', 'Champs-Élysées', '1617'),
        ('Germany', 'Bavaria', 'Munich', 'Marienplatz', '1819'),
        ('Australia', 'New South Wales', 'Sydney', 'George St', '2021'),
        ('Japan', 'Tokyo', 'Tokyo', 'Shibuya', '2223')
    ]
    cursor.executemany('INSERT INTO address (country, state, city, street, house_number) VALUES (?, ?, ?, ?, ?)', addresses)
    conn.commit()
    print("Data inserted into the address table.")

# Function to insert data into the person table
def insert_person_data(conn):
    cursor = conn.cursor()
    persons = [
        ('John', '', 'Doe', 'john.doe@email.com', 1234567890, '1990-01-01', 'Male', 9876543210, 1),
        ('Jane', '', 'Doe', 'jane.doe@email.com', 9876543210, '1995-05-05', 'Female', 1234567890, 2),
        # Add more rows as needed
    ]
    cursor.executemany('INSERT INTO person (firstName, middleName, surname, email, contactNumber, dateOfBirth, gender, emergencyContactNumber, addressId) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', persons)
    conn.commit()
    print("Data inserted into the person table.")

# Function to insert data into the staff_type table
def insert_staff_type_data(conn):
    cursor = conn.cursor()
    staff_types = [
        ('Doctor'),
        ('Nurse'),
        ('Administrator'),
        # Add more rows as needed
    ]
    cursor.executemany('INSERT INTO staff_type (type) VALUES (?)', staff_types)
    conn.commit()
    print("Data inserted into the staff_type table.")

# Function to insert data into the staff_grade table
def insert_staff_grade_data(conn):
    cursor = conn.cursor()
    staff_grades = [
        ('Junior'),
        ('Senior'),
        ('Specialist'),
        # Add more rows as needed
    ]
    cursor.executemany('INSERT INTO staff_grade (grade) VALUES (?)', staff_grades)
    conn.commit()
    print("Data inserted into the staff_grade table.")

# Function to insert data into the staff_category table
def insert_staff_category_data(conn):
    cursor = conn.cursor()
    # Assuming there are no predefined categories, so just insert IDs
    cursor.execute('INSERT INTO staff_category (id) VALUES (1)')
    conn.commit()
    print("Data inserted into the staff_category table.")

# Function to insert data into the staff table
def insert_staff_data(conn):
    cursor = conn.cursor()
    staff = [
        (1, 1, 1, 1),
        (1, 1, 1, 2),
        # Add more rows as needed
    ]
    cursor.executemany('INSERT INTO staff (staffCategoryId, staffTypeId, staffGradeId, personId) VALUES (?, ?, ?, ?)', staff)
    conn.commit()
    print("Data inserted into the staff table.")

# Function to insert data into the er_shift table
def insert_er_shift_data(conn):
    cursor = conn.cursor()
    er_shifts = [
        ('Morning', '08:00:00', '16:00:00', 1),
        ('Evening', '16:00:00', '00:00:00', 2),
        # Add more rows as needed
    ]
    cursor.executemany('INSERT INTO er_shift (name, startTime, endTime, inchargeStaffId) VALUES (?, ?, ?, ?)', er_shifts)
    conn.commit()
    print("Data inserted into the er_shift table.")

# Function to insert data into the patient table
def insert_patient_data(conn):
    cursor = conn.cursor()
    patients = [
        (1, 1, 1, 1, 1, 1, '2024-04-29', 30),
        (2, 1, 1, 1, 2, 2, '2024-04-29', 25),
        # Add more rows as needed
    ]
    cursor.executemany('INSERT INTO patient (personId, admittedBy, supervisedBy, bedId, medicationId, admittedDate, age) VALUES (?, ?, ?, ?, ?, ?, ?)', patients)
    conn.commit()
    print("Data inserted into the patient table.")

# Function to insert data into the medication table
def insert_medication_data(conn):
    cursor = conn.cursor()
    medications = [
        ('Paracetamol', 500),
        ('Aspirin', 100),
        # Add more rows as needed
    ]
    cursor.executemany('INSERT INTO medication (name, dosage) VALUES (?, ?)', medications)
    conn.commit()
    print("Data inserted into the medication table.")

# Function to insert data into the bed table
def insert_bed_data(conn):
    cursor = conn.cursor()
    beds = [
        (1, 101, 1),
        (2, 102, 1),
        # Add more rows as needed
    ]
    cursor.executemany('INSERT INTO bed (bedNo, supervisedBy) VALUES (?, ?)', beds)
    conn.commit()
    print("Data inserted into the bed table.")

# Main code
if __name__ == "__main__":
    db_name = "hospital.db"
    conn = create_database(db_name)
    create_tables(conn)
    insert_address_data(conn)
    insert_person_data(conn)
    insert_staff_type_data(conn)
    insert_staff_grade_data(conn)
    insert_staff_category_data(conn)
    insert_staff_data(conn)
    insert_er_shift_data(conn)
    insert_patient_data(conn)
    insert_medication_data(conn)
    insert_bed_data(conn)
    conn.close()
    print("Database created and data inserted successfully.")

'''
import sqlite3
import random
import datetime

# Function to create a database and connect to it
def create_database(db_name):
    conn = sqlite3.connect(db_name)
    return conn

# Function to insert data into all tables
def insert_data(conn):
    cursor = conn.cursor()

    # Insert data into the person table
    for i in range(1, 31):
        firstName = f"First{i}"
        middleName = f"Middle{i}"
        surname = f"Surname{i}"
        email = f"email{i}@example.com"
        contactNumber = 6000000000 + i
        dateOfBirth = datetime.date.today() - datetime.timedelta(days=i*365)
        gender = random.choice(['Male', 'Female'])
        emergencyContactNumber = 7000000000 + i
        addressId = i

        cursor.execute("INSERT INTO person (firstName, middleName, surname, email, contactNumber, dateOfBirth, gender, emergencyContactNumber, addressId) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                        (firstName, middleName, surname, email, contactNumber, dateOfBirth, gender, emergencyContactNumber, addressId))

    # Insert data into the address table
    for i in range(1, 31):
        country = f"Country{i}"
        state = f"State{i}"
        city = f"City{i}"
        street = f"Street{i}"
        house_number = f"House{i}"

        cursor.execute("INSERT INTO address (country, state, city, street, house_number) VALUES (?, ?, ?, ?, ?)", 
                        (country, state, city, street, house_number))

    # Insert data into the staff_type table
    for i in range(1, 31):
        staff_type = f"Type{i}"

        cursor.execute("INSERT INTO staff_type (type) VALUES (?)", (staff_type,))

    # Insert data into the staff_grade table
    for i in range(1, 31):
        staff_grade = f"Grade{i}"

        cursor.execute("INSERT INTO staff_grade (grade) VALUES (?)", (staff_grade,))

    # Insert data into the staff_category table
    for i in range(1, 31):
        cursor.execute("INSERT INTO staff_category DEFAULT VALUES")

    # Insert data into the staff table
    for i in range(1, 31):
        staffCategoryId = i
        staffTypeId = random.randint(1, 30)
        staffGradeId = random.randint(1, 30)
        personId = i

        cursor.execute("INSERT INTO staff (staffCategoryId, staffTypeId, staffGradeId, personId) VALUES (?, ?, ?, ?)", 
                        (staffCategoryId, staffTypeId, staffGradeId, personId))

    # Insert data into the er_shift table
    for i in range(1, 31):
        name = f"Shift{i}"
        startTime = datetime.time(8, 0)
        endTime = datetime.time(16, 0)
        inchargeStaffId = i

        cursor.execute("INSERT INTO er_shift (name, startTime, endTime, inchargeStaffId) VALUES (?, ?, ?, ?)", 
                ("Shift Name", "08:00:00", "16:00:00", 1))


    # Insert data into the patient table
    for i in range(1, 31):
        personId = i
        admittedBy = random.randint(1, 30)
        supervisedBy = random.randint(1, 30)
        bedId = random.randint(1, 30)
        medicationId = random.randint(1, 30)
        admittedDate = datetime.date.today() - datetime.timedelta(days=i*30)
        age = random.randint(1, 100)

        cursor.execute("INSERT INTO patient (personId, admittedBy, supervisedBy, bedId, medicationId, admittedDate, age) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                        (personId, admittedBy, supervisedBy, bedId, medicationId, admittedDate, age))

    # Insert data into the medication table
    for i in range(1, 31):
        name = f"Medication{i}"
        dosage = random.uniform(1, 10)

        cursor.execute("INSERT INTO medication (name, dosage) VALUES (?, ?)", 
                        (name, dosage))

    # Insert data into the bed table
    for i in range(1, 31):
        bedNo = i
        supervisedBy = random.randint(1, 30)

        cursor.execute("INSERT INTO bed (bedNo, supervisedBy) VALUES (?, ?)", 
                        (bedNo, supervisedBy))

    conn.commit()

# Main code
if __name__ == "__main__":
    db_name = "hospital.db"
    conn = create_database(db_name)
    insert_data(conn)
    conn.close()
    print("Data inserted successfully.")
'''