#Login Registration

1. Create database (`login_reg_db`) [X]
  + `users`
    + `first_name`
    + `last_name`
    + `email`
    + `pw_hash`
    + `created_at`
    + `updated_at`
2. Create a Flask application
    + Routing
      + `/` (GET) render a page with login/registration forms
      + `/login` (POST) log a registered user in
      + `/register` (POST) register a new user AND log them in
      + `/accounts` (GET) welcome page
    + Validations
    + PW hashing
    + Flash messaging
3. Front-end
  + `index.html` (login and registration forms)
  + `welcome.html` (welcome a logged in user)
