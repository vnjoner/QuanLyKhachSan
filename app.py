from flask import Flask, render_template
app = Flask(__name__)


@app.route("/Home")
def Home():
	return render_template('TrangChu.html')

@app.route("/SignUp")
def SignUp():
	return render_template('DangKy.html')

@app.route("/SignIn")
def SignIn():
	return render_template('DangNhap.html')

@app.route("/")
def main():
	return Home()
