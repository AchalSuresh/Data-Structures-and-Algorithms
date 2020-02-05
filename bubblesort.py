
def bubblesort(dataset):

	for i in range(len(dataset)-1, 0 ,-1):
		for j in range(i):
			if dataset[j] > dataset[j+1]:
				temp = dataset[j]
				dataset[j] = dataset[j+1]
				dataset[j+1] = temp

			print("The updated List is ",dataset)



list1 = [3,8,23,4,7,1]
bubblesort(list1)
print(list1)