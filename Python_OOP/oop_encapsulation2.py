class Blog:
    
    def __init__(self):
        self.__author = "Mike"
        self.__titles = []

    def __print_title_and_author(self):
        print("title : {}, author : {}\n".format(self.__titles, self.__author))

    def add_title(self, title):
        self.__titles.append(title)
        print("Finish adding title!")
        self.__print_title_and_author()


blog = Blog()
# blog.__print_title_and_author()  # error
blog._Blog__print_title_and_author()

blog.add_title("Python")

print("blog.__dict__ : {}".format(blog.__dict__))

