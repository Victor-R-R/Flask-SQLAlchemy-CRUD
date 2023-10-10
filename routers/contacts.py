from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils.db import db
from models.contact import Contact

contacts = Blueprint('contacts', __name__)


@contacts.route('/')
def home():
    contactos = Contact.query.all()
    return render_template('index.html', contactos=contactos)


@contacts.route('/new', methods=['POST'])
def add_contact():

    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']
    new_contact = Contact(fullname, email, phone)

    print(new_contact)

    db.session.add(new_contact)
    db.session.commit()

    flash("Contacto añadido")

    return redirect(url_for('contacts.home'))


@contacts.route('/update/<id>', methods=['POST', 'GET'])
def update_contact(id):
    contact = Contact.query.get(id)
    if request.method == 'POST':
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']

        db.session.commit()

        flash("Contacto actualizado")

        return redirect(url_for('contacts.home'))

    return render_template('update.html', contact=contact)


@contacts.route('/delete/<id>')
def delete_contact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    flash("Contacto eliminado")
    return redirect(url_for('contacts.home'))


@contacts.route('/about')
def about():
    return render_template('about.html')
