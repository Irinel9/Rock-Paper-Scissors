def heading(sign, nr=None):
    lista = ['#' for _ in range(nr)]
    print(*lista, sign, '"')


heading('A', 4)
