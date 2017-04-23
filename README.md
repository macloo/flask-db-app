# edit-db branch: A Flask app using a MySQL database

This branch will stay apart and separate from *master* because *master* should remain as simple as possible for students to use.

The app file to run in this branch is: *db_app2.py*

It adds new routes to:

* Select a database record for editing or deleting.
* Create a new database record and add it.

All this is done using Flask-SQLAlchemy and Flask-WTF as strictly as I can figure out. I am pretty darned excited about how these things work, especially because they are so fabulously more wonderful than using PHP!

Like the version in *master,* this version depends on the same one-table MySQL database (sockmarket) running in XAMPP on *localhost,* while the Flask app runs on *localhost:5000.*

## What it does

![Screenshot: Index/home](/github_images/index.png)

![Screenshot: List](/github_images/list_by_style.png | width=100)

![Screenshot: Sock detail](/github_images/sock_detail_01.png)

![Screenshot: Table, all socks](/github_images/table.png)

![Screenshot: Sock detail](/github_images/sock_detail_02.png)

![Screenshot: Confirm deletion](/github_images/delete_sure.png)

![Screenshot: Result](/github_images/result_deleted.png)

![Screenshot: Update exisitng record](/github_images/update_record.png)

![Screenshot: Validation message](/github_images/validation.png)

![Screenshot: Result](/github_images/result_updated.png)

![Screenshot: Add new record](/github_images/add_new_record.png)
