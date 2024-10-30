var1 = 2


def multbyvar(x):
    return x*var1


print(multbyvar(7))


def mult(x):
    var2 = 5
    return x * var2


print(mult(7))


def mult2(x):
    var3 = 7
    return x * var3


var3 = 3
print(mult2(7))


def adding(x):
    var4 = 7
    return x + var4


print(adding(4))
# print(var4)

var5 = 2
print(var5)


def returnvar():
    global var5
    var5 = 5
    return var5


print(returnvar())
print(var5)


def message():
    alt = 1
    print('Olá mundo!')
# print(alt)


a = 1


def fun():
    a = 2
    print(a)


fun()
print(a)

a = 1


def fun2():
    global a
    a = 2
    print(a)


fun2()
a = 3
print(a)

a = 1


def fun3():
    global a
    a = 2
    print(a)


a = 3
fun3()
print(a)


def multiply(a1, b1):
    return a1 * b1


print(multiply(3, 4))


#def multiply(a1, b1):
#    return


#print(multiply(3, 4))


def wishes():
    return 'Feliz aniversário!'


w = wishes()
print(w)


def wishes2():
    print('Meus desejos')
    return 'Feliz aniversário!'


wishes2()


def wishes3():
    print('Meus desejos')
    return 'Feliz aniversário!'


print(wishes3())


def chamada(lista):
    for nomes in lista:
        print('Olá,', nomes)


chamada(['Adao', 'John', 'Lucy'])


def lista2(n):
    minhalista = []
    for i in range(n):
        minhalista.append(i)
    return minhalista


def lista3(n):
    minhalista2 = []
    for i in range(n):
        minhalista2.append(i)
    return minhalista2


lista3(5)


def lista4(n):
    minhalista3 = []
    for i in range(n):
        minhalista3.append(i)
    return minhalista3


print(lista4(5))


def lista5(n):
    minhalista4 = []
    for i in range(n):
        minhalista4.append(i)
    return minhalista4


x = lista5(5)
print(x)


def hi():
    return
    print('Oi!')


hi()


def isint(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False


print(isint(5))
print(isint(5.0))
print(isint('5'))


def evennumlst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst


print(evennumlst(11))


def listupdater(lst):
    updlist = []
    for elem in lst:
        elem **= 2
        updlist.append(elem)
    return updlist


foo = [1, 2, 3, 4, 5]
print(listupdater(foo))


def subtra(a3, b3):
    print(a3 - b3)


subtra(5, 2)
subtra(2, 5)


def subtra2(a4, b4):
    print(a4-b4)


subtra2(a4=5, b4=2)
subtra2(b4=2, a4=5)


def subtra3(a5, b5):
    print(a5 - b5)


subtra3(5, b5=2)
subtra3(5, 2)


def subtra4(a6, b6):
    print(a6 - b6)


subtra4(5, b6=2)
# subtra4(a6 = 5, 2)


def name(firstname, lastname='Smith'):
    print(firstname, lastname)


name('Andy')
name('Betty', 'Johnson')


def intro(a7='James Bond', b7='Bond'):
    print('Meu nome é', b7 + '.', a7 + '.')
intro()

def intro2(a8='James Bond', b8 = 'Bond'):
    print('Meu nome é', b8 + '.', a8 + '.')
intro2(b8 = 'Sean Connery')

def intro3(a9, b9='Bond'):
    print('Meu nome é', b9 + '.', a9 + '.')
intro3('Susan')

#def addnumbers(a10, b10=2,c10):
#    print(a10 + b10 + c10)
#addnumbers(a10=1,c10=3)