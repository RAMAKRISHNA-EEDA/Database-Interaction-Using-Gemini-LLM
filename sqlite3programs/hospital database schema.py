import sqlite3

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

# Main code
if __name__ == "__main__":
    db_name = "hospital.db"
    conn = create_database(db_name)
    create_tables(conn)
    conn.close()
    print("Database created successfully.")
