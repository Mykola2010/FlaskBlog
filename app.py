from flask import Flask, render_template, abort
from init_db import create_mock_data
from db import get_db_connection

app = Flask(__name__)
create_mock_data()
@app.get("/")
def index():
    connection = get_db_connection()
    posts = connection.execute("SELECT * FROM posts").fetchall()
    print(posts)
    connection.close()
    return render_template("index.html", posts=posts)

@app.get("/<int:post_id>")
def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute("SELECT * FROM posts WHERE id=?", (post_id,)).fetchone()
    connection.close()
    if post is None:
        abort(404)
    return render_template("post.html", post=post)

if __name__ == '__main__':
    app.run(port=8080, debug=True)