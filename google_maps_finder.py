# Google Maps Finder.

import webbrowser

print("Google Maps Finder")
print("-" * 30)

address = input("Enter an address: ")

# Replace spaces with + for URL format.
formatted_address = address.replace(" ", "+")

# Create Google Maps Search URL.
maps_url = "https://www.google.com/maps/search/" + formatted_address

# Opens the location in browser.
webbrowser.open(maps_url)

print("Opening Google Maps...")