from flask import (
    Flask,
    render_template,
    redirect,
    request
)

app = Flask(__name__)

saved_data = {}



@app.route('/')
def route_index():
    note_text = None
    if 'note' in saved_data:
        note_text = saved_data['note']

    return render_template('index.html', note=note_text)

# now we accept not only requests with the default GET method but with POST additionally
@app.route('/edit-note', methods=['GET', 'POST'])
def route_edit():
    note_text = "konik"



    if 'note' in saved_data:  # If we have something already stored, then use that
        note_text = saved_data['note']


    if request.method == 'POST':  # the function is called with POST when we save a note
        saved_data['note'] = request.form['note']
        return redirect('/')  # redirect to the home page which will show the saved note

    return render_template('edit.html', note=note_text)








if __name__ == "__main__":
    app.run(
        debug=True,
        port=7010
    )



