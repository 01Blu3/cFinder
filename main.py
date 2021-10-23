try:
    from flask import Flask, render_template, url_for, flash, redirect, request
except ImportError:
    print("Import Error")

app = Flask(__name__)
app.config['SECRET_KEY'] = '2d6ca153ea201fe4daf5a90f380026b5'


@app.route("/")
def home():
    return render_template('home.html')

# Main Function
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")