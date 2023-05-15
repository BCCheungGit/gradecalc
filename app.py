from flask import Flask, render_template, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST': 
        grades = request.form.getlist("grades")
        weights = request.form.getlist("weights")
        assignments = request.form.getlist("assignments")
        #print(grades)
        #print(weights)
        weightsum = 0
        average = 0
        for i in range(0, len(grades)):
            if grades[i] == '':
                break
            weightsum += int(weights[i])
            average += int(grades[i]) * float((int(weights[i])/100))
        finalgrade = f'{(average / weightsum) * 100:.2f}'
        

        lettergrades = ['A', 'A-', 'B', 'B-', 'C', 'C-', 'D', 'F']
        letter = 'F'
        finalfloat = float(finalgrade)


        if finalfloat >=95:
            letter = lettergrades[0]
        elif finalfloat >= 90:
            letter = lettergrades[1]
        elif finalfloat >= 85:
            letter = lettergrades[2]
        elif finalfloat >= 80:
            letter = lettergrades[3]
        elif finalfloat >= 75:
            letter = lettergrades[4]
        elif finalfloat >= 70:
            letter = lettergrades[5]
        elif finalfloat >= 65: 
            letter = lettergrades[6]
        else:
            letter = lettergrades[7]



        return render_template('index.html', grade=finalgrade, lettergrade=letter, grades=grades, weights=weights, assignments=assignments)
    return render_template('home.html')