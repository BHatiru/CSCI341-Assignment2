from flask import render_template, redirect, request, url_for, flash
from flaskApp import app, db 


from flaskApp.models import User, Caregiver, Member
from flaskApp.forms import UserForm, CaregiverForm, MemberForm




@app.route('/')
def home():
    return render_template('home.html')

@app.route('/users', endpoint='user_list')
def user_list():
    users = User.query.all()
    form = UserForm()
    return render_template('User/user.html', users=users, form=form, formC=CaregiverForm(), formM=MemberForm())

@app.route('/caregivers')
def caregiver_list():
    caregivers = Caregiver.query.all()
    form = CaregiverForm()
    return render_template('Caregiver/caregiver.html', caregivers=caregivers, form=form)


@app.route('/members')
def member_list():
    members = Member.query.all()
    form = MemberForm()
    return render_template('Member/member.html', members=members, form=form)

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
    return render_template('User/user.html', form=form, formC=CaregiverForm(), formM=MemberForm(),users=User.query.all())


@app.route('/add_caregiver/<int:user_id>', methods=['GET','POST'])
def add_caregiver(user_id):
    formCare = CaregiverForm()
    if formCare.validate_on_submit():
        new_caregiver = Caregiver(
            caregiver_user_id=user_id,
            photo=formCare.photo.data,
            gender=formCare.gender.data,
            caregiving_type=formCare.caregiving_type.data,
            hourly_rate=formCare.hourly_rate.data
        )
        db.session.add(new_caregiver)
        db.session.commit()
        flash('Caregiver added successfully', 'success')
        return redirect(url_for('user_list'))
    return render_template('User/user.html', form=UserForm(),formC=formCare,formM=MemberForm(), users=User.query.all())

@app.route('/add_member/<int:user_id>', methods=['GET','POST'])
def add_member(user_id):
    formMem = MemberForm()
    if formMem.validate_on_submit():
        new_member = Member(
            member_user_id=user_id,
            house_rules=formMem.house_rules.data
        )
        db.session.add(new_member)
        db.session.commit()
        flash('Member added successfully', 'success')
        return redirect(url_for('user_list'))
    return render_template('User/user.html', form=UserForm(),formC=CaregiverForm(), formM=formMem, users=User.query.all())


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

@app.route('/edit_caregiver/<int:caregiver_user_id>', methods=['GET', 'POST'])
def edit_caregiver(caregiver_user_id):
    caregiver = Caregiver.query.get_or_404(caregiver_user_id)
    form = CaregiverForm(obj=caregiver)
    if form.validate_on_submit():
        caregiver.photo = form.photo.data
        caregiver.gender = form.photo.data
        caregiver.caregiving_type = form.caregiving_type.data
        caregiver.hourly_rate = form.hourly_rate.data
        db.session.commit()

        flash('Caregiver updated successfully', 'success')
        return redirect(url_for('caregiver_list'))
    return render_template('Caregiver/edit_caregiver.html', form=form, caregiver=caregiver)

@app.route('/edit_member/<int:member_user_id>', methods=['GET', 'POST'])
def edit_member(member_user_id):
    member = Member.query.get_or_404(member_user_id)
    form = MemberForm(obj=member)
    if form.validate_on_submit():
        member.house_rules = form.house_rules.data
        db.session.commit()

        flash('Member updated successfully', 'success')
        return redirect(url_for('member_list'))
    return render_template('Member/edit_member.html', form=form, member=member)

@app.route('/delete_user/<int:user_id>', methods=['GET', 'POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully', 'success')
    return redirect(url_for('user_list'))


@app.route('/delete_caregiver/<int:caregiver_user_id>', methods=['GET', 'POST'])
def delete_caregiver(caregiver_user_id):
    caregiver = Caregiver.query.get_or_404(caregiver_user_id)

    db.session.delete(caregiver)
    db.session.commit()
    flash('Caregiver deleted successfully', 'success')
    return redirect(url_for('caregiver_list'))

@app.route('/delete_member/<int:member_user_id>', methods=['GET', 'POST'])
def delete_member(member_user_id):
    member = Member.query.get_or_404(member_user_id)

    db.session.delete(member)
    db.session.commit()
    flash('Member deleted successfully', 'success')
    return redirect(url_for('member_list'))

@app.route('/search_users', methods=['GET'])
def search_users():
    attribute = request.args.get('attribute')
    value = request.args.get('value')

    form = UserForm()
    users = User.query.filter(User.__dict__[attribute].like(f'%{value}%')).all()

    return render_template('User/user.html', users=users, form=form)

@app.route('/search_caregivers', methods=['GET'])
def search_caregivers():
    attribute = request.args.get('attribute')
    value = request.args.get('value')

    form = CaregiverForm()
    caregivers = Caregiver.query.filter(Caregiver.__dict__[attribute].like(f'%{value}%')).all()

    return render_template('Caregiver/caregiver.html', caregivers=caregivers, form=form)

@app.route('/search_members', methods=['GET'])
def search_members():
    attribute = request.args.get('attribute')
    value = request.args.get('value')

    form = MemberForm()
    members = Member.query.filter(Member.__dict__[attribute].like(f'%{value}%')).all()

    return render_template('Member/member.html', members=members, form=form)

