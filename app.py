from flask import Flask, render_template, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST': 
        grades = request.form.getlist("grades")
        weights = request.form.getlist("weights")
        print(grades)
        print(weights)
        weightsum = 0
        average = 0
        for i in range(0, len(grades)):
            weightsum += int(weights[i])
            average += int(grades[i]) * float((int(weights[i])/100))
        finalgrade = f'{(average / weightsum) * 100:.2f}'

        return render_template('index.html', grade=finalgrade)
    return render_template('home.html')