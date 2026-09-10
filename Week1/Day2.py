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
        url = input("Enter the URL of the bookmark: ")
        category = input("Enter the category of the bookmark: ")
        bookmark = {
            "_id": count,
            "title": title,
            "url": url,
            "Category": category
            }
        bookmarks.append(bookmark)
        print("Bookmark added successfully!")
        
    
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
    for item in bookmarks:
        if item.get("title")== search_title:
                print("Bookmark found:")
                print(item)
                break
        else:
            print("Bookmark not found.")

def deleteBookmark():
    delete_title = input("Enter the title of the bookmark to delete: ")
    for item in bookmarks:
        if item.get("title")== delete_title:
                bookmarks.remove(item)
                print("Bookmark deleted successfully!")
                break
        else:
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
