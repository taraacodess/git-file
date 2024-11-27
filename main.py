class Author:

    def __init__(self,name, author):
        self.name=name
        self.author=author

    def fav_book(self):
        print("my fav book is", self.name)
        print("by", self.author)


Book= Author("Rust","BR")
Book.fav_book()    