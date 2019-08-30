from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route("/Home")
def Home():
	return render_template('TrangChu.html')

@app.route("/SignUp")
def SignUp():
	return render_template('DangKy.html')

@app.route("/SignIn")
def SignIn():
	return render_template('DangNhap.html')

@app.route("/login", methods=['POST'])
def login():
	_ID = request.form['id']
	_password = request.form['password']
	
	if _ID == 'admin'and _password == 'admin' :
		session['id'] = _ID
		return 'Success!!!'
	else:
		return 'Faile!!!'

@app.route("/logout", methods=["POST"])
def logout():
	if 'id' in session:
		session.pop('id',None)
		return 'logout Success'
	else: 
		return 'do not login'

@app.route("/")
def welcome():
	return Home()

if __name__ == '__main__':
	app.run(host='localhost',port=5000,debug=True)
