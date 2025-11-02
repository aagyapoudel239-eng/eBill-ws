from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <form action="/calculate" method="post">
        Enter units used: <input type="number" name="units" required>
        <button type="submit">Calculate</button>
    </form>
    '''

@app.route('/calculate', methods=['POST'])
def calculate_bill():
    units = float(request.form['units'])
    if units <= 20:
        bill = 80
    elif units <= 30:
        bill = (20 * 4) + ((units - 20) * 7)
    elif units <= 50:
        bill = (20 * 4) + (10 * 7) + ((units - 30) * 8.5)
    elif units <= 150:
        bill = (20 * 4) + (10 * 7) + (20 * 8.5) + ((units - 50) * 10)
    elif units <= 250:
        bill = (20 * 4) + (10 * 7) + (20 * 8.5) + (100 * 10) + ((units - 150) * 11)
    else:
        bill = (20 * 4) + (10 * 7) + (20 * 8.5) + (100 * 10) + (100 * 11) + ((units - 250) * 12)

    meter_charge = 30
    total_bill = bill + meter_charge
    return f"<h3>Your total bill is Rs. {total_bill}</h3><a href='/'>Go back</a>"

# Only **one run block** using Render's PORT
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
