from db import get_db_connection

def mark_attendance(data):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO attendance
            (student_id, subject_id, attendance_date, status)
            VALUES (%s, %s, %s, %s)
        """

        values = (
            data["student_id"],
            data["subject_id"],
            data["attendance_date"],
            data["status"]
        )

        cursor.execute(query, values)
        conn.commit()
        return True

    except Exception as e:
        print(e)
        return False

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def get_attendance_by_student(student_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT *
            FROM attendance
            WHERE student_id = %s
            ORDER BY attendance_date
        """

        cursor.execute(query, (student_id,))
        records = cursor.fetchall()
        return records

    except Exception as e:
        print(e)
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def get_attendance_by_date(attendance_date):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT *
            FROM attendance
            WHERE attendance_date = %s
        """

        cursor.execute(query, (attendance_date,))
        records = cursor.fetchall()
        return records

    except Exception as e:
        print(e)
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
