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
    return render_template('User/user.html', users=users, form=form)

# @app.route('/caregivers', endpoint='caregiver_list')
# def caregiver_list():
#     caregivers = Caregiver.query.all()
#     form = CaregiverForm()
#     return render_template('Caregiver/caregiver.html', caregivers=caregivers, form=form)

@app.route('/add_user', methods=['GET','POST'])
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
    return render_template('User/user.html', form=form, users=User.query.all())

@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
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
        return redirect(url_for('user_list'))
    return render_template('User/edit_user.html', form=form, user=user)

@app.route('/delete_user/<int:user_id>', methods=['GET', 'POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully', 'success')
    return redirect(url_for('user_list'))


@app.route('/search_users', methods=['GET'])
def search_users():
    attribute = request.args.get('attribute')
    value = request.args.get('value')

    form = UserForm()
    users = User.query.filter(User.__dict__[attribute].like(f'%{value}%')).all()

    return render_template('User/user.html', users=users, form=form)

