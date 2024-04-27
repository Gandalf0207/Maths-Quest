print("ok")
c = 0
def bonjour(c):
    print("bonjour")

    def ah(c):
        c+= 1
        print("ah")
        bonjour(c)
        return c

    if c < 3:

        c = ah(c)
    return c


ok = bonjour(c)
print(ok)