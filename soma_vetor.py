import threading

# Função que será executada em cada thread
def soma_parcial(numeros, resultado, indice):
    resultado[indice] = sum(numeros)

# Função principal que usa duas threads
def soma_com_duas_threads(lista):
    meio = len(lista) // 2
    resultado = [0, 0]

    # Divide a lista em duas partes
    parte1 = lista[:meio]
    parte2 = lista[meio:]

    # Cria as threads
    t1 = threading.Thread(target=soma_parcial, args=(parte1, resultado, 0))
    t2 = threading.Thread(target=soma_parcial, args=(parte2, resultado, 1))

    # Inicia as threads
    t1.start()
    t2.start()

    # Espera as threads terminarem
    t1.join()
    t2.join()

    # Soma os resultados parciais
    return resultado[0] + resultado[1]

# --------------------------
# Casos de teste
# --------------------------

# Teste 1: Lista pequena
lista1 = [1, 2, 3, 4, 5, 6]
print("Teste 1 - Lista:", lista1)
print("Soma com threads:", soma_com_duas_threads(lista1))
print()

# Teste 2: Lista com 10.000 elementos
lista2 = list(range(1, 10001))  # Soma esperada: 50005000
print("Teste 2 - Lista de 1 a 10000")
print("Soma com threads:", soma_com_duas_threads(lista2))
print()

# Teste 3: Lista com números negativos e positivos
lista3 = [-10, 20, -30, 40, -50, 60]
print("Teste 3 - Lista:", lista3)
print("Soma com threads:", soma_com_duas_threads(lista3))
