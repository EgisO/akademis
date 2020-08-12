from flask import Flask, render_template, request, redirect, url_for
import forms

app = Flask(__name__)

@app.route('/',methods=['GET'])
def homepage():
    if (request.method == 'GET'):
        return render_template('homepage.html')


@app.route("/register", methods=['GET', 'POST'])
def register():

    if request.method == 'GET':
        return render_template('register.html')

    elif request.method == 'POST':
        if(request.form['register_button']) == 'Register':
            username = request.form.get('add_username')
            password = request.form.get('add_password')
            obj = forms.Users()
            obj.register_user(username,password)
            return redirect(url_for('homepage'))


@app.route("/login",methods=['GET','POST'])
def login():
    if(request.method == 'GET') :
        return render_template('login.html')
    else:
        if(request.form['login_button']) == 'Login':
            username = request.form.get('login_username')
            password = request.form.get('login_password')
            obj = forms.Users()
            data = obj.login_user(username, password)
            if (data):
                return redirect(url_for('profile'))
            else:
                return redirect(url_for('login'))


@app.route("/profile", methods=['GET', 'POST'])
def profile():

    if request.method == 'GET':
        obj = forms.Profile()
        name, _tags = obj.get_profile()
        return render_template('profile.html', _tags = _tags, get_name=name)

    elif request.method == 'POST':
        if(request.form['name_button']) == 'Name':
            username = request.form.get('get_name')
            obj = forms.Profile()
            obj.update_name(username)
            return redirect(url_for('profile'))
        if(request.form['name_button']) == 'Tag':
            print('HERE1')
            tag = request.form.get('get_tags')
            print('HERE2')
            obj = forms.Profile()
            print('HERE3')
            obj.update_tags(tag)
            print('HERE')
            return redirect(url_for('profile'))
        else:
            print('ANNEN')
            username = request.form.get('get_name')
            print(username)
            return redirect(url_for('profile'))


if __name__ == "__main__":
    app.run()