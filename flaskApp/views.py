from flask import render_template, redirect, request, url_for, flash
from flaskApp import app, db 


from flaskApp.models import User
from flaskApp.forms import UserForm


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/users', endpoint='user_list')
def user_list():
    users = User.query.all()
    form = UserForm()
    return render_template('user.html', users=users, form=form)

@app.route('/add_user', methods=['POST'])
def add_user():
    
    form = UserForm()
    if form.validate_on_submit():
        new_user = User(
            email=form.email.data,
            given_name=form.given_name.data,
            surname=form.surname.data,
            city=form.city.data,
            phone_number=form.phone_number.data,
            profile_description=form.profile_description.data,
            password=form.password.data
        )
        db.session.add(new_user)
        db.session.commit()
        flash('User added successfully', 'success')
        return redirect(url_for('user_list'))
    return render_template('user.html', form=form, users=User.query.all())

@app.route('/edit_user', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    form = UserForm(obj=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.given_name = form.given_name.data
        user.surname = form.surname.data
        user.city = form.city.data
        user.phone_number = form.phone_number.data
        user.profile_description = form.profile_description.data
        user.password = form.password.data
        db.session.commit()
        flash('User updated successfully', 'success')
        return render_template('user.html', users=User.query.all(), form=form)
    return render_template('edit_user.html', form=form, user=user)

@app.route('/delete_user', methods=['GET', 'POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('user_list'))