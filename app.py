from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/blogs/research-1')
def research_1():
    return render_template('research_1.html')

@app.route('/blogs/research-2')
def research_2():
    return render_template('research_2.html')

@app.route('/blogs/research-3')
def research_3():
    return render_template('research_3.html')

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
