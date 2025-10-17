
# Rafael Gonzalez Reyes                  Examen primer parcial              13 de octubre del 2025 

def really_simple_sort(A):
    n = len(A)
    k = 0
    
    #contar cuántos son 1
    for i in range(n):
        if A[i] == 1:
            k += 1
    
    #poner los 1 al inicio
    for i in range(k):
        A[i] = 1
    
    #poner los 2 después de los 1
    for i in range(k, n):
        A[i] = 2
    
    return A

rss = [2, 1, 2, 1, 1, 1, 2, 1, 2]
sorted_arr = really_simple_sort(rss)
print(sorted_arr) 


