password = input("Введите пароль:")

if len(password) < 16:
    print ("Пароль слишком короткий")
else:
    numbers = 0
    letters = 0
    for char in password:
        if char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            letters += 1
        elif char in "0123456789":
            numbers += 1

    if len(password)==numbers or len(password)==letters:
        print ("Слабый пароль")
    else:
        print ("Надежный пароль")
    

