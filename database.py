import sqlite3


# --------- project functions ----------

# get project timetables
def get_project_timetables(table):
    # Create a database or connect to one
    conn = sqlite3.connect('database/rando_database.db')
    # Create cursor
    c = conn.cursor()

    if table == "weekly":
        c.execute("SELECT *, oid FROM weekly_tasks")
    if table == "daily":
        c.execute("SELECT *, oid FROM daily_tasks")

    tasks = c.fetchall()
    for task in tasks:
        print(task)

    # Commit changes
    conn.commit()
    # Close database connection
    conn.close()


def fetch_tasks(table):
    # Create a database or connect to one
    conn = sqlite3.connect('database/rando_database.db')
    # Create cursor
    c = conn.cursor()

    c.execute("SELECT *, oid FROM " + table + " ORDER BY day DESC")
    tasks = c.fetchall()

    returned_list = []
    for task in tasks:
        returned_list.append([task[0], task[1], task[2]])

    # Commit changes
    conn.commit()
    # Close database connection
    conn.close()

    return returned_list


# write project data to db
def submit_tasks(table, data_list):
    # Create a database or connect to one
    conn = sqlite3.connect('database/rando_database.db')
    # Create cursor
    c = conn.cursor()

    c.execute("SELECT day, oid FROM " + table)
    tasks = c.fetchall()
    for data in data_list:
        day = data[0]
        plan = data[1]
        done = data[2]
        exist = True
        for task in tasks:
            if day in task:
                c.execute("UPDATE " + table + " SET day_plan = :day_plan, day_done = :day_done WHERE day= :day",
                          {
                              'day': day,
                              'day_plan': plan,
                              'day_done': done
                          })
                exist = False
                break
        if exist:
            c.execute("INSERT INTO " + table + " VALUES(:day, :day_plan, :day_done)",
                      {
                          'day': day,
                          'day_plan': plan,
                          'day_done': done
                      })
    # Commit changes
    conn.commit()
    # Close database connection
    conn.close()


# -------- Login and account functions ---------
# open login
def login(username, userpw):
    # Create a database or connect to one
    conn = sqlite3.connect('database/rando_database.db')
    # Create cursor
    c = conn.cursor()

    c.execute("SELECT * FROM accounts WHERE username=?", (username,))
    account_data = c.fetchone()
    # print(account_data[1])

    # Commit changes
    conn.commit()
    # Close database connection
    conn.close()
    if account_data is None:
        print("no account name")
        print(account_data)
    else:
        if account_data[1] == userpw:
            print("login found")
            # print(account_data)
            return True
        else:
            # no password match
            print("wrong password")
            return False


def admin_delete_account(username):
    # Create a database or connect to one
    conn = sqlite3.connect('database/rando_database.db')
    # Create cursor
    c = conn.cursor()

    # c.execute("DELETE FROM accounts WHERE username=?", (username,))
    # c.execute("DELETE FROM accounts WHERE oid=?", (username,))

    c.execute("DELETE FROM daily_tasks WHERE oid=?", (username,))

    # Commit changes
    conn.commit()
    # Close database connection
    conn.close()


def create_account(username, password, status):
    # Create a database or connect to one
    conn = sqlite3.connect('database/rando_database.db')
    # Create cursor
    c = conn.cursor()

    c.execute("SELECT username FROM accounts")
    accounts = c.fetchall()
    print(accounts)
    for account in accounts:
        temp_un = "('" + username + "',)"
        print(account)
        if username in account:
            print("Username already exists")
            return False
    c.execute("INSERT INTO accounts VALUES(:username, :password, :status)",
              {
                  'username': username,
                  'password': password,
                  'status': status
              })
    # Commit changes
    conn.commit()
    # Close database connection
    conn.close()
    # account created successfully
    return True

def admin_get_account_info():
    # Create a database or connect to one
    conn = sqlite3.connect('database/rando_database.db')
    # Create cursor
    c = conn.cursor()

    c.execute("SELECT username, status, oid FROM accounts ORDER BY status")
    accounts = c.fetchall()

    # Commit changes
    conn.commit()
    # Close database connection
    conn.close()

    return accounts


# --------- Database functions --------
def show_table():
    # Create a database or connect to one
    conn = sqlite3.connect('database/rando_database.db')
    # Create cursor
    c = conn.cursor()

    c.execute("SELECT *, oid FROM daily_tasks")
    accounts = c.fetchall()

    print(accounts)

    # Commit changes
    conn.commit()
    # Close database connection
    conn.close()


# create database
def create_database(dbname, dbcontent):
    # Create a database or connect to one
    conn = sqlite3.connect('database/rando_database.db')
    # Create cursor
    c = conn.cursor()
    # Create table

    c.execute("""CREATE TABLE dbname (
            dbcontent
            )""",
              {
                  'dbname': dbname,
                  'dbcontent': dbcontent
              })

    # Commit changes
    conn.commit()
    # Close database connection
    conn.close()

    '''
    c.execute("""CREATE TABLE accounts (
        username text,
        password text,
        status text
        )""")
    c.execute("""CREATE TABLE daily_tasks (
        day text,
        day_plan text,
        day_done text
        )""")
    c.execute("""CREATE TABLE weekly_tasks (
        day text,
        week_plan text,
        week_done text
        )""")
    '''
