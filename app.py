from flask import Flask, render_template_string
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    # Original HTML content to be modified
    html_content = """
    <html>
        <head><title>My Website</title></head>
        <body>
            <h1>Welcome to My Website</h1>
            <p>This is some sample text.</p>
        </body>
    </html>
    """

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Modify the HTML using BeautifulSoup
    new_paragraph = soup.new_tag("p")
    new_paragraph.string = "Here is a new paragraph added with BeautifulSoup!"
    soup.body.append(new_paragraph)

    # Render the modified HTML back to the user
    return render_template_string(str(soup))

if __name__ == '__main__':
    app.run(debug=True)
