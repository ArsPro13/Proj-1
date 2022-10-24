from email import message
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['post', 'get'])
def hello_world():
  answer = ""
  if request.method == 'POST':
    answer = ""
    word = request.form.get('word')
    if (word == word[::-1]):
      answer = "Слово является палиндромом"
    else:
      answer = "Слово не является палиндромом, но из него можно составить " + word+word[::-1] + ", являющееся им"
    print(answer)
  return render_template("temp.html", message = answer)

if __name__ == "__main__":
    app.run()