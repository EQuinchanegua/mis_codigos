# Algoritmo para el calculo manual de una raiz cuadrada

## Analisis del problema

Dado un numero real, al cual mediante una serie de procedimiento logicos y matematicos se obtiene un resultado, siendo este ultimo la raiz cuadrada del numero dado

## Variables involucradas en el proceso

a) Número dado: radicando.

b) Raiz Cuadrada.

c) operador auxiliar 1: Doble de la raiz cuadrada.

operador auxiliar 2: ultimo digito evaluador

d) Residuo resta radicando.

e) n_periodos

f) periodo

## lista de procedimientos:

### *1.- Algorimo Calculo_raiz_cuadrada*
### *_2.- declaracion de variables:_*
  2.1- *radicando*

  2.2- *raiz cuadrada*

  2.3- *n_periodos*

  2.4- *periodos*

  2.5- *operador_auxiliar_draiz*

  2.6- *digito_verificador*

  2.7- *residuo*

  2.8- *resultado_auxiliar*


### *3.- inicio del algorimo*
  3.1.- *leer numero dado y asignarlo a variable radicando.*

  3.2.- *contar los digitos del  numero dado desde la derecha y según corresponda hacer:*

   3.2.1.- *Si el numero dado tiene un numero par de digitos asignar tantos periodos por cada dos digitos, y ese numero asignarlo a la variable n_periodos.*

  3.2.2.- *si el numero dado tiene un numero impar de digitos asignar tantos periodos por cada dos digitos, a ese numero agregarle uno más, y ese número asignarlo a la variable n_periodos.*

3.3.- *iniciar a evaluar por el primer periodo, buscando un numero el cual multiplicado por si mismo tiene como resultado un valor menor cercano o igual a este grupo de digitos*


3.2.- *Este numero asignarlo a la variable raiz.*

3.1.- *Restar el producto calculado de la variable raiz.*

3.3.- *hallado este residuo, hacer segun corresponda:*
  
  3.3.1- *si al periodo le sigue un punto o coma decimal: escribir una coma o punto a la derecha de la raiz hallada.*

  3.3.2- *si al periodo no le sigue un punto o coma decimal: continuar al siguiente paso.*

3.4.- *escribir al lado del residuo los digitos del siguiente periodo*

3.5.- *multiplicar el valor de la raiz cuadrada por dos y escribir dicho producto en la zona de operaciones auxiliares.*

3.6- *Del numero formado por el residuo y el siguiente periodo, se toman los dos primeros digitos y se busca un número que multiplicado por si mismo; nos de un numero que se aproxime a este grupo y que si siendo unido a la derecha del doble de la raiz recientemente hallada no sobre pase, o sea igual al numero formado por los digitos del residuo y del periodo.*

3.7.- *multiplicar el numero formado por los digitos del doble de la raiz más el digito del numero anteriormente hallado por el mismo digito.*

3.8.- *restar el producto hallado al numero formado por los digitos del residuo y del periodo, hacer segun sea:*

3.8.1- *si el residuo es menor a cero: buscar otro digito contiguo y realizar el paso 3.6.*

3.8.2.- *si el residuo es mayor,o más cercano o igual a cero: escribir el digito buscado en el paso 3.6  al lado derecho del ultimo digito de la raiz hallada .*

3.9.- *repetir desde el paso 3.3 al 3.8, hasta que se hayan acabado los periodos*

  3.10. *evaluar la raiz hallada: multiplicar el valor hallado po si mismo y agregarle el ultimo residuo hallado y segun sea hacer:*

  3.10.1.- *si el resultado no es igual al numero dado repetir el proceso desde el paso 3.2*

   3.10.2.- *si el resultado es igual al numero dado seguir al paso siguiente.*

3.11- *devolver el valor de la raiz cuadrada hallada al usuario*

3.12.- **fin**
  