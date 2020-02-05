#import account
import csv


def open_database():
    f = open("dataFiles/database.csv", "r")
    reader = csv.reader(f)
    db = []

    for row in reader:
        try:
            db.append([row[0], row[1], row[2]])
        except:
            pass

    #print(db)
    for item in db:
        print(item)
    return db


def write_database(db):
    f = open("dataFiles/database.csv", "w")
    for data in db:
        f.write(data[0] + "," + data[1] + "," + data[2] + "\n")
    f.close()


def create_database():
    header = "name, password, role\n"
    account_database = [("mike", "mike123", "noob"), ("josh", "josh234", "pro"), ("mila", "mila32", "admin"),
                        ("osku", "s", "admin")]
    f = open("database.csv", "w")
    f.write(header)
    for data in account_database:
        f.write(data[0] + ", " + data[1] + ", " + data[2] + "\n")
    f.close()


def account_data_change(old_account, updated_account):
    f = open("dataFiles/database.csv", "r")
    reader = csv.reader(f)
    db = []

    for row in reader:
        try:
            if row[0] == old_account.name:
                db.append([updated_account.name, row[1], updated_account.role])
            else:
                db.append([row[0], row[1], row[2]])
        except:
            pass

    # print(db)
    for item in db:
        print(item)
    write_database(db)


def account_password_change(current_account, password_new, password_old):
    f = open("dataFiles/database.csv", "r")
    reader = csv.reader(f)
    db = []

    for row in reader:
        try:
            print(row[1])
            print(password_old)
            if row[1] == password_old:
                db.append([row[0], password_new, row[2]])
                print("password changed successfully!")
            else:
                db.append([row[0],row[1],row[2]])
        except:
            pass

    # print(db)
    for item in db:
        print(item)
    write_database(db)
    print("current password wrong")
    print("account not found in database!??!!?")
