from flask import Flask, request, jsonify
import products_dao
from sql_connection import get_sql_connection

  


app = Flask(__name__)

connection = get_sql_connection()

@app.route('/getProducts', methods=['GET'])
def getProducts():
    products = products_dao.get_all_products(connection)
    #jsonify is converting dictionpry to json
    response = jsonify(products)
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteProduct', methods = ['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection,request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
    
    
      


if __name__ == "__main__":
    print("Starting Flask Server...")
    app.run(port=5000)
    