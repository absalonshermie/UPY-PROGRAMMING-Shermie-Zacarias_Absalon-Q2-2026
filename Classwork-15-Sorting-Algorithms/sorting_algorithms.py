import random
import stddraw
from color import Color

# BUBBLE SORT
def bubble_sort(numbers):
    n = len(numbers)
    for sweep in range(n):
        for pair in range( 0, n-1 - sweep):
            if numbers[pair] > numbers[pair + 1]:
                numbers[pair], numbers[pair + 1] = numbers[pair+1], numbers[pair]

def bubble_sort_animated(numbers):
    # CONFIG - Canvas
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)
    
    for sweep in range(n):
        for pair in range( 0, n-1 - sweep):
            draw_bars(numbers, selected=(pair, pair + 1))
            if numbers[pair] > numbers[pair + 1]:
                numbers[pair], numbers[pair + 1] = numbers[pair+1], numbers[pair]
                draw_bars(numbers, selected=(pair, pair + 1))
                
    draw_bars(numbers)
    stddraw.show(2000) 

# SELECTION SORT
def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

def selection_sort_animated(numbers):
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            draw_bars(numbers, selected=(min_idx, j))
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
        draw_bars(numbers, selected=(i, min_idx))
        
    draw_bars(numbers)
    stddraw.show(2000)

# INSERTION SORT
def insertion_sort(numbers):
    n = len(numbers)
    for i in range(1, n):
        j = i
        while j > 0 and numbers[j - 1] > numbers[j]:
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            j -= 1

def insertion_sort_animated(numbers):
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)
    
    for i in range(1, n):
        j = i
        while j > 0 and numbers[j - 1] > numbers[j]:
            draw_bars(numbers, selected=(j - 1, j))
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            draw_bars(numbers, selected=(j - 1, j))
            j -= 1
            
    draw_bars(numbers)
    stddraw.show(2000)

# DRAW BARS FUNCTION
def draw_bars(numbers, selected=()):
    stddraw.clear()
    n = len(numbers)
    bar_width = 10.0 / n
    
    for i, number in enumerate(numbers):
        x = i * bar_width + bar_width / 2
        color = Color(255, 90, 90) if i in selected else Color(70, 130, 220)
        stddraw.setPenColor(color)
        stddraw.filledRectangle(x - bar_width / 2, 0, bar_width * 0.9, number)
    stddraw.show(500)
    
# MAIN EXECUTION
# Creamos la lista original una sola vez
original_numbers = [random.randint(0,100) for x in range(10)]
print(f"Lista original desordenada: {original_numbers}")

# 1. Bubble Sort
print("Ejecutando Bubble Sort...")
# Enviamos una copia para que la lista original no se modifique
list_for_bubble = original_numbers.copy()
bubble_sort_animated(list_for_bubble)

# 2. Selection Sort
print("Ejecutando Selection Sort...")
list_for_selection = original_numbers.copy()
selection_sort_animated(list_for_selection)

# 3. Insertion Sort
print("Ejecutando Insertion Sort...")
list_for_insertion = original_numbers.copy()
insertion_sort_animated(list_for_insertion)

print("¡Todas las animaciones finalizaron!")

# Esto mantiene la ventana abierta al final de todo el programa
stddraw.show()