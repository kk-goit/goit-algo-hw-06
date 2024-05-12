# goit-algo-hw-06
Графи

## Завдання 1
* task1.py

### Результат
```
Graph have 12 nodes and 17 edges and is connected
Degree Centrality: {'A': 0.1818, 'B': 0.2727, 'C': 0.2727, 'D': 0.3636, 'E': 0.2727, 'G': 0.2727, 'L': 0.2727, 'K': 0.1818, 'F': 0.2727, 'I': 0.2727, 'J': 0.2727, 'M': 0.1818}
Average shotests path: 2.1515
```

## Завдання 2
* task2.py

### Результат
```
DFS path: A B D G C L M I E F J K 
BFS path: A B C D E L G F K I M J 
```

### Висновки
1. Алгоритм пошуку в глибину (DFS) пішов по графу від вершини до вершини пока не зустріне "тупік" (в нашому грвфі таких немає, усі вершини мають не меньше двох ребер) чи вершину в якій вже був
2. Алгорим пошуку в ширину (BFS) спочатку обходить усі ребра поточної вершини, лише потів обходить ребра зв'язаних вершин (якщо він ше не бачих їх раніше)

## Завдання 3
* task3.py

### Результат
```
A -> 'A':  0, 'B':  2, 'C': 10, 'D':  4, 'E':  4, 'G':  6, 'L': 13, 'K':  5, 'F':  5, 'I':  5, 'J':  6, 'M': 10
B -> 'A':  2, 'B':  0, 'C':  8, 'D':  2, 'E':  2, 'G':  4, 'L': 11, 'K':  3, 'F':  3, 'I':  3, 'J':  4, 'M':  8
C -> 'A': 10, 'B':  8, 'C':  0, 'D':  6, 'E':  8, 'G':  4, 'L': 10, 'K':  7, 'F':  7, 'I':  9, 'J':  8, 'M': 14
D -> 'A':  4, 'B':  2, 'C':  6, 'D':  0, 'E':  2, 'G':  2, 'L':  9, 'K':  1, 'F':  1, 'I':  3, 'J':  2, 'M':  8
E -> 'A':  4, 'B':  2, 'C':  8, 'D':  2, 'E':  0, 'G':  4, 'L': 11, 'K':  3, 'F':  1, 'I':  1, 'J':  2, 'M':  6
G -> 'A':  6, 'B':  4, 'C':  4, 'D':  2, 'E':  4, 'G':  0, 'L':  7, 'K':  3, 'F':  3, 'I':  5, 'J':  4, 'M': 10
L -> 'A': 13, 'B': 11, 'C': 10, 'D':  9, 'E': 11, 'G':  7, 'L':  0, 'K': 10, 'F': 10, 'I': 10, 'J': 11, 'M':  5
K -> 'A':  5, 'B':  3, 'C':  7, 'D':  1, 'E':  3, 'G':  3, 'L': 10, 'K':  0, 'F':  2, 'I':  2, 'J':  1, 'M':  7
F -> 'A':  5, 'B':  3, 'C':  7, 'D':  1, 'E':  1, 'G':  3, 'L': 10, 'K':  2, 'F':  0, 'I':  2, 'J':  1, 'M':  7
I -> 'A':  5, 'B':  3, 'C':  9, 'D':  3, 'E':  1, 'G':  5, 'L': 10, 'K':  2, 'F':  2, 'I':  0, 'J':  1, 'M':  5
J -> 'A':  6, 'B':  4, 'C':  8, 'D':  2, 'E':  2, 'G':  4, 'L': 11, 'K':  1, 'F':  1, 'I':  1, 'J':  0, 'M':  6
M -> 'A': 10, 'B':  8, 'C': 14, 'D':  8, 'E':  6, 'G': 10, 'L':  5, 'K':  7, 'F':  7, 'I':  5, 'J':  6, 'M':  0
```
