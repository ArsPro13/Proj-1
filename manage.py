from flask import Flask
from flask import render_template
from flask import request

def toweb(f):
    app = Flask(__name__)

    @app.route("/", methods=['GET', 'POST'])
    def myfunc():
        about = f.__doc__
        
        a = f.__annotations__
        if 'return' in a:
            a.pop('return') 
        if request.form:
            res = f(**request.form)
        else:
            res = None

        return render_template('temp.html',  about = "Проверка на палиндром", res=res, a = a)

    return app

# s = toweb(hello_world)
@toweb
def hello_world(word: str) -> str:
  answer = ""
  if (word == word[::-1]):
    answer = "Слово является палиндромом"
  else:
    answer = "Слово не является палиндромом, но из него можно составить " + word+word[::-1] + ", являющееся им"
  return answer

hello_world.run(host='0.0.0.0', port="5001")
