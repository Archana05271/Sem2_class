class Library:
    def issue_book(self,book_name,user):
        return f"Book issued : {book_name} to {user}"
    def return_book(self,book_name,user):
        return f"Book returned : {book_name} by {user}"

class DigiLibrary(Library):
    def issue_book(self,book_name,user):
        return f"Book issued : {book_name} to {user}"
    def return_book(self,book_name,user):
        return f"Book returned : {book_name} by {user}"
lib=Library()
dig=DigiLibrary()

book=input()
username=input()

print(lib.issue_book(book,username))
print(lib.return_book(book,username))

print(dig.issue_book(book,username))
print(dig.return_book(book,username))

lib.issue_book(book,username)
dig.issue_book(book,username)



