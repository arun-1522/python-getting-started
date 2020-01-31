from flask import Flask,render_template,request,url_for
app = Flask(__name__)

@app.route('/index')
def success():
   return render_template("ma.html")

@app.route('/Medicalcollege')
def main():
   return render_template('college.html')

@app.route('/Engineeringcollege')
def main1():
   return render_template('college1.html')
   
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      mark=request.form['Mark of 12: ']
      q=int(mark)//12
      if 90<=q<=100:
         n='Your Eligible To Join The Medical College as well as Engineering college'
         form = request.form
         return render_template('pysir.html',form=form,rest=n,mark=q)
      elif 80<=q<=89:
         n='Your Eligible To Join The Engineering College'
         form = request.form
         return render_template('pysir.html',form=form,rest=n,mark=q)
      else:
         n='Your Not Eligible To Join The Medical College And Engineering College'
         form = request.form
         return render_template('pysir.html',form=form,rest=n,mark=q)

if __name__ == '__main__':
   app.run(debug = True)
