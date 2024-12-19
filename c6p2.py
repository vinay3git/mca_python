class Book:
	def __init__(self, publisher_id, publisher_name, title, author, price, no_of_pages):
		self.publisher_id = publisher_id
		self.publisher_name = publisher_name
		self.title = title
		self.author = author
		self.price = price
		self.no_of_pages = no_of_pages

	def display(self):
		print("\n")
		print(f"Publisher ID: {self.publisher_id}")
		print(f"Publisher Name: {self.publisher_name}")
		print(f"Title: {self.title}")
		print(f"Author: {self.author}")
		print(f"Price: {self.price}")
		print(f"Number of Pages: {self.no_of_pages}")

if __name__ == "__main__":
	publisher_id = input("Enter Publisher ID: ")
	publisher_name = input("Enter Publisher Name: ")
	title = input("Enter Book Title: ")
	author = input("Enter Author Name: ")
	price = float(input("Enter Book Price: "))
	no_of_pages = int(input("Enter Number of Pages:"))

	book = Book(publisher_id, publisher_name, title, author, price, no_of_pages)
	book.display()
