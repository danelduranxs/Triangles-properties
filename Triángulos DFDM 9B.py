print()
print("¡Calculadora de Triángulos!")
print()
print("(Por Daniel Felipe Durán Martínez)")
print()
print("(Solo escribir valores numéricos.)")

lado_a= float(input("Por favor determine un valor para un lado del triángulo:"))
print()
lado_b= float(input("Por favor determine el segundo valor de un lado del triángulo:"))
print()
lado_c= float(input("Por favor determine el tercer valor de un lado del triángulo:"))
print()

print()

if lado_a <= 0 or lado_b<=0 or lado_c<=0:
    print("El triángulo no puede existir ya que uno o más de sus lados son 0 o tienen un valor negativo (osea no existente). Por lo tanto, el perímetro no se puede sacar.")
elif lado_a >= lado_b + lado_c or lado_b >= lado_a + lado_c or lado_c >= lado_b+lado_a:
    print("El triángulo no puede existir ya que uno de los lados es mayor que la suma de los otros 2 lados. Por lo tanto, el perímetro no se puede sacar.")
elif lado_a==lado_b==lado_c:
    print("El triángulo es Equlátero ya que todos sus lados son iguales. Además, el perímetro es",lado_a + lado_b + lado_c, ".")
elif lado_a != lado_b == lado_c or lado_b != lado_a == lado_c or lado_c != lado_a==lado_b:
    print("El triángulo es isoceles ya que solo 2 lados son iguales. Además, el perímetro es", lado_a + lado_b  + lado_c, ".")
elif lado_a != lado_b != lado_c:
    print("El triángulo es escaleno ya que los lados no son iguales. Además, el perímetro es", lado_a + lado_b + lado_c, ".")
    


    
input("(Presione ENTER para finalizar)")
    
    




    