import math

def Closest_pair(P):

	Sorted_X = SortX(P) #sorting the array in order of the x-coordinates

	if (len(P)<=3) :
		return BaseCase(P) #manually calculating the distance between the points 
		                   #when less than 4 are present

	mid = len(Sorted_X)//2
	median = Sorted_X[mid] #finding median
	L = Sorted_X[:mid]  #splitting array into two halves
	R = Sorted_X[mid:]
		
	dl, plql = Closest_pair(L) #recursively computing the closest pair in each half
	dr, prqr = Closest_pair(R)

	if (dl<dr): #storing the smaller of the distances in the two halves
		d = dl
		p = plql
	else :
		d = dr
		p = prqr
	#checking if the required pair of points lies in the different regions
	Py = []
	for i in range(len(Sorted_X)):
		x_bar = Sorted_X[i]
		if ((x_bar[0]>(median[0]-d)) | (x_bar[0]<(median[0]+d))) : 
			Py.append(x_bar)    #Storing points present only in the central band of width 2d

	Sorted_Y = SortY(Py)  #Sorting in the order of the y-coordinates
	
	#checking if closest pair of points in the central region are closer than the distance d
	for i in range(len(Sorted_Y) - 1):
		for j in range(i+1, min(i+7, len(Sorted_Y))):
			Pm = Sorted_Y[i]
			Qm = Sorted_Y[j]
			dm = Distance(Pm,Qm)
			if dm < d:
				d = dm
				p = Pm,Qm
	
	return d, p
#function to return the minimum between two values
def min(a,b):
	if (a<b):
		return a 
	else:
		return b
#function to sort an array based on its x-coordinates
def SortX(Array):
	if len(Array) == 1:
		return Array
	mid_point = len(Array) // 2
	left_part = Array[:mid_point]
	right_part = Array[mid_point:]

	left_sorted = SortX(left_part)
	right_sorted = SortX(right_part)
	i = j = 0
	C = []

	while i < len(left_sorted) and j < len(right_sorted):
		if left_sorted[i][0] <= right_sorted[j][0]:
			C.append(left_sorted[i])
			i += 1
		elif right_sorted[j][0] < left_sorted[i][0]:
			C.append(right_sorted[j])
			j += 1
	while i < len(left_sorted) and j == len(right_sorted):
		C.append(left_sorted[i])
		i += 1
	while j < len(right_sorted) and i == len(left_sorted):
		C.append(right_sorted[j])
		j += 1
	return C
#function to sort an array based on its y-coordinates
def SortY(Array):
    if len(Array) == 1:
        return Array
    mid_point = len(Array) // 2
    left_part = Array[:mid_point]
    right_part = Array[mid_point:]

    left_sorted = SortY(left_part)
    right_sorted = SortY(right_part)
    
    i = j = 0
    C = []

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i][1] <= right_sorted[j][1]:
            C.append(left_sorted[i])
            i += 1
        elif right_sorted[j][1] < left_sorted[i][1]:
            C.append(right_sorted[j])
            j += 1
    while i < len(left_sorted) and j == len(right_sorted):
        C.append(left_sorted[i])
        i += 1
    while j < len(right_sorted) and i == len(left_sorted):
        C.append(right_sorted[j])
        j += 1
    return C
#BaseCase which manually calculates the distance between points if length of the array<=3
def BaseCase(Array):
	size = len(Array)
	minimum_distance = Distance(Array[0],Array[1])
	Target_Pair = (Array[0],Array[1])
	if size == 2:
	   	return Distance(Array[0],Array[1]),Array[0],Array[1]
	for i in range(0,size):
		for j in range(i+1,size):
			distance = Distance(Array[i],Array[j])
			if distance < minimum_distance:
				minimum_distance = distance
				Target_Pair = (Array[i],Array[j])
	return minimum_distance,Target_Pair
#function to calculate distance between two points
def Distance(P1,P2):
    return math.sqrt((P1[0] - P2[0])**2 + (P1[1] - P2[1])**2)
#arrays
L = [(9,0),(3,1),(4,3),(6,2),(0,1),(0,2)]        #array where closest pair is in the left region
R = [(3, 6),(2,5),(12,30),(1, 30),(8, 4),(1,9)]  #array where closest pair is in the right region
M = [(0,3),(1,5),(9,10),(6,2),(6,3),(10,11)]  #array where each of the pair of points are in the different regions

p, k = Closest_pair(R)
print("Points entered :", M)
print("The pair of closest points are :",k)
print("The distance between the points are :",p,"units")


