from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from pypdf import PdfReader
import openai
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # Max file size is 2MB
openai.api_key = os.getenv("OPENAI_API_KEY")  # Set your API key here

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

def training_data(data):
    return f"""Review this Resume text and highlight
              how this resume can be reworded to maximize
              recruiting chances, here is the resume text: {data}, 
              Put your response in bullet points with titles that match
              the experience that the resume refers to. Also ensure that 
              the inputted data is in fact a resume, if the data looks like 
              it is something else, provide a response that requests the user to 
              input a resume or something that is more formatted as one. 
              Pretend like you are a resume reviewer providing information to the user
              generate sentences so it feels more natural instead of just outputting the 
              information. 
              
           """

def query_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

@app.route('/', methods=['GET', "POST"])
@app.route('/home', methods=['GET', "POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        
        save_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'])
        os.makedirs(save_path, exist_ok=True)
        
        full_file_path = os.path.join(save_path, filename)
        file.save(full_file_path)

        try:
            reader = PdfReader(full_file_path)
            text = ''
            for page in reader.pages:
                text += page.extract_text() or ''
            
            prompt = training_data(text)
            gpt_response = query_gpt(prompt)
            if gpt_response:
                return render_template('response.html', gpt_response=gpt_response)
            else:
                flash("GPT did not generate a response.", "error")
                return render_template('index.html', form=form)

        except Exception as e:
            flash(f"Failed to read the PDF file: {e}", "error")
            return render_template('index.html', form=form)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)