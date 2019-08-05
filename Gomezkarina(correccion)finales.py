# 1- imprimir x -> x
def imprimir():
# *—*
    print("hola mundo")
imprimir()


# 2-
def sum(a,b):
    return a+b
print(sum(1,2))
# f: >< — >< — ><

# 3-
def max(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

print(max(7,6))

# 4-
def entre0y10(n):
    return ((n >0) and (n<10))
    print ("entre o y 10")
    else: 
    print ( " no esta en este rango")
   def "entreoy10"(7):
        return 
# 5-
def comparandoUnNumero(a):
    if(a>=1 and a<=10):
        print("Esta entre 1 y 10")
    elif(a>=11 and a<=20):
        print("Esta entre 11 y 20")
    elif(a>=21 and a<=30):
        print("Esta entre 21 y 30")
    else:
        print("No esta en ese rango")
 def "comparandoUnNumero"(20):
     return 

# y aca???

# 6- 
x=1
while x<=100:
    print(x)
    x=x+1
# f:>< — string
#aca no lo probo, no deberia tomar un valor, y no inicializa

# 7-
def imprime1al100():
    for i in range (1, 100):
        print i
i def imprime1al100
       return 

# 8-
def imprimecadacaracter():
    print ("hola mundo")
imprimir ()  
# quizas no esta bien explicada la funcion, pero deberia hace run for para imprimir cada caracter
  
# 9- 
def numeropar(n):
num = input("Introduce un número: ")
num = int(num)
if num == 0:
     print ("Este número es par")
elif num%2 == 0:
    print ("Este numero es par")
else:
    print ("Este numero es impar")
def "numeropar"(7):
     return 
#??????????

# 10-
def muestrapares0y100():
    print i in range (1,100):
          print i 
i def imprimepares0y100
#?????

# 11-
def entre0y100():
print randrange(0,100,2)
def "entre0y100" 
     return 

#????

def entre1y100():
print randrange(1,100,2)
def "entre1y100" 
     return 
# 12-
 print randint(5,10)
       return 
#genera una lista de numeros, no un numero

# 13-
rango = list(range(10,0,)) 
print(rango)
#aca si

# 14-
rango = list( range(0, len("Hola mundo")))
 
print(rango)
# el programa lo hace, pero no es una funcion

# 15-
import random
n=random.randrange(1,100)
nu=int(input('Dime el número que crees que he elegido '))
c=1
while nu!=n:
  c+=1
  if nu>n:
      nu=int(input('El número es mas pequeño'))
  elif nu<n:
      nu=int(input('El número es mas grande'))
print('Felicidades has adivinado que el número secreto es:',n)
print('Y lo has adivinado en',c,'intentos.')def a(n):
    x = 0
    i = 0
    while i <= n:
        x += i
        i += 1
    return x
def a(n):
    x = 0
    i = 0
    while i <= n:
        x += i
        i += 1
    return x
# REvisar

#16-
def mayor3(a,b,c):
    if((a > b) and (a > c)):
        return a
    if((b > a) and (b > c)):
        return b
    if((c > a) and (c > b)):
return c


#17-
Funcion isNum():
      def isnum(a):
      try:
         int(a)
      except:
         return False;
      return True;
   Funcion Length():
    def length(a):
    i = 0
    if not (isnum(a)):
        for i in range(len(a)):
            i = i + 1
    elif(isnum(a)):
        return(a)
return(i)

#18- 
def solovocales():
        vocales = "aeiouáéíóú"
        if vocal return true
        else vocal return false 
def "solovocales"(j)
     return 

#19-
 def suma(lista_numero):
    resultado=0
    for i in lista_numero:
        resultado+=i
    return resultado

def producto(lista_numero):
    resultado=1
    for i in lista_numero:
        resultado*=i
    return resultado
    
print("Programa para calcular la suma o producto de una lista")

lista=[1,2,3,4]
print("Lista de numeros : ")
print(lista[:])
print("Suma de la lista es: ")
print(suma(lista))
print("Producto de la lista es: ")
print(producto(lista))

#revisar que no compila

#20-def inversa(a):
      trans = ""
      if(isnum(a)):
          print("La entrada es un numero")
          return "Error"
      elif not(isChar(a) and isnum(a)):
          for i in range(len(a)):
              trans = trans + a[(len(a)-1)-i]
          return trans
   
     else:
          print("La entrada no deve ser un numero o una sola letra")

#21-
def es_palindromo(original):
txt=list(palabra)
txt.reverse()
cadena = "".join(txt)
if cadena == original:
print True
else:
print False

#22-
def superPos(a,b):
    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i] == b[j]):
                return True
            else:
                return False
