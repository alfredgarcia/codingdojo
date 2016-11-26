#Full Friends

1. Create a database (`friends`)
  + Single Table (`friends`)
    + `first_name`
    + `last_name`
    + `email`
    + `created_at`
2. Create a server (Flask)
  + Routing
    + `/` (GET) show all friends plus form to create new friend
    + `/friends` (POST) create a friend
    + `/friends/<id>` (POST) update a friend
    + `/friends/<id>/edit` (GET) show a form to edit a friend
    + `/friends/<id>/delete` (POST) delete a friend
3. Front end
  + `templates`
    + `index.html`
    + `edit.html`
