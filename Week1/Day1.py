#Welcome Message
print("="*100)
print("Welcome to LinkNest Basic Bookmark Manager")
print("="*100)

user_input=''
count =1
Bookmarks =[]


while user_input !='5':
    print("Choose an option:")
    print("1. Add a new bookmark")
    print("2. View all Saved bookmarks")
    print("3. Search for a bookmark")
    print("4. Delete a bookmark")
    print("5. Exit the application")
    user_input =input() 
    if user_input == "1":
        title = input("Enter the title of the bookmark: ")
        url = input("Enter the URL of the bookmark: ")
        category = input("Enter the category of the bookmark: ")
        bookmark = {
            "_id": count,
            "title": title,
            "url": url,
            "Category": category
            }
        Bookmarks.append(bookmark)
        print("Bookmark added successfully!")
        count=count+1
    elif user_input == "2":
        if not Bookmarks:
            print("Bookmark is currently empty. Add Bookmark and try again")
        else:
            print("Saved Bookmarks:")
            for item in Bookmarks:
                print("id       ||",item.get("_id"))
                print("Title    ||",item.get("title"))
                print("URL      ||",item.get("url"))
                print("Category ||",item.get("Category"))
            #print(Bookmarks)
        
    elif user_input == "3":
        search_title = input("Enter the title of the bookmark to search: ")              
        for item in Bookmarks:
                if item.get("title")== search_title:
                    print("Bookmark found:")
                    print(item)
                    break
        else:
            print("Bookmark not found.")

    elif user_input == "4":
        delete_title = input("Enter the title of the bookmark to delete: ")
        for item in Bookmarks:
            if item.get("title")== delete_title:
                Bookmarks.remove(item)
                print("Bookmark deleted successfully!")
                break
        else:
            print("Bookmark not found.")
    elif user_input == "5":
        print("Exiting the application. Goodbye!")

    else:
        print("Invalid option. Please try again.")

