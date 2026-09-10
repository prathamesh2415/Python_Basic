Bookmarks= [{'_id': 1, 'title': 'google', 'url': 'google.com', 'Category': 'search engine'}, {'_id': 2, 'title': 'yotube', 'url': 'yotube.com', 'Category': 'meia'}]

searchResult ="google"

for item in Bookmarks:
    for keys,value in item.items():
        if keys=="title" and value == searchResult:
            print("Found")
            break
        else:
            print("Bookmark not found")