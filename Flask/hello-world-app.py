from flask import Flask

app = Flask (__name__)

@app.route('/')
def whoIsAwesome():
    return 'Girls are The Power'

if __name__ == "__main__":
    app.run(debug=True)