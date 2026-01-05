
from app.db import get_connection

def load_questions(db_path: str | None = None):
    conn = get_connection(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, question_text
        FROM question_bank
        WHERE is_active = 1
        ORDER BY id
    """)

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        raise RuntimeError("No questions found in database")

    return rows   # [(id, text), ...]
