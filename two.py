#2) Dado a sequência de Fibonacci, 
# onde se inicia por 0 e 1 e o próximo valor 
# sempre será a soma dos 2 valores anteriores
#  (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a 
# sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

#resposta da 2
def fibonacci(n):
    
    fib = [0, 1]

    # Calcula os próximos valores da sequência
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])

    
    return fib


num = int(input("Informe um número: "))


fib = fibonacci(num)


if num in fib:
    print(f"{num} pertence à sequência de Fibonacci!")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")



