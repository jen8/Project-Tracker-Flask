from flask import Flask, request, render_template

import hackbright


app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    # get_grades_by_github is a function in hackbright.py 
    grades = hackbright.get_grades_by_github(github)
    first, last, github = hackbright.get_student_by_github(github)
    # Added grades variable in our student_info.html
    
    html = render_template("student_info.html", first=first, last=last, github=github, grades=grades)
    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-add-form")
def student_form():
    """Display new student form. Add a new student."""

    return render_template("student_form.html")

@app.route("/student-add", methods=['POST'])
def confirm_student_add():
    """Add a student. Tell student they have been successfully added."""

    first_name = request.form.get("fname")
    last_name = request.form.get("lname")
    github_name = request.form.get("github")


# make_new_student is a FUNCTION in hackbright.py file: look inside the 
    # first thing and give me the second thing(ie:make_new_student.)
    hackbright.make_new_student(first_name, last_name, github_name)

# name is from jinja and first_name is variable from variable request.form.get
# request.form.get is form POST methods.
# when using POST method(pass it as argument in decorator: methods=['POST'], 
    # use request.form.get,in html type method=POST)
    return render_template("greet_student.html", name=first_name, github=github_name)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
