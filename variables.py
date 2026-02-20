vi = 2
print("vi:",vi,"la , añade automaticamente un espacio")
print("type(vi):", type(vi))
vf = 2.0
print("vi:",vf)
print("type(vf):", type(vf))

vb = True #Ejemplo de comentario: En Python True/False se escribe la primera en mayusculas
print("vb:",vb)
print("type(vb):", type(vb))

vs = "Hola"
print("vs:",vs)
print("type(vs):", type(vs))


fecNAc= input("En que año naciste ?")
print("En 2026 tendras", 2026 - int(fecNAc),"años")

print("Tipo de fecNac:", type(fecNAc))
fecNAc = 2000
print("Tipo de fecNac:", type(fecNAc))


vf = float("2.3")
print("vf: ", vf)
vf = 3.4
vi = int(vf)
print("vi: " , vi)
vi =int(float("2.3"))
print("vi:" ,vi)


#Operadores
a = 5
b = 2
c = a + b
print("c:", c)
c= a / b
print("c: ", c)
c= a // b
print("c: ", c)
c= a % b
print("c: ", c)
c= a ** b
print("c: ", c)


#Operadores relacionales
c= a < b
print("c: ", c)
c= a != b
print("c: ", c)

#Operadores logicos
c= True or False
print("c: ", c)
c= True and False
print("c: ", c)

# () -> Mult -> Aditivos -> Relacionales -> Logicos
c= (a + b) * a + a**b + a < 100 and a * b < 50
c1= (a + b) * a + a**(b + a)
print("c1: ", c1)
print("c: ", c)


#Cadenas de caracteres
a = "Hola"
b = "que tal"
c = a + ' ' + b + "!"
print("c: ", c)
c = a*5
print("c: ", c)
c = '$'.join(a)
print("c: ", c)

a = 2
a = a + 1
a = '+'
c = a == '+'
print("c: ", c)


num1= input("Numero 1: ")
num2= input("Numero 2: ")
num3 = num1 + num2
print("Suma:",num3)


num1= input("Numero 1: ")
num2= input("Numero 2: ")
num3 = num1 * num2
print("Multi:",num3)



