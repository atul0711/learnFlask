from flask import Flask, request
import sqlalchemy as db

app = Flask(__name__)

schema = ['id', 'name', 'salary', 'department', 'position', 'hireDate']


@app.route('/webhook/', methods=['GET', 'POST'])
def db_webhook():
    if request.method == 'POST':
        variable_name = request.get_json()
        return f"The name of the student is {variable_name['name']}"
    if request.method == 'GET':
        return "Invoked the GET method"

if __name__ == '__main__':
    app.run(debug=True)
