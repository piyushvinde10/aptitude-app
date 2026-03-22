# app/routes/student.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import Question, Result

student = Blueprint('student', __name__)


@student.route('/student/dashboard')
@login_required
def dashboard():
    # Block admin from accessing student pages
    if current_user.role == 'admin':
        return redirect(url_for('admin.dashboard'))
    results = Result.query.filter_by(user_id=current_user.id).all()
    return render_template('student/dashboard.html', results=results)


@student.route('/student/take_test', methods=['GET', 'POST'])
@login_required
def take_test():
    if current_user.role == 'admin':
        return redirect(url_for('admin.dashboard'))

    questions = Question.query.all()

    if request.method == 'POST':
        score = 0
        total = len(questions)

        for q in questions:
            selected = request.form.get(f'question_{q.id}')
            if selected and selected.lower() == q.correct_option.lower():
                score += 1

        # Save result to database
        result = Result(score=score, total=total, user_id=current_user.id)
        db.session.add(result)
        db.session.commit()

        flash(f'Test submitted! You scored {score}/{total}', 'success')
        return redirect(url_for('student.result', score=score, total=total))

    return render_template('student/take_test.html', questions=questions)


@student.route('/student/result')
@login_required
def result():
    if current_user.role == 'admin':
        return redirect(url_for('admin.dashboard'))
    score = request.args.get('score', 0, type=int)
    total = request.args.get('total', 0, type=int)
    return render_template('student/result.html', score=score, total=total)


@student.route('/student/my_results')
@login_required
def my_results():
    if current_user.role == 'admin':
        return redirect(url_for('admin.dashboard'))
    results = Result.query.filter_by(user_id=current_user.id).all()
    return render_template('student/my_results.html', results=results)