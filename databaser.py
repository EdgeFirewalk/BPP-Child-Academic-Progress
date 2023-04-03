import sqlite3

def find_in_database(pupil_name, subject):
    try:
        sqlite_connection = sqlite3.connect('sqlite_pupils.db')
        cursor = sqlite_connection.cursor()
        if subject != 'Все':
            cursor.execute(f'SELECT pupils.id, pupils.name, subjects.pupil_id, subjects.name, subjects.marks FROM pupils JOIN subjects ON pupils.id = subjects.pupil_id WHERE pupils.name=\'{pupil_name}\' AND subjects.name=\'{subject}\'')
        else:
            cursor.execute(f'SELECT pupils.id, pupils.name, subjects.pupil_id, subjects.name, subjects.marks FROM pupils JOIN subjects ON pupils.id = subjects.pupil_id WHERE pupils.name=\'{pupil_name}\'')
        records = cursor.fetchall()
        return records
    except sqlite3.Error as error:
        print("Ошибка при подключении к базе данных учеников...", error)
        return []
