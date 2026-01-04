# Doc2Doc makes using markdown a breeze. This includes adding images to markdown documents.

# Complete the create_markdown_image function using currying. It takes a string input, alt_text.

# Enclose the alt_text in square brackets prefixed with an exclamation point ![alt_text].
# Define an inner function that also takes a string input, url:
# The inner function should first escape any parentheses in the URL by replacing them with encoded sequences.
# Use the .replace() string method to change any opening parenthesis ( into %28.
# Do the same to change any closing parenthesis ) into %29.
# Enclose the url with parentheses (url).
# Add the enclosed url to the end of the enclosed alt_text: ![alt_text](url)
# Define the innermost function. It should take an optional string input for the title (title=None).
# If a title is passed:
# Enclose it in double quotes.
# Then add the quoted title to the image syntax by first removing the closing parenthesis ) from the end of the image syntax.
# Add a space and the quoted title with a closing parenthesis ) to the end of the image syntax: ![alt_text](url "title")
# Return the finished image syntax.
# Return the innermost function
# Return the inner function




def create_markdown_image(alt_text):
    image = ""
    alt_text=f"![{alt_text}]"
    def add_url(url):
        nonlocal alt_text
        print("before: ", url)
        url = url.replace("(", "%28")
        url = url.replace(")", "%29")
        url = f"({url})"
        print("🪩", url)
        image = alt_text + url
        def add_title(title =None):
            nonlocal image
            if title:
                title = "\"" + title + "\""
                # print("❤️‍🔥", image)
                image = image.replace(")", " ") + title + ")"
            return image            
        return add_title        
    return add_url
