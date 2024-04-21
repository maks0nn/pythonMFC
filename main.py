import coonection
from flask import jsonify
from flask import Flask, render_template, request, redirect, url_for, session, make_response
from collections import defaultdict
import os.path


TEMPLATE_DIR = os.path.abspath('../templates')
STATIC_DIR = os.path.abspath('../static')

app = Flask(__name__)
app.url_map.strict_slashes = False
#lmlmlmllmml

@app.route('/register', methods=["POST", "GET"])
def register_user():
    if request.method == "POST":
        if (len(request.form["login"]) > 6 and len(request.form["fullname"]) > 6
                and len(request.form["password"]) > 6
                and request.form["password"] == request.form["repeat_password"] and not coonection.user_exist(
                    request.form["login"])):
            login = request.form["login"]
            fullname = request.form["fullname"]
            password = request.form["password"]
            print(login)
            print(fullname)
            print(request.form["password"])
            coonection.add_user(login, fullname, password)
            return redirect(url_for('login'))

        else:
            print("Такой пользователь уже существует")
    else:
        print("не метод пост")
    return render_template("register.html", title="Register")


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]
        session['login'] = login
        if coonection.login_user(login, password):
            return redirect('/menu')
            print('redirect to menu')
        print('**--**')
    return render_template("login.html", title="Login")


@app.route('/logout', methods=["POST", "GET"])
def logout():
    session.clear()
    return redirect('/login')


@app.route('/menu', methods=["POST", "GET"])
def menu():
    login = session['login']
    # old_grades=coonection.get_mark_where_user_srvises_indicator(login)
    # indicator=coonection.get_all_indicator();
    # if indicator:
    #     indicator, _ = zip(*(indicator,indicator))

    # # new_grades=coonection.add_new_mark(login)
    # if new_grades:
    #     _, _,new_grades=zip(*(new_grades))
    # new_grades_dict=defaultdict(list)
    # for new_grades_dict in new_grades_dict:
    #     new_grades_dict[new_grades_dict].append(new_grades_dict)
    mark = coonection.get_mark_where_user_srvises_indicator(login)
    print(mark)
    print(coonection.get_all_servises())
    print(coonection.get_all_indicator())

    return render_template('menu.html',fullname=coonection.get_name(login),mark=coonection.get_mark_where_user_srvises_indicator(login),
                           indicators=coonection.get_all_indicator(), servises=coonection.get_all_servises())





@app.route('/api')
def api():
    data = {
        "id": 123,
        "name": "vasa",
        "surname": "Pupkin"
    }
    print(len(coonection.get_all_indicator()))

    return jsonify(coonection.get_all_indicator())



@app.route('/admin', methods=["POST", "GET"])
def admin():
    login = session['login']


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
