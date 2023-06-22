from flask import Flask, render_template

app = Flask(
    __name__,
    static_folder='static'
)

@app.route('/point-hub')
def point_hub():
    return render_template('point-hub.html')

if __name__ == '__main__':
    app.run()
