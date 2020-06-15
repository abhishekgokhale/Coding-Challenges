# Coding-Challenges

### 1. Check if the given point lies inside or outside a polygon?

The solution to this challenge can be found in the first.py python file. In this code, inputs are taken in the following order:  
i)   Number of vertices of the polygon.  
ii)  x and y co-ordinates of each of the vertices.  
iii) x and y co-ordinates of the point to check.  

The function 'check_point_inside_polygon(vertices, point_to_check)' takes two parameters which are - list containing all vertices and x,y co-ordinates as [[x1,y1],[x2,y2],....,[xn,yn]] and list containing x,y co-ordinates of the point to check as [x,y].  
The function returns 'True' if the point to check is inside or on the polygon and returns 'False' if it is outside the polygon.

### 2. Calculate the surface of the building exposed to sunlight?

The solution to this challenge can be found in the second.py python file. In this code, inputs are taken in the following order:  
i)   Number of buildings
ii)  x,y co-ordinates of corners of each building in the order: Top-left, Bottom-left, Bottom-right, Top-right
iii) x,y co-ordinates of the source (sun)

The function 'calc_exposed_length(buildings_list, source, no_of_buildings)' takes three parameters which are - list containing all the buildings as [[[x000,y000],[x001,y001],[x010,y010],[x011,y011]],[....],[....], ...., [[],[],[],[xn11,yn11]]] where n = number of buildings and one [[xy][xy][xy][xy]] indicates one building with its four corners. This is the first parameter. Source as [x,y] and no_of_buildings = n are the remaining two parameters to the function.  
The function returns a float value of the total surface exposed to sunlight.
