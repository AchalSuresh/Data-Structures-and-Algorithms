def MergeSort(dataset):

	if len(dataset) > 1:
	# Divide the array into 2 equal halves	
		mid = len(dataset) // 2
		leftarray = dataset[:mid]
		rightarray = dataset[mid:]

		#keep diving the array till only one element left
		MergeSort(leftarray)
		MergeSort(rightarray)

		#create indexes to store values of each array
		i=0 #left array
		j=0 #right array
		k=0 #new array

		# Comparision between element in i and j
		while i<len(leftarray) and j<len(rightarray):
			if leftarray[i]< rightarray[j]:
				dataset[k] = leftarray[i]
				i += 1

			else:
				dataset[k] = rightarray[j]
				j += 1

			k+=1

		#fill up dataset with remaining elements
		while i < len(leftarray):
			dataset[k] = leftarray[i]
			i += 1
			k += 1

		while j < len(rightarray):
			dataset[k] = rightarray[j]
			j += 1
			k += 1


items = [8, 4 , 23, 17 , 9, 10, 46, 55]
print(items)
MergeSort(items)
print(items)
