from flask import Flask,render_template
app = Flask(__name__)
  
  
@app.route('/about/<username>')
def about_user(username):
      return f'<h1>This is about the page of {username}</h1>'
  
@app.route('/about')
def about_page():
    return '<h1>About Page</h1>'

@app.route('/')
def home_page():
    return render_template('home.html')
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)