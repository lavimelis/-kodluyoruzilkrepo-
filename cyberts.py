import math

def euclideanDistance(point1, point2):
  """
  This function calculates the Euclidean distance between two points.

  Args:
      point1: A tuple representing the first point (x1, y1).
      point2: A tuple representing the second point (x2, y2).

  Returns:
      The Euclidean distance between the two points.
  """
  x1, y1 = point1
  x2, y2 = point2
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Define the list of points
points = [(1, 1), (2, 2), (3, 3), (4, 4)]

# Calculate the distances between all pairs of points
distances = []
for i in range(len(points)):
  for j in range(i + 1, len(points)):
    distance = euclideanDistance(points[i], points[j])
    distances.append(distance)

# Find the minimum distance
min_distance = min(distances)

# Print the minimum distance
print("Minimum distance:", min_distance)