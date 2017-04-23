# edit-db branch: A Flask app using a MySQL database

This branch will stay apart and separate from *master* because *master* should remain as simple as possible for students to use.

The app file to run in this branch is: *db_app2.py*

It adds new routes to:

* Select a database record for editing or deleting.
* Create a new database record and add it.

All this is done using Flask-SQLAlchemy and Flask-WTF as strictly as I can figure out. I am pretty darned excited about how these things work, especially because they are so fabulously more wonderful than using PHP!

Like the version in *master,* this version depends on the same one-table MySQL database (sockmarket) running in XAMPP on *localhost,* while the Flask app runs on *localhost:5000.*

## What it does

`@app.route('/', methods=['GET'])`
![Screenshot: Index/home](/github_images/index.png)

`@app.route('/list', methods=['POST'])`
![Screenshot: List](/github_images/list_by_style.png)

`@app.route('/sock/<id>')`
![Screenshot: Sock detail](/github_images/sock_detail_01.png)

`@app.route('/socks', methods=['GET', 'POST'])`

table.html
![Screenshot: Table, all socks](/github_images/table.png)

sock.html
![Screenshot: Sock detail](/github_images/sock_detail_02.png)

`@app.route('/delete', methods=['POST'])`
![Screenshot: Confirm deletion](/github_images/delete_sure.png)

`@app.route('/deletion_result', methods=['POST'])`
![Screenshot: Result](/github_images/result_deleted.png)

`@app.route('/update', methods=['POST'])`
![Screenshot: Update exisitng record](/github_images/update_record.png)

Example of form validation — Flask `flash()` method
![Screenshot: Validation message](/github_images/validation.png)

`@app.route('/update_result', methods=['POST'])`
![Screenshot: Result](/github_images/result_updated.png)

`@app.route('/add', methods=['GET', 'POST'])`
![Screenshot: Add new record](/github_images/add_new_record.png)
