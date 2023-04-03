from flask import Flask,escape,render_template,request
from pydantic import BaseModel,validator,ValidationError

app = Flask(__name__)


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
    return render_template('index.html')

@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html',company_name='VG enterprises')

@app.route('/stocks/',methods=['GET'])
def stocks():
    return '<h2>Stock List ...</h2>'

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
        except ValidationError as e:
            print(e)
    return render_template('add_stock.html')