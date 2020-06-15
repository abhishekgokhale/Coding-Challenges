def check_point_inside_polygon(vertices, point_to_check):

	lines = []
	for i in range(len(vertices)):
		x1 = vertices[i][0]
		y1 = vertices[i][1]
		x2 = vertices[(i+1)%len(vertices)][0]
		y2 = vertices[(i+1)%len(vertices)][1]
		xc = y2-y1
		yc = -(x2-x1)
		c = y1*(x2-x1) - x1*(y2-y1)
		line = [xc,yc,c]															#Forming equations of all sides of the polygon
		lines.append(line)

		if(((xc*point_to_check[0] + yc*point_to_check[1] + c) == 0)):					#Checking whether point is on the lines of sides
			if(point_to_check[0]<=max(x1,x2) and point_to_check[0]>=min(x1,x2) and point_to_check[1]<=max(y1,y2) and point_to_check[1]>=min(y1,y2)):	#Check whether point is on sides
				return True					#If yes, return True
			else:
				return False				#If no, return False

	no_of_intersections = 0
	flag = 0

	for i in range(len(lines)):
		x = point_to_check[0]
		if(lines[i][1] != 0):
			y = -(lines[i][0]*x + lines[i][2]) / lines[i][1]
			xmax = max(vertices[i][0], vertices[(i+1)%len(vertices)][0])
			xmin = min(vertices[i][0], vertices[(i+1)%len(vertices)][0])
			ymax = max(vertices[i][1], vertices[(i+1)%len(vertices)][1])
			ymin = min(vertices[i][1], vertices[(i+1)%len(vertices)][1])
			if((x >= xmin and x <= xmax) and (y >= ymin and y <= ymax)):
				if(y <= point_to_check[1]):
					if([x,y] in vertices):
						flag = flag+1
					no_of_intersections = no_of_intersections+1

	no_of_intersections = no_of_intersections - flag/2

	if(no_of_intersections%2==0):
		return False
	else:
		return True



vertices = []
num_vertices = int(input("Enter number of vertices to input:"))
for i in range(num_vertices):
	x = float(input("Enter x coordinate for vertex "+str(i+1)+":"))
	y = float(input("Enter y coordinate for vertex "+str(i+1)+":"))
	vertex = [x,y]
	vertices.append(vertex)

xcheck = float(input("Enter x coordinate for point to check:"))
ycheck = float(input("Enter y coordinate for point to check:"))
point_to_check = [xcheck,ycheck]

isInside = check_point_inside_polygon(vertices, point_to_check)

print(isInside)
if(isInside):
	print("The point is inside the polygon")
else:
	print("The point is outside the polygon")	