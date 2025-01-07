from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')  # Home page of the portfolio


@app.route('/about')
def about():
    return render_template('about.html')  # About page (optional)

@app.route('/projects')
def projects():
    project_list = [
        {"title": "Project 1", "description": "A cool project", "link": "#"},
        {"title": "Project 2", "description": "Another cool project", "link": "#"},
        {"title": "Project 3", "description": "Yet another project", "link": "#"},
    ]
    return render_template('projects.html', projects=project_list)


@app.route('/contact')
def contact():
    return render_template('contact.html')  # Contact page


if __name__ == "__main__":
    app.run(debug=True)
