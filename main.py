"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI

    print('lado 1')
    l1 = float(input('> '))

    print('Lado 2')
    l2 = float(input('> '))

    print('Lado 3')
    l3 = float(input('> '))

    if l1 <= 0 or l2 <= 0 or l3 <= 0 :
      print('Os valores informados não formam um triângulo.')
      return

    if l1 >=(l2 + l3) or l2 >=(l1 + l3) or l3 >=(l1 + l2):
      print('Os valores informados não formam um triângulo.')
      return
      
    if l1 == l2 == l3:
      print('O triângulo é equilátero.')
    elif l1 == l2 or l2 == l3 or l3 == l1:
      print('O triângulo é isósceles.')
    else:
      print('O triângulo é escaleno.')


if __name__ == '__main__':
    main()
