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

After a sock was selected from the table, you can choose to update it or delete it.

![Screenshot: Sock detail](/github_images/sock_detail_02.png)

`@app.route('/delete', methods=['POST'])`

![Screenshot: Confirm deletion](/github_images/delete_sure.png)

`@app.route('/deletion_result', methods=['POST'])`

![Screenshot: Result](/github_images/result_deleted.png)

`@app.route('/update', methods=['POST'])`

![Screenshot: Update exisitng record](/github_images/update_record.png)

Example of form validation — Flask `flash()` method

This was very hard for me to figure out on this form, which updates an existing record. It was easy as pie for the add-new-record form (below), though.

![Screenshot: Validation message](/github_images/validation.png)

`@app.route('/update_result', methods=['POST'])`

![Screenshot: Result](/github_images/result_updated.png)

`@app.route('/add', methods=['GET', 'POST'])`

This form was a breeze to create, including lots of validation requirements.

![Screenshot: Add new record](/github_images/add_new_record.png)

## Pros and cons

This was hard for me to figure out because the [Flask-WTF](https://flask-wtf.readthedocs.io/) documentation is so minimal, and the [WTForms](https://wtforms.readthedocs.io/) documentation is so verbose.

Validation on a form that started out as blank (add a new record) was quite easy — the biggest challenge was to write the regex strings. (Tip: Use [Pythex](http://pythex.org/).) Flask-WTF has so much built into `wtf.quick_form()` — it's awesome.

Filling the form from an existing database record: I couldn't figure out how to manage that with the quick_form, so I had to work with the `wtf.form_field()` syntax. That wasn't *too* taxing (see [WTForms support](https://pythonhosted.org/Flask-Bootstrap/forms.html) in the Flask-Bootstrap docs) — but using validation with `form.validate_on_submit()` just DID NOT WORK until I realized I had to capture and reuse the values in the form (because I couldn't reload the database record while the user is editing it — the edits would be lost).

Get a value out of a form that was POSTed:

`color = request.form['color']`

Get a value out of a form that has not been submitted:

`color = form.color.data`

Anyway, after a struggle that lasted abut two days, I got it working.

## `flash()`

[Flask message flashing](http://flask.pocoo.org/docs/0.12/patterns/flashing/)

This turned out to be *essential* to displaying validation messages in the form, and it was also pretty tough for me to work through.
