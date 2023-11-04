from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize an empty list to store tasks
tasks = []


# Function to add a task to the list
def add_task(task):
    tasks.append(task)


# Function to remove a task from the list
def remove_task(task):
    if task in tasks:
        tasks.remove(task)


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        add_task(task)
    return redirect(url_for('index'))


@app.route('/remove', methods=['POST'])
def remove():
    task = request.form.get('task')
    if task:
        remove_task(task)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
