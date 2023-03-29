import queue
import time
import random

#radix_sort
def base_changer(numar, baza):
    sir = ""
    i = 1
    nr = len(str(baza-1))
    while numar:
        sir = str(numar % baza) + sir
        while i*nr != len(sir):
            sir = '0' + sir
        numar //= baza
        i += 1
    return int(sir)

def radix_sort(vector, baza):
    l = [queue.Queue() for i in range (baza)]
    b = len(str(baza-1))
    maxim = len(str(max(vector))) // b + 1
    digit = 1
    while digit <= maxim:
        for numar in vector:
            if digit == 1:
                d = numar % (10**b)
            else:
                d = (numar % (10 ** (digit * b))) // (10 ** ((digit - 1) * b))
            l[d].put(numar)
        vector.clear()
        for coada in l:
            while not coada.empty():
                vector.append(coada.get())
        digit += 1
    return vector

#merge_sort
def merge_sort(vector):
    if len(vector) > 1:
        mijloc = len(vector) // 2
        dreapta = vector[mijloc:]
        stanga = vector[:mijloc]
        merge_sort(dreapta)
        merge_sort(stanga)
        i = j = k = 0
        while i < len(stanga) and j < len(dreapta):
            if stanga[i] <= dreapta[j]:
                vector[k] = stanga[i]
                i += 1
            else:
                vector[k] = dreapta[j]
                j += 1
            k += 1
        while i< len(stanga):
            vector[k] = stanga[i]
            k += 1
            i += 1
        while j< len(dreapta):
            vector[k] = dreapta[j]
            k += 1
            j += 1

#shell_sort
def shell_sort(vector, n):
    distanta = n // 2
    while distanta > 0:
        j = distanta
        while j < n:
            i = j - distanta
            while i >= 0:
                if vector[i+distanta] <= vector[i]:
                    aux = vector[i+distanta]
                    vector[i+distanta] = vector[i]
                    vector[i] = aux
                else:
                    break
                i -= distanta
            j += 1
        distanta //= 2
    return vector

#quick_sort
def partitii(vector, stanga, dreapta):
    pivot = vector[dreapta]
    i = stanga - 1
    for j in range(stanga, dreapta):
         if vector [j] <= pivot:
              i += 1
              aux = vector[i]
              vector[i] = vector[j]
              vector[j] = aux
    aux = vector[i+1]
    vector[i+1] = vector[dreapta]
    vector[dreapta] = aux
    return i + 1

def quick_sort(vector, stanga, dreapta):
     if stanga < dreapta:
          x = partitii(vector, stanga, dreapta)
          quick_sort(vector, stanga, x  - 1)
          quick_sort(vector, x + 1, dreapta)

#counting_sort
def counting_sort(vector, mx):
    frecventa = [0 for i in range(mx)]
    vector_sortat = []
    for i in vector:
        frecventa[i] += 1
    for i in range (mx):
        while frecventa[i] != 0:
            vector_sortat.append(i)
            frecventa[i] -= 1
    return vector_sortat

f = open('teste_radix_sort', 'r')
s = f.readline().split()
numar_teste = int(s[0])
vector_teste_radix_sort = []
for i in range (numar_teste):
    s = f.readline().split()
    for i in range (3):
        s[i] = int(s[i])
    vector_teste_radix_sort.append(s)

f = open('teste_merge_shell_quick_counting', 'r')
s = f.readline().split()
numar_teste = int(s[0])
vector_teste = []
for i in range (numar_teste):
    s = f.readline().split()
    for i in range (2):
        s[i] = int(s[i])
    vector_teste.append(s)

for i in vector_teste_radix_sort:
    N = i[0]
    maxim = i[1]
    baza = i[2]
    test = []
    for j in range (N):
        test.append(random.randint(1, maxim))
    if baza != 10:
        for j in range (N):
            test[j] = base_changer(test[j], baza)
    start = time.time()
    test = radix_sort(test, baza)
    stop = time.time()
    print(f'La radix_sort, pentru lista de {N} numere in baza {baza} generate random pana la {maxim}, testul a durat {stop-start} secunde.', end = ' ')
    if (test == sorted(test)):
        print('Test reusit.')
    else:
        print('Test picat.')

for i in vector_teste:
    N = i[0]
    maxim = i[1]
    test = []
    for j in range (N):
        test.append(random.randint(0, maxim))
    aux = test.copy()
    start = time.time()
    merge_sort(test)
    stop = time.time()
    print(f'La merge_sort, pentru lista de {N} numere generate random pana la {maxim}, testul a durat {stop-start} secunde.', end = ' ')
    if (test == sorted(test)):
        print('Test reusit.')
    else:
        print('Test picat.')
    test = aux.copy()
    start = time.time()
    shell_sort(test, len(test))
    stop = time.time()
    print(f'La shell_sort, pentru lista de {N} numere generate random pana la {maxim}, testul a durat {stop-start} secunde.', end = ' ')
    if (test == sorted(test)):
        print('Test reusit.')
    else:
        print('Test picat.')
    test = aux.copy()
    start = time.time()
    quick_sort(test, 0, len(test)-1)
    stop = time.time()
    print(f'La quick_sort, pentru lista de {N} numere generate random pana la {maxim}, testul a durat {stop-start} secunde.', end = ' ')
    if (test == sorted(test)):
        print('Test reusit.')
    else:
        print('Test picat.')
    test = aux.copy()
    start = time.time()
    counting_sort(test, maxim)
    stop = time.time()
    print(f'La counting_sort, pentru lista de {N} numere generate random pana la {maxim}, testul a durat {stop-start} secunde.', end = ' ')
    if (test == sorted(test)):
        print('Test reusit.')
    else:
        print('Test picat.')
