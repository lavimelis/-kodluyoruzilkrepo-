points = [(1, 2), (3, 4), (5, 6), (7, 8)]  # Noktaları temsil eden liste
def euclideanDistance(point1, point2):

  x1, y1 = point1
  x2, y2 = point2
  distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
  return distance
distances = []  # Mesafeleri saklayacak liste

for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances)  # Minimum mesafeyi bulma

print("Minimum Öklid Mesafesi:", min_distance)  # Minimum mesafeyi yazdırma