def "superPos"(a,b):
     return 
# no termina de ejecutarse

#23- 
def generarcaracteres (6,"x"):
print letra *veces 
return b 

#24-
def procedimiento(datos):

listado = list(datos)
for i in listado:
print "*"*int(i)

datos = raw_input("Introduce lista de numeros: ")
procedimiento(datos)
#Revisar identacion


#25-
a)
def igualesa(n):
    x = 0
    i = 0
    while i <= n:
        x += i
        i += 1
    return x
b)
def sumara(n):
    if n == 0:
        return 0
    else:
        return n + a(n-1)
c)
def multiplicarangoa(n):
    x = 1
    for i in xrange(n):
        x = x *(i + 1)
    return x
d)
def multiplicaa(n):
    if n <= 1:
        return 1
    else:
        return n * a(n-1)
e)
def devuelvetruea(s):
    if len(s) <= 1:
        return True
    else:
        i = 0
        j = len(s) - 1
        while i < j:
if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True

f)
def devuelveerrora(l,i,j):
    if len(l) == 0:
        return 'Error'
    elif len(l) == 1:
        if i != 0 and j != 0:
            return 'Error'
        else:
            return l[0]
    elif len(l) >= 2:
        if i < 0 or j > len(l)-1:
            return 'Error'
        else:
            return l[i] + l[j]






# 1- imprimir x -> x
def imprimir():
# *—*
    print("hola mundo")
imprimir()


# 2-
def sum(a,b):
    return a+b
print(sum(1,2))
# f: >< — >< — ><

# 3-
def max(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

print(max(7,6))

# 4-
def entre0y10(n):
    return ((n >0) and (n<10))
#f:>< — /B

# 5-
def comparandoUnNumero(a):
    if(a>=1 and a<=10):
        print("Esta entre 1 y 10")
    elif(a>=11 and a<=20):
        print("Esta entre 11 y 20")
    elif(a>=21 and a<=30):
        print("Esta entre 21 y 30")
    else:
        print("No esta en ese rango")
print def comparandoUnNumero # y aca???
# f:>< — string

# 6- 
def entre1y100(i):
    while( i<=100 ):
        print(i)
        i+=1
# f:>< — string
#aca no lo probo, no deberia tomar un valor, y no inicializa

# 7-
def imprime1al100():
    for i in range (1, 100):
        print i
i def imprime1al100

# 8-
def imprimecadacaracter():
    print ("hola mundo")
imprimir ()  
# quizas no esta bien explicada la funcion, pero deberia hace run for para imprimir cada caracter
  
# 9-
def espar(n):
    if(n) par = true 
    else(n) par = false 
#??????????

# 10-
def muestrapares0y100():
    print i in range (1,100):
          print i 
i def imprimepares0y100
#?????

# 11-
def entre0y100(i):
    while( i<=100 ) :
    print i 
i def imprime0y100

#????

print("1 forma")
for i in range(1,100):
    if( (i%2)==0 ):
        print(i)
# 12-
rango = list(range(5,10))
  print(rango)
#genera una lista de numeros, no un numero

# 13-
rango = list(range(10,0,)) 
print(rango)
#aca si

# 14-
cadena1 = input("Dame la primera cadena: ")
cadena2 = input("Dame la segunda cadena: ")
 
print( cadena2[:2] + cadena1[2:] + " " + cadena1[:2] + cadena2[2:] )
# el programa lo hace, pero no es una funcion

# 15-
import random
n=random.randrange(1,100)
nu=int(input('Dime el número que crees que he elegido '))
c=1
while nu!=n:
  c+=1
  if nu>n:
      nu=int(input('El número es mas pequeño'))
  elif nu<n:
      nu=int(input('El número es mas grande'))
print('Felicidades has adivinado que el número secreto es:',n)
print('Y lo has adivinado en',c,'intentos.')def a(n):
    x = 0
    i = 0
    while i <= n:
        x += i
        i += 1
    return x
def a(n):
    x = 0
    i = 0
    while i <= n:
        x += i
        i += 1
    return x
# REvisar

#16-
def mayor3(a,b,c):
    if((a > b) and (a > c)):
        return a
    if((b > a) and (b > c)):
        return b
    if((c > a) and (c > b)):
return c


#17-
Funcion isNum():
      def isnum(a):
      try:
         int(a)
      except:
         return False;
      return True;
   Funcion Length():
    def length(a):
    i = 0
    if not (isnum(a)):
        for i in range(len(a)):
            i = i + 1
    elif(isnum(a)):
        return(a)
return(i)

#18- 
Funcion isChar:
      def isChar(s):
        if(len(s) > 1):
          return False
        if(len(s) == 1):
          return True
    Funcion isVoc:
      def isvoc(s):
        vocales = "aeiouáéíóú"
        if not(isnum(s)) and (isChar(s)):
           for i in range(len(vocales)):
              for j in range(len(s)):
                  if (vocales[i] == s):
                      return True
                  else:
                     return False
        elif(isnum(s)):
            print("El valor es un numero")
        elif not(isChar(s)):
print("El valor no es solo un caracter")

#19-
Solucion:
    def suma(a):
    total = 0
    for i in range(len(a)):
        total += a[i]
    return total

  def mult(a):
    total = 1
    for i in range(len(a)):
        total *= a[i]
    return total
#revisar que no compila

#20-def inversa(a):
      trans = ""
      if(isnum(a)):
          print("La entrada es un numero")
          return "Error"
      elif not(isChar(a) and isnum(a)):
          for i in range(len(a)):
              trans = trans + a[(len(a)-1)-i]
          return trans
   
     else:
          print("La entrada no deve ser un numero o una sola letra")

#21-
def es_palindromo(original):
txt=list(palabra)
txt.reverse()
cadena = "".join(txt)
if cadena == original:
print True
else:
print False

#22-
def superPos(a,b):
    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i] == b[j]):
                return True
            else:
                return False
# no termina de ejecutarse

#23- 
def generarcaracteres (6,"x"):
print letra *veces 
return b 

#24-
def procedimiento(datos):

listado = list(datos)
for i in listado:
print "*"*int(i)

datos = raw_input("Introduce lista de numeros: ")
procedimiento(datos)
#Revisar identacion


#25-
a)
def igualesa(n):
    x = 0
    i = 0
    while i <= n:
        x += i
        i += 1
    return x
b)
def sumara(n):
    if n == 0:
        return 0
    else:
        return n + a(n-1)
c)
def multiplicarangoa(n):
    x = 1
    for i in xrange(n):
        x = x *(i + 1)
    return x
d)
def multiplicaa(n):
    if n <= 1:
        return 1
    else:
        return n * a(n-1)
e)
def devuelvetruea(s):
    if len(s) <= 1:
        return True
    else:
        i = 0
        j = len(s) - 1
        while i < j:
if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True

f)
def devuelveerrora(l,i,j):
    if len(l) == 0:
        return 'Error'
    elif len(l) == 1:
        if i != 0 and j != 0:
            return 'Error'
        else:
            return l[0]
    elif len(l) >= 2:
        if i < 0 or j > len(l)-1:
            return 'Error'
        else:
            return l[i] + l[j]



#f:>< — /B

# 5-
def comparandoUnNumero(a):
    if(a>=1 and a<=10):
        print("Esta entre 1 y 10")
    elif(a>=11 and a<=20):
        print("Esta entre 11 y 20")
    elif(a>=21 and a<=30):
        print("Esta entre 21 y 30")
    else:
        print("No esta en ese rango")
print def comparandoUnNumero # y aca???
# f:>< — string

# 6- 
def entre1y100(i):
    while( i<=100 ):
        print(i)
        i+=1
# f:>< — string
#aca no lo probo, no deberia tomar un valor, y no inicializa

# 7-
def imprime1al100():
    for i in range (1, 100):
        print i
i def imprime1al100

# 8-
def imprimecadacaracter():
    print ("hola mundo")
imprimir ()  
# quizas no esta bien explicada la funcion, pero deberia hace run for para imprimir cada caracter
  
# 9-
def espar(n):
    if(n) par = true 
    else(n) par = false 
#??????????

# 10-
def muestrapares0y100():
    print i in range (1,100):
          print i 
i def imprimepares0y100
#?????

# 11-
def entre0y100(i):
    while( i<=100 ) :
    print i 
i def imprime0y100

