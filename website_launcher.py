# Website Launcher.

import webbrowser

# Predefined list of websites.
websites = {
    "1": "https://www.google.com",
    "2": "https://www.github.com",
    "3": "https://www.youtube.ccom",
    "4": "https://www.python.org"
}

print("Website Launcher")
print("-" * 30)

# Display available websites.
for key, value in websites.items():
    print(f"{key}, {value}")

print("5. Enter custom website")

choice = input("\nChoose a website to open: ")

# Open predefined websites.
if choice in websites:
    webbrowser.open(websites[choice])

# Open custom website.
elif choice == '5':
    url = input("Enter website URL: ")
    if not url.startswith('http'):
        url = 'https://' + url
    
    webbrowser.open(url)

else:
    print("Invalid Choice.")