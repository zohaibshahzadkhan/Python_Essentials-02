collectionOfBooks = ["react", "python", "javascript"];
print('Enter the name of the book');

bookToBeChecked = input();
for book in collectionOfBooks:
  if bookToBeChecked == book:
    print("Book available");
    break;  
else:
    print("Book not available");