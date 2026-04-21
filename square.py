from time import sleep
from os import system, name

# look at this ugly nerdy code

def bresenham_line(array, pt0, pt1):
  x0, y0 = pt0
  x1, y1 = pt1
  dx = abs(x1 - x0)
  dy = abs(y1 - y0)
  x, y = x0, y0
  sx = 1 if x0 < x1 else -1
  sy = 1 if y0 < y1 else -1

  if dx > dy:
    err = dx / 2.0
    while x != x1:
      if 0 <= y < len(array) and 0 <= x < len(array[0]):
        array[y][x] = '█'
      err -= dy
      if err < 0:
        y += sy
        err += dx
      x += sx
  else:
    err = dy / 2.0
    while y != y1:
      if 0 <= y < len(array) and 0 <= x < len(array[0]):
        array[y][x] = '█'
      err -= dx
      if err < 0:
        x += sx
        err += dy
      y += sy
  if 0 <= y < len(array) and 0 <= x < len(array[0]):
    array[y][x] = '█'

def bresenham_coordinates(pt0, pt1):
  points = []
  x0, y0 = pt0
  x1, y1 = pt1
  dx = abs(x1 - x0)
  dy = abs(y1 - y0)
  x, y = x0, y0
  sx = 1 if x0 < x1 else -1
  sy = 1 if y0 < y1 else -1

  if dx > dy:
    err = dx / 2.0
    while x != x1:
      points.append((x, y))
      err -= dy
      if err < 0:
        y += sy
        err += dx
      x += sx
  else:
    err = dy / 2.0
    while y != y1:
      points.append((x, y))
      err -= dx
      if err < 0:
        x += sx
        err += dy
      y += sy
  points.append((x, y))
  return points

def monitor(lines):
  system("cls" if name == "nt" else "clear")
  array = [[' ']*15 for i in range(15)]

  for i in lines:
    bresenham_line(array, i[0], i[1])

  for i in array:
    print(*i, sep='')
  sleep(0.25)
  

deg = (0, 14), (14, 14), (14, 0), (0, 0)

while True:
  for p1, p2, p3, p4 in zip(*[bresenham_coordinates(deg[i-1], deg[i]) for i in range(4)]):
    monitor(((p1, p2), (p2, p3), (p3, p4), (p4, p1)))
