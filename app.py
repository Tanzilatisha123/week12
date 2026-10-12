from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("register.html")
@app.route('/register', methods=['POST'])
def register():
    name = request.form['username']
    password = request.form['password']
    return render_template('sucessful.html',name=name,password=password)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
