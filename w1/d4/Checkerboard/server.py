from flask import Flask, render_template
app = Flask(__name__)
    
@app.route('/') 
def square_Checkerboard():
    return render_template('8by8.html')

@app.route('/4')
def eightByFour():
    return render_template('8by4.html')

@app.route('/<int:x>/<int:y>')
def customSquare(x,y):
    return render_template('custom.html', x=x,y=y)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def customColors(x,y,color1,color2):
    return render_template('colors.html', x=x, y=y, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)