while True:
    s1 = int(input("typ an mummer : "))
    s2 = input("typ what u want to do :, x , - , +  ")
    s3 = int(input("typ an other nummer : "))
    if s2 == ("x"):
        result1 = s1 * s3
        print(s1 ," x ", s3, " = " ,result1)
        break
    elif s2 == ("-"):
        result2 = s1 - s3
        print(s1 ," - ", s3, " = " ,result2)
        break
    elif s2 == ("+"):
        result3 = s1 + s3
        print(s1 ," + ", s3, " = " ,result3)
        break
    elif s2 == (":"):
        resulte4 = s1 / s3
        print(s1 ," : ", s3, " = " ,resulte4)
        break
    else:
        print("Sorry try 1 more time .")