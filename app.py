from flask import Flask, render_template, abort
import os
import markdown2

app = Flask(__name__)

# Blog metadata
blogs = [
    {
        'slug': 'llama3_vision_gcp_app',
        'title': 'Llama3.2 in action for Vision',
        'description': 'A proof of concept utilizing the Llama3.2 model, GCP, and Chainlit to create a vision-based chatbot.'
    }
    
]

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Blogs overview route
@app.route('/blogs')
def show_blogs():  # Renamed the function here
    return render_template('blogs.html', blogs=blogs)

# Dynamic blog route that renders a blog based on its slug (the name in URL)
@app.route('/blogs/<slug>')
def blog_post(slug):
    # Try to find the blog metadata by slug
    blog = next((blog for blog in blogs if blog['slug'] == slug), None)
    
    if blog:
        # Assuming you store markdown files named after the slug
        markdown_file_path = os.path.join('blogs', f'{slug}.md')

        if os.path.exists(markdown_file_path):
            # Read and convert markdown file
            with open(markdown_file_path, 'r') as file:
                markdown_content = file.read()
                content_html = markdown2.markdown(markdown_content)

            return render_template('blog_template.html', blog=blog, content=content_html)
        else:
            abort(404, description="Blog content not found")
    else:
        abort(404, description="Blog not found")

@app.route('/gcp-solutions')
def gcp_solutions():
    return render_template('gcp_solutions.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
