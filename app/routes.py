from flask import Blueprint, render_template, request
from .resume_analyzer import analyze_resume
from .ats_checker import check_ats
from .grammar_checker import check_grammar

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        resume_file = request.files['resume']
        feedback = analyze_resume(resume_file)
        ats_score = check_ats(resume_file)
        grammar_feedback = check_grammar(resume_file)
        return render_template('result.html', feedback=feedback, ats_score=ats_score, grammar_feedback=grammar_feedback)
    return render_template('upload.html')


