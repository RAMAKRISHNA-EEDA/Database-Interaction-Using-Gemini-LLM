import sqlite3

def get_schema(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    schema = {}
    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        schema[table_name] = [col[1] for col in columns]

    conn.close()
    return schema

# Example usage
schema = get_schema('hospital.db')
for table, columns in schema.items():
    print(f"Table: {table}")
    print("Columns:", ", ".join(columns))
    print()
