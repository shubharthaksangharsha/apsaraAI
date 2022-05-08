from click import command
from flask import Flask, render_template, template_rendered, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from main2 import run
import speech_recognition as sr
from os import path, system
from pydub import AudioSegment

#from gtts import gTTS
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///apsara.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
def write(command):
    with open('command.txt', 'w') as f:
        f.write(command)
        
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    command = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.command}"
    
def read_command():
    with open('command.txt', 'r') as f:
        apsara_command = f.read()
    return apsara_command


@app.route("/talk", methods=['GET', 'POST'])
def talk():
    transcript = ''
    if request.method == "POST":
        print("FORM DATA RECIEVED")
        if "file" not in request.files:
            print('Failed')
            return redirect(request.url)
        
        file = request.files["file"]
        print(file.filename)
        if file.filename == "":
            return redirect(request.url)
        if file:  
        # assign files
            print(file.filename)
            input_file = file
            output_file = "result.wav"
            sound = AudioSegment.from_mp3(input_file)
            sound.export(output_file, format="wav")            
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(output_file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data)
            print(f'User said: {transcript}')
            write(transcript)
            run(transcript)
    return render_template('talk.html', take_command=transcript,apsara_command=read_command())
@app.route("/text", methods=['GET', 'POST'])
def text():
    command = ''
    if request.method=='POST':
        command = request.form['take_command']
        write(command)
        run(command)
        apsara_command= Todo(command=command)
        db.session.add(apsara_command)
        db.session.commit()
    all_commands = Todo.query.all()
    print(command)
    return render_template('text.html',all_commands=all_commands, take_command=command,apsara_command=read_command())

@app.route('/about')
def about():
    return render_template('about.html')
@app.route("/", methods=['GET', 'POST'])
def main():
    command = ''
    if request.method=='POST':
        command = request.form['take_command']
        write(command)
        run(command)
        apsara_command= Todo(command=command)
        db.session.add(apsara_command)
        db.session.commit()
    all_commands = Todo.query.all()
    print(command)   
    return render_template('index.html')
    return render_template('text.html',all_commands=all_commands, take_command=command,apsara_command=read_command())


@app.route("/delete/<int:sno>")
def delete(sno):
    delete_command = Todo.query.filter_by(sno=sno).first()
    db.session.delete(delete_command)
    db.session.commit()
    with open('command.txt', 'w') as f:
        pass
    return redirect("/text")

@app.route("/delete/<command>")
def delete_all(command):
    system("rm apsara.db")
    db.create_all()
    write("")
    return redirect("/text")

    
@app.route("/send/<command>")
def send_again(command):
    write(command)
    run(command)
#    apsara_command= Todo(command=command)
#    db.session.add(apsara_command)
#    db.session.commit()
    print(command)
    all_commands = Todo.query.all()
    return render_template('text.html',all_commands=all_commands, take_command=command,apsara_command=read_command())

if __name__ == '__main__':
    app.run(debug=True, port=5001)