#????

print("1 forma")
for i in range(1,100):
    if( (i%2)==0 ):
        print(i)
# 12-
rango = list(range(5,10))
  print(rango)
#genera una lista de numeros, no un numero

# 13-
rango = list(range(10,0,)) 
print(rango)
#aca si

# 14-
cadena1 = input("Dame la primera cadena: ")
cadena2 = input("Dame la segunda cadena: ")
 
print( cadena2[:2] + cadena1[2:] + " " + cadena1[:2] + cadena2[2:] )
# el programa lo hace, pero no es una funcion

# 15-
import random
n=random.randrange(1,100)
nu=int(input('Dime el número que crees que he elegido '))
c=1
while nu!=n:
  c+=1
  if nu>n:
      nu=int(input('El número es mas pequeño'))
  elif nu<n:
      nu=int(input('El número es mas grande'))
print('Felicidades has adivinado que el número secreto es:',n)
print('Y lo has adivinado en',c,'intentos.')def a(n):
    x = 0
    i = 0
    while i <= n:
        x += i
        i += 1
    return x
def a(n):
    x = 0
    i = 0
    while i <= n:
        x += i
        i += 1
    return x
# REvisar

#16-
def mayor3(a,b,c):
    if((a > b) and (a > c)):
        return a
    if((b > a) and (b > c)):
        return b
    if((c > a) and (c > b)):
return c


#17-
Funcion isNum():
      def isnum(a):
      try:
         int(a)
      except:
         return False;
      return True;
   Funcion Length():
    def length(a):
    i = 0
    if not (isnum(a)):
        for i in range(len(a)):
            i = i + 1
    elif(isnum(a)):
        return(a)
return(i)

#18- 
Funcion isChar:
      def isChar(s):
        if(len(s) > 1):
          return False
        if(len(s) == 1):
          return True
    Funcion isVoc:
      def isvoc(s):
        vocales = "aeiouáéíóú"
        if not(isnum(s)) and (isChar(s)):
           for i in range(len(vocales)):
              for j in range(len(s)):
                  if (vocales[i] == s):
                      return True
                  else:
                     return False
        elif(isnum(s)):
            print("El valor es un numero")
        elif not(isChar(s)):
print("El valor no es solo un caracter")

#19-
Solucion:
    def suma(a):
    total = 0
    for i in range(len(a)):
        total += a[i]
    return total

  def mult(a):
    total = 1
    for i in range(len(a)):
        total *= a[i]
    return total
#revisar que no compila

#20-def inversa(a):
      trans = ""
      if(isnum(a)):
          print("La entrada es un numero")
          return "Error"
      elif not(isChar(a) and isnum(a)):
          for i in range(len(a)):
              trans = trans + a[(len(a)-1)-i]
          return trans
   
     else:
          print("La entrada no deve ser un numero o una sola letra")

#21-
def es_palindromo(original):
txt=list(palabra)
txt.reverse()
cadena = "".join(txt)
if cadena == original:
print True
else:
print False

#22-
def superPos(a,b):
    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i] == b[j]):
                return True
            else:
                return False
# no termina de ejecutarse

#23- 
def generarcaracteres (6,"x"):
print letra *veces 
return b 

#24-
def histograma procedimiento():
lista = [4,9,7]

def procedimiento(lis01):

    for i in lis01:
        print ("x"*i)

def "procedimiento" (lista)
     return 

#Revisar identacion


#25-
a)
def igualesa(n):
    x = 0
    i = 0
    while i <= n:
        x += i
        i += 1
    return x
b)
def sumara(n):
    if n == 0:
        return 0
    else:
        return n + a(n-1)
c)
def multiplicarangoa(n):
    x = 1
    for i in xrange(n):
        x = x *(i + 1)
    return x
d)
def multiplicaa(n):
    if n <= 1:
        return 1
    else:
        return n * a(n-1)
e)
def devuelvetruea(s):
    if len(s) <= 1:
        return True
    else:
        i = 0
        j = len(s) - 1
        while i < j:
if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True

f)
def devuelveerrora(l,i,j):
    if len(l) == 0:
        return 'Error'
    elif len(l) == 1:
        if i != 0 and j != 0:
            return 'Error'
        else:
            return l[0]
    elif len(l) >= 2:
        if i < 0 or j > len(l)-1:
            return 'Error'
        else:
            return l[i] + l[j]



