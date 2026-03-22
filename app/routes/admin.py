# app/routes/admin.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import Question, Result, User

admin = Blueprint('admin', __name__)


def admin_required(f):
    """Decorator to block non-admins from admin pages."""
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            flash('Access denied! Admins only.', 'danger')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated


@admin.route('/admin/dashboard')
@login_required
@admin_required
def dashboard():
    total_questions = Question.query.count()
    total_students  = User.query.filter_by(role='student').count()
    total_results   = Result.query.count()
    return render_template('admin/dashboard.html',
                           total_questions=total_questions,
                           total_students=total_students,
                           total_results=total_results)


@admin.route('/admin/add_question', methods=['GET', 'POST'])
@login_required
@admin_required
def add_question():
    if request.method == 'POST':
        question_text  = request.form.get('question_text')
        option_a       = request.form.get('option_a')
        option_b       = request.form.get('option_b')
        option_c       = request.form.get('option_c')
        option_d       = request.form.get('option_d')
        correct_option = request.form.get('correct_option')

        new_q = Question(
            question_text=question_text,
            option_a=option_a,
            option_b=option_b,
            option_c=option_c,
            option_d=option_d,
            correct_option=correct_option
        )
        db.session.add(new_q)
        db.session.commit()

        flash('Question added successfully! ✅', 'success')
        return redirect(url_for('admin.add_question'))

    return render_template('admin/add_question.html')


@admin.route('/admin/manage_questions')
@login_required
@admin_required
def manage_questions():
    questions = Question.query.all()
    return render_template('admin/manage_questions.html', questions=questions)


@admin.route('/admin/delete_question/<int:q_id>')
@login_required
@admin_required
def delete_question(q_id):
    question = Question.query.get_or_404(q_id)
    db.session.delete(question)
    db.session.commit()
    flash('Question deleted.', 'info')
    return redirect(url_for('admin.manage_questions'))


@admin.route('/admin/view_results')
@login_required
@admin_required
def view_results():
    results = Result.query.all()
    return render_template('admin/view_results.html', results=results)


@admin.route('/admin/view_students')
@login_required
@admin_required
def view_students():
    students = User.query.filter_by(role='student').all()
    return render_template('admin/view_students.html', students=students)