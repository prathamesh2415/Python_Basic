import re


#Welcome Message
print("="*100)
print("Welcome to LinkNest Basic Bookmark Manager")
print("="*100)
count=1
user_input=''
bookmarks =[]

def showMenu():
    print("Choose an option:")
    print("1. Add a new bookmark")
    print("2. View all Saved bookmarks")
    print("3. Search for a bookmark")
    print("4. Delete a bookmark")
    print("5. Exit the application")


def addBookmark(count_val,bookmarks_val):
        count=count_val
        bookmarks=bookmarks_val
        title = input("Enter the title of the bookmark: ")
        if not title:
            print(f"Error : The field {"\033[31m"}Title{"\033[0m"} is empty!!")   
        
        while title == '':    
            title = input("Enter the title of the bookmark: ")
        
        url = input("Enter the URL of the bookmark: ")
        if not url:
            print(f"Error : The field {"\033[31m"}Url{"\033[0m"} is empty!!")
        
        while url == '':
            url = input("Enter the URL of the bookmark: ")
            
        
        category = input("Enter the category of the bookmark: ")
        if not category:
            print(f"Error : The field {"\033[31m"}Category{"\033[0m"} is empty!!")
        
        while category=='':
            category = input("Enter the category of the bookmark: ") 
        
        isValid = urlValidation(url)
        while isValid == False:
             url = input("Enter the URL of the bookmark: ")
             isvalid =urlValidation(url)
             if isvalid == True:
                  break
        bookmark = {
            "_id": count,
            "title": title,
            "url": url,
            "Category": category
            }
        #isValid=validation(bookmark)
        #if isValid == False:
        #    exit()
        bookmarks.append(bookmark)
        print("Bookmark added successfully!")
'''        
def validation(bookmark):
    missing = [name for name , value in bookmark.items() if not value]
    if missing:
         print(f"The following fields are empty :{', '.join(missing)}")
         return False
    else:
         return True 
'''
def urlValidation(url):
    regex_pattern = "^(https?:\/\/)?(www\.)?([a-zA-Z0-9-]+)(\.[a-zA-Z0-9-]+)+(\/[a-zA-Z0-9-._~:/?#[\]@!$&'()*+,;=]*)?$"
    if re.match(regex_pattern,url):
          print(f"valid Url")
          valdation = True
    else:
          print(f"Invalid Url")
          valdation = False
    
    return valdation

def viewBookmark():
    if not bookmarks:
        print("Bookmark is currently empty. Add Bookmark and try again")
    else:
        print("Saved bookmarks:")
        for item in bookmarks:
            print("id       ||",item.get("_id"))
            print("Title    ||",item.get("title"))
            print("URL      ||",item.get("url"))
            print("Category ||",item.get("Category"))
            print("="*50)
        
def searchBookmark():
    search_title = input("Enter the title of the bookmark to search: ")
    found =False              
    for item in bookmarks:
        if item.get("title")== search_title:
                print("Bookmark found:")
                print(item)
                found = True
                break
    if found is False:
        print("Bookmark not found.")

def deleteBookmark():
    delete_title = input("Enter the title of the bookmark to delete: ")
    found =False 
    for item in bookmarks:
        if item.get("title")== delete_title:
                bookmarks.remove(item)
                print("Bookmark deleted successfully!")
                found = True
                break
    if found is False:
        print("Bookmark not found.")


while user_input !='5':
    showMenu()
    user_input =input() 
    if user_input == "1":
        addBookmark(count,bookmarks)
        count=count+1
    elif user_input == "2":
        viewBookmark()
    elif user_input == "3":
        searchBookmark()
    elif user_input == "4":
         deleteBookmark()
    elif user_input == "5":
        print("Exiting the application. Goodbye!")
    else:
        print("Invalid option. Please try again.")
