from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hook():
    print(request.data)
    return "hello World"
   

if __name__ == '__main__':
    app.run(debug=True)
