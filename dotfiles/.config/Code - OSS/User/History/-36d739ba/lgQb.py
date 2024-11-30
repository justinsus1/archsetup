import mechanize

# Create a browser object
br = mechanize.Browser()

# Open the Python website
br.open("https://www.python.org")

# Select the first form on the page (search form)
br.select_form(nr=0)

# Fill in the search query
br["q"] = "pycon"

# Submit the form
response = br.submit()

# Print the response content (HTML of the search results page)
print(response.read())
