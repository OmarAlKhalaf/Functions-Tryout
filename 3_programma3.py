def t1 ():
    print("Hello " + name + (" and you are " + leeftijd + (" old.")))
while True:
    name = input("What is your name ? :")
    leeftijd = input("What is your age ? :")
    t1()
    stop = input("""do u want to stop ? typ stop.
if you dont want to stop press enter : """)
    if stop == ("stop"):
        break
    elif stop == (""):
        continue