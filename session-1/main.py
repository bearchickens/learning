from flask import Flask
app = Flask(__name__)


@app.route('/')
def ugly():
    return "Ugly Turtle!"


@app.route('/gayturtle')
def gay_turtle():
    return "Gay Turtle Very Much!"


@app.route('/prettyturtle')
def pretty_turtle():
    name = "Linoyz"
    last_name = "Hevron"
    final_response = "{0} {1}".format(name, last_name)
    return final_response


if __name__ == '__main__':
    app.run()
