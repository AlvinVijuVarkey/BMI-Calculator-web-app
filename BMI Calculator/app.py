from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    bmi = None
    category = None
    color = None

    if request.method == 'POST':
        try:
            height = float(request.form['height'])
            weight = float(request.form['weight'])

            # Convert height from cm to meters
            height_m = height / 100
            bmi = round(weight / (height_m ** 2), 2)

            # Determine category
            if bmi < 18.5:
                category = "Underweight"
                color = "blue"
            elif 18.5 <= bmi < 24.9:
                category = "Normal"
                color = "green"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
                color = "orange"
            else:
                category = "Obese"
                color = "red"
        except:
            bmi = "Invalid input"
            category = "Please enter valid numbers!"
            color = "gray"

    return render_template('index.html', bmi=bmi, category=category, color=color)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
