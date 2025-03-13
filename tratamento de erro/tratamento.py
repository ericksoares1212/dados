while True:
  try:
      n1 = int(input('\ndigite um numero '))
      n2 = int(input('\ndigite outro numero '))
      conta = n1 / n2
#Erro para acaso houver divisão com 0 
  except ZeroDivisionError:
    print('\nnao divida por ZERO')
#erro a caso digite numeros float ou strings
  except ValueError:
    print('\nuse apenas numeros inteiros')
#se não houver os problemas acima vai funcionar normalmente
  else:
    print('\na divisao entre os numeros {} e {} é {:.1f}'.format(n1 , n2 , conta))
    break
