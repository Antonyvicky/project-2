from flask import Flask, render_template, request, redirect, url_for
from queen import solveNQueens as queen_solver
from user import solveNQueens as user_solver

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            N = int(request.form['n_value'])
            if N < 4:
                return render_template('index.html', error="N should be greater than or equal to 4.")
            else:
                queen_solutions = queen_solver(N)
                user_solutions = user_solver(N)
                print(user_solutions)
                return render_template('index.html', queen_solutions=queen_solutions, user_solutions=user_solutions)
        except ValueError:
            return render_template('index.html', error="Invalid input. Please enter a valid integer for N.")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)