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
