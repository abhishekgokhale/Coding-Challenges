# To run:  python second.py
# Enter coordinates of buildings in the following order: Top-left, bottom-left, bottom-right, top-right


def calc_exposed_length(buildings_list, source, no_of_buildings):
	exposed_length = 0
	buildings = []
	sx, sy = source[0], source[1]

	for k in range(no_of_buildings):													#Sort buildings in order from left to right
		xmin = buildings_list[0][0][0]
		index = 0
		for i in range(len(buildings_list)):
			for j in range(4):
				if(buildings_list[i][j][0] < xmin):
					xmin = buildings_list[i][j][0]
					index = i
		buildings.append(buildings_list[index])
		del buildings_list[index]

	if(sy > buildings[0][0][1]):														#Checking if source is higher than height of the first building
		exposed_length = exposed_length + (buildings[0][0][1] - buildings[0][1][1]) + (buildings[0][3][0] - buildings[0][0][0])			#If yes, add both height and width(top) of the building
	else:
		exposed_length = exposed_length + (buildings[0][0][1] - buildings[0][1][1])														#If not, only add height of the building

	for i in range(no_of_buildings - 1):
		if(sy>buildings[i][3][1]):														#Checking if source is higher than building i
			bx = buildings[i][3][0]
			by = buildings[i][3][1]
			xline = by-sy
			yline = -(bx-sx)
			cline = sy*(bx-sx) - sx*(by-sy)
			if((buildings[i][0][1] - buildings[i][1][1]) < (buildings[i+1][0][1] - buildings[i+1][1][1])):			#Checking if building i+1 is higher than building i
				xnext = buildings[i+1][0][0]
				ynext = (-(xline*xnext) - cline) / yline
				exposed_length = exposed_length + (buildings[i+1][0][1] - ynext) + (buildings[i+1][3][0] - buildings[i+1][0][0])		#If yes, add calculated height exposed and width
			else:
				ynext = buildings[i+1][0][1]
				xnext = (-(yline*ynext) - cline) / xline
				if(xnext>=buildings[i+1][0][0] and xnext<=buildings[i+1][3][0]):
					exposed_length = exposed_length + (buildings[i+1][3][0] - xnext)													#If no, add only calculated width exposed.

		else:																			#Enters else if source is not higher than building i
			if((buildings[i][0][1] - buildings[i][1][1]) < (buildings[i+1][0][1] - buildings[i+1][1][1])):			#Checking if building i+1 is higher than building i
				bx = buildings[i][0][0]
				by = buildings[i][0][1]
				xline = by-sy
				yline = -(bx-sx)
				cline = sy*(bx-sx) - bx*(sy-by)
				xnext = buildings[i+1][0][0]
				ynext = (-(xline*xnext) - cline) / yline
				if(ynext>=buildings[i+1][1][1] and ynext<=buildings[i+1][0][1]):
					exposed_length = exposed_length + (buildings[i+1][0][1] - ynext)								#If yes, add calculated height exposed

	return exposed_length



buildings_list = []
exposed_length = 0
no_of_buildings = int(input("Enter number of buildings:"))
for i in range(no_of_buildings):
	building = []
	for j in range(4):
		print("Enter x y coordinates of corner "+str(j+1)+" of building "+str(i+1)+":")
		x = float(input())
		y = float(input())
		building.append([x,y])
	buildings_list.append(building)

print("Enter x y coordinates of source:")
sx = float(input())
sy = float(input())
source = [sx,sy]

exposed_length = calc_exposed_length(buildings_list, source, no_of_buildings)
print("Total length of buildings exposed to sunlight = "+str(exposed_length))