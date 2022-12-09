rom flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Asifasif6625'
  
if __name__ == "__main__":
  
    app.run()
