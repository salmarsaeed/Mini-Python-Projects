books = []

# إضافة كتاب جديد
book_name = input("Enter the name of your book: \n")
author = input("Enter the author of your book (or press enter to skip): \n")
books.append({"name": book_name, "author": author})

# إضافة كتاب تتمنى الحصول عليه
wish_book = input("Enter the name of a book you wish to have in the future: \n")
wish_author = input("Enter the author of the book you wish to have in the future (or press enter to skip): \n")
books.append({"name": wish_book, "author": wish_author, "wish": True})

# إضافة كتاب من قائمة الأحلام حصلت عليه
obtained_book = input("Enter a book from your dream list that you have obtained (or press enter to skip): \n")
if obtained_book:
    books.append({"name": obtained_book, "author": "", "obtained": True})

# عرض كل الكتب في المكتبة
print("\nYour Library:")
for book in books:
    if book.get("wish"):
        print(f"- (Wish) {book['name']} by {book['author'] or 'Unknown'}")
    elif book.get("obtained"):
        print(f"- (Obtained) {book['name']}")
    else:
        print(f"- {book['name']} by {book['author'] or 'Unknown'}")