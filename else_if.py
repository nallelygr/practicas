usuario_autenticado = False
usuario_admin = False


if usuario_autenticado:
 if usuario_admin:
    print('ACCESO TOTAL')
 else:
    print('Acceso al sistema')
else:
   print('Debes iniciar sesion')

   #ejemplpo con elif
   ocupacion = 'Desempleado'

if ocupacion == 'Estudainte':
   print('Tienes 50% de Descuento')
elif ocupacion == 'jubilado':
   print('Tienes 75% de descuento')
elif ocupacion == 'Desempleado':
    print('Tienes un 10% de descuento')
else:
    print('Debes pagar el 100%')