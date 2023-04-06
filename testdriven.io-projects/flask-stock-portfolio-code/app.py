from flask import Flask,escape,render_template,request,session,redirect,url_for,flash
from pydantic import BaseModel,validator,ValidationError
import logging
from flask.logging import default_handler
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# Remove the default logger 
app.logger.removeHandler(default_handler)

app.secret_key = b'>o\xf5\x10r\xe3\x13\xfa\xd6\xc2UE\xc8\x18\x83\x82\x10\xbfVP\x90\xb5\x16\xf3\x91\x86\xb3\xf2Z\x80Oh'

# Logging Configuration
file_handler = RotatingFileHandler('flask_stock_portfolio.log',maxBytes=16384,backupCount=20)
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s:%(lineno)d]')
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

# Log that the flask application is starting
app.logger.info('Starting Flask Stock Portfolio Application')

#---------
# Helper Classes
#---------
class StockModel(BaseModel):
    stock_symbol: str
    number_of_shares: int
    purchase_price: float

    @validator('stock_symbol')
    def symbol_symbol_check(cls,value):
        if not value.isalpha() or len(value)>5:
            raise ValueError('Stock symbol must be 1-5 characters')
        return value.upper()

#---------
# Routes
#---------

@app.route('/')
def index():
    app.logger.info('Called the index() function.')
    return render_template('index.html')

@app.route('/about',methods=['GET'])
def about():
    flash(f"Thanks for learning about this site!",'info')
    return render_template('about.html',company_name='VG enterprises')

@app.route('/stocks/',methods=['GET'])
def list_stocks():
    return render_template('stocks.html')

@app.route('/hello/<message>')
def hello_message(message):
    return f'<h1>Welcome {escape(message)}!</h1>'

@app.route('/blog_posts/<int:post_id>')
def display_blog_post(post_id):
    return f'<h1>Blog Post #{post_id}..</h1>' 

@app.route('/add_stock',methods=['GET','POST'])
def add_stock():
    if request.method == 'POST':
        #Print the form data to the terminal
        for key,value in request.form.items():
            print(f'{key} = {value}')

        try:
            stock_data = StockModel(
                stock_symbol=request.form['stock_symbol'],
                number_of_shares=request.form['number_of_shares'],
                purchase_price=request.form['purchase_price']
            )
            print(stock_data)

            # save the form data to the session object
            session['stock_symbol'] = stock_data.stock_symbol
            session['number_of_shares'] = stock_data.number_of_shares
            session['purchase_price'] = stock_data.purchase_price
            flash(f"Added new stock ( { stock_data.stock_symbol } )!",'success')
            app.logger.info(f"Added new stock ( {request.form['stock_symbol']} )!")

            return redirect(url_for('list_stocks'))
        except ValidationError as e:
            print(e)
    return render_template('add_stock.html') 