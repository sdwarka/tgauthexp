from flask import render_template, url_for, redirect, request, flash
from flask_login import login_required
from datetime import datetime
from .models import Expense
from app import db
from . import exp

######################################################
# displays the add_expense.html input page
######################################################
@exp.route('/add', methods=['GET'])
@login_required
def add_expense_input():
    return render_template('add_exp.html')

######################################################
# processes the expense data submitted from the add_expense.html input page
######################################################
@exp.route('/add', methods=['POST'])
@login_required
def add_expense_process():
    
    # local var
    exp_data = request.form
    
    # TODO: validate the expense data
    print("add_expense_process: TODO validate expense data")
    
    # create an expense record using the POST data
    dtformat = '%Y-%M-%d'
    dt   = datetime.strptime(exp_data['v_exp_date'], dtformat)
    cat  = exp_data['v_exp_head']
    desc = exp_data['v_desc']
    amt  = exp_data['v_amt' ]
    typ  = exp_data['v_exp_type']
    mode = exp_data['v_pay_mode']
    rem  = exp_data['v_remarks' ]

    exp_record = Expense(exp_date=dt, exp_catg=cat, exp_desc=desc,
        exp_amt=amt, exp_type=typ, exp_mode=mode, exp_rem=rem)

    # store the validated expense record in the database
    print(f'storing expense {exp_data}')
    db.session.add(exp_record)
    db.session.commit()

    # redirect to the view expenses page
    return redirect(url_for('exp.view'))

######################################################
# view list of expenses
######################################################
@exp.route('/view', methods=['GET'])
@login_required
def view():
    
    # Fetch data from database and display
    exps = Expense.query.all()
    return render_template('view_exp.html', exp_data=exps)
