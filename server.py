from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def show_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    try:
         with open('/Users/NidaKhan/PycharmProjects/MyProject/webserver/database.csv','a',newline='') as database2:
                email=data["email"]
                subject=data["subject"]
                message=data["message"]
                # file=database2.write(f'\n{email},{subject},{message}')
                csv_writer=csv.writer(database2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL )
                csv_writer.writerow([email,subject,message])

    except FileNotFoundError as err:
        print((err))

def write_to_file(data):
    try:
         with open('/Users/NidaKhan/PycharmProjects/MyProject/webserver/database.txt',mode='a') as database:
                email=data["email"]
                subject=data["subject"]
                message=data["message"]
                file=database.write(f'\n{email},{subject},{message}')
    except FileNotFoundError as err:
        print((err))

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data=request.form.to_dict()
        # print(data)
        # write_to_file(data)
        write_to_csv(data)
    return redirect('/thankyou.html')

# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None,post_id=None):
#     return render_template('index1.html',name=username,post_id=post_id)
#
# @app.route('/blog')
# def hello_blog():
#     return 'Welcome to my first Blog!!'
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
# @app.route('/works.html')
# def work():
#     return render_template('works.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')
#
# @app.route('/index.html')
# def index():
#     return render_template('index.html')