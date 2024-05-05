import random 

nb1 = random.randint(1,4)
nb2 = random.randint(1,4)
nb3 = random.randint(-50,50)
nb4 = random.randint(1,4)
nb5 = random.randint(1,4)
nb6 = random.randint(-50,50)

go = True
while go == True:
    for x in range(-50,50):
        for y in range(-50,50):
            if x*nb1 + y*nb2 == nb3 and x*nb4 - nb5*y == nb6:
                print(f"{nb1}x + {nb2}y = {nb3}")
                print(f"{nb4}x - {nb5}y = {nb6}")

                print(f"x = {x}, y = {y}")
                go = False
          
    nb1 = random.randint(1,3)
    nb2 = random.randint(1,3)
    nb3 = random.randint(-50,50)
    nb4 = random.randint(1,3)
    nb5 = random.randint(1,3)
    nb6 = random.randint(-50,50)