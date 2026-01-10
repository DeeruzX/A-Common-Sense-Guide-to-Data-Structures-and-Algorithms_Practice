def username_database(user_count: int):
    database = {}
    for _ in range(user_count):
        user_input = input()
        if user_input not in database:
            database[user_input] = 1
            print("OK")
        else:
            database[user_input] += 1
            print(f"{user_input}{database[user_input]}")


username_database(int(input()))
