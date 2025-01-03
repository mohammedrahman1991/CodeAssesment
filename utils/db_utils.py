# utils/db_utils.py

import mysql.connector

def get_db_connection():
    """
    Example DB connection; replace host/user/password/db with real values
    """
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password123",
        database="orangehrm_db"
    )

def user_exists_in_db(username):
    """
    Return True if user with given username is found in the 'users' table
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def delete_user_in_db(username):
    """
    Example of removing user from DB if needed
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    conn.commit()
    conn.close()
