import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger


logger = setup_logger('db_helper')


@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    cursor.close()
    connection.close()


def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses


def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))


def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expense called with date: {expense_date}, amount: {amount}, category: {category}, notes: {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )


def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary called with start: {start_date} end: {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT category, SUM(amount) as total 
               FROM expenses WHERE expense_date
               BETWEEN %s and %s  
               GROUP BY category;''',
            (start_date, end_date)
        )
        data = cursor.fetchall()
        return data


def fetch_monthly_expense_summary():
    logger.info(f"fetch_expense_summary_by_months")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT month(expense_date) as expense_month, 
               monthname(expense_date) as month_name,
               sum(amount) as total FROM expenses
               GROUP BY expense_month, month_name
               ORDER BY expense_month ASC;
            '''
        )
        data = cursor.fetchall()
        return data

def fetch_custom_reports(start_date=None, end_date=None, categories=None):
    logger.info(f"fetch_custom_reports called with start: {start_date}, end: {end_date}, categories: {categories}")
    with get_db_cursor() as cursor:
        query = "SELECT * FROM expenses"
        conditions = []
        params = []

        if start_date:
            conditions.append("expense_date >= %s")
            params.append(start_date)
        if end_date:
            conditions.append("expense_date <= %s")
            params.append(end_date)
        if categories:
            placeholders = ','.join(['%s'] * len(categories))
            conditions.append(f"category IN ({placeholders})")
            params.extend(categories)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        cursor.execute(query, params)
        data = cursor.fetchall()
        return data

if __name__ == "__main__":
    # expenses = fetch_expenses_for_date("2024-09-30")
    # print(expenses)
    # # delete_expenses_for_date("2024-08-25")
    # summary = fetch_expense_summary("2024-08-01", "2024-08-05")
    # for record in summary:
    #     print(record)
    print(fetch_monthly_expense_summary())
