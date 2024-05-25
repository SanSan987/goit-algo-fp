import heapq

class Graph:
    def __init__(self):
        self.edges = {}
        self.vertices = set()

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.edges:
            self.edges[from_vertex] = []
        if to_vertex not in self.edges:
            self.edges[to_vertex] = []
        self.edges[from_vertex].append((to_vertex, weight))
        self.vertices.add(from_vertex)
        self.vertices.add(to_vertex)

def dijkstra(graph, start):
    # Ініціалізація відстаней до всіх вершин як нескінченність
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start] = 0
    priority_queue = [(0, start)]  # Пріоритетна черга, ініціалізується з початковою вершиною
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Якщо поточна дистанція більша за записану, пропускаємо її
        if current_distance > distances[current_vertex]:
            continue
        
        # Оновлюємо дистанції до сусідів
        for neighbor, weight in graph.edges.get(current_vertex, []):
            distance = current_distance + weight
            
            # Якщо знайдено коротший шлях до сусіда
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Приклад використання
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)

print(f"Найкоротші шляхи від вершини {start_vertex}:")
for vertex in distances:
    print(f"Від {start_vertex} до {vertex}: {distances[vertex]}")


# Результат виконання (один прклад, копія з терміналу):
# Найкоротші шляхи від вершини A:
# Від A до D: 4
# Від A до B: 1
# Від A до C: 3
# Від A до A: 0