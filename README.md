# edit-db branch: A Flask app using a MySQL database

This branch will stay apart and separate from *master* because *master* should remain as simple as possible for students to use.

The app file to run in this branch is: *db_app2.py*

It adds new routes to:

* Select a database record for editing or deleting.
* Create a new database record and add it.

All this is done using Flask-SQLAlchemy and Flask-WTF as strictly as I can figure out. I am pretty darned excited about how these things work, especially because they are so fabulously more wonderful than using PHP!

Like the version in *master,* this version depends on the same one-table MySQL database (sockmarket) running in XAMPP on *localhost,* while the Flask app runs on *localhost:5000.*
