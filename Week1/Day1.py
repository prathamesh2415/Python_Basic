#Welcome Message
print("="*100)
print("Welcome to LinkNest Basic Bookmark Manager")
print("="*100)

#Getting User input
title = ""
url = ""
category = ""

print("1. Add a new bookmark")
print("2. View all Saved bookmarks")
print("3. Search for a bookmark")
print("4. Delete a bookmark")
print("5. Exit the application")
user_input =input()
Bookmark = {"_id": id, 
            "title": title, 
            "url": url,
            "Category": category
            }

while user_input !=5:
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
        Bookmark["_id"] = id
        Bookmark["title"] = title
        Bookmark["url"] = url
        Bookmark["Category"] = category
        print("Bookmark added successfully!")
    elif user_input == "2":
        print("Saved Bookmarks:")
        print(Bookmark)
    elif user_input == "3":
        search_title = input("Enter the title of the bookmark to search: ")
        if search_title == Bookmark["title"]:
            print("Bookmark found:")
            print(Bookmark)
        else:
            print("Bookmark not found.")
    elif user_input == "4":
        delete_title = input("Enter the title of the bookmark to delete: ")
        if delete_title == Bookmark["title"]:
            Bookmark.clear()
            print("Bookmark deleted successfully!")
        else:
            print("Bookmark not found.")
    elif user_input == "5":
        print("Exiting the application. Goodbye!")
    else:
        print("Invalid option. Please try again.")



