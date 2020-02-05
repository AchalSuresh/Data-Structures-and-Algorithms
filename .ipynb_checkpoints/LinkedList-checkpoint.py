class Node(object):

	'''
	The class defines the Node object for a linked list along with functions to return the data, returns the next node
	and assigns the pointer to next node
	'''
	def __init__(self,data=None,next_node=None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_next(self,new_next):
		self.next_node = new_next


class LinkedList(object):
	"""Define class for LinkedList"""
	def __init__(self, head =None):
		self.head = head

	def print_list(self):
		current = self.head

		while current:
			print(current.get_data())
			current = current.get_next()
		

	# Function to insert data at Head of a linked list
	def insert(self,data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node

	# Function to count the number of data.
	def count(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.get_next()
		return count

	#function to delete a element
	def delete(self,data):

		current = self.head
		previous = None
		found = False

		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				previous = current
				current = current.get_next()

			if current is None:
				raise ValueError("Data not in list")

			if previous is None:
				self.head = current.get_next()

			else:
				previous.set_next(current.get_next())


	def search(self,data):

		current = self.head
		found = False

		while current and found is False:
			if current.get_data() == data:
				found = True

			else:
				current = current.get_next()

		return current



Itemlist =LinkedList()

Itemlist.insert(32)
Itemlist.insert(64)
Itemlist.insert(98)
Itemlist.print_list()
Itemlist.count()
Itemlist.search(64)
