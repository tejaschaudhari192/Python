       

app = Flask(__name__);

@app.route('/eval', methods=['GET'])
def evaluate():
    exp = request.args.get('exp');
    
    if exp:
        try:
            result = eval(exp);
            return jsonify({'result': result}),200;
        except Exception as e:
            return jsonify({'error': str(e)}),400;
    else:
        return jsonify({'error': 'Expression parameter is required'}), 400

if __name__ == '__main__':
    app.run(debug=True);