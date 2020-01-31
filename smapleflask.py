from flask import jsonify
from flask import Flask, render_template, request
from flask import g

app = Flask(__name__)

@app.route('/_get_current_user')
def get_current_user():
    return jsonify(username=g.user.username,
                   email=g.user.email,
                   id=g.user.id)

if __name__ == '__main__':
    app.run()