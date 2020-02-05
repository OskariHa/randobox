from database1 import open_database


def login(name, pw):
    database = open_database()
    if name != "":
        for data in database:
            if name == data[0]:
                # print(data)
                if data[1] == pw:
                    print("logging in")

                    return True
                else:
                    print("wrong password")
                    return False
        print("no registered username")
    else:
        print("no user name given")
    return False
