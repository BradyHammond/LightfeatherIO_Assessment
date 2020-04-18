# ================================================== #
#                        APP                         #
# ================================================== #
# Author: Brady Hammond                              #
# Created: 04/16/2020                                #
# Last Edited: N/A                                   #
# ================================================== #
#                      IMPORTS                       #
# ================================================== #

from encode import Encoder
from flask import Flask, render_template, request, abort, make_response, jsonify

# ================================================== #
#                    APP CONFIG                      #
# ================================================== #

app = Flask(__name__,
            static_folder='./client/dist/static',
            template_folder='./client/dist')

# ================================================== #
#                      ROUTES                        #
# ================================================== #


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/encode', methods=['POST'])
def encode():
    if not request.json:
        abort(make_response(jsonify({'status': '500', 'message': 'Invalid JSON request'}), 500))
    if 'Shift' not in request.json:
        abort(make_response(jsonify({'status': '500', 'message': 'Request missing key: Shift'}), 500))
    if 'Message' not in request.json:
        abort(make_response(jsonify({'status': '500', 'message': 'Request missing key: Message'}), 500))
    if type(request.json['Shift']) != int:
        abort(make_response(jsonify({'status': '500', 'message': 'Invalid Shift value'}), 500))
    if type(request.json['Message']) != str:
        abort(make_response(jsonify({'status': '500', 'message': 'Invalid Message value'}), 500))
    encoder = Encoder(request.json['Shift'], request.json['Message'])
    encoder.encode()
    encoder.save()
    return jsonify({'EncodedMessage': encoder.encoded_message}), 200

# ================================================== #
#                       MAIN                         #
# ================================================== #


if __name__ == "__main__":
    app.run(debug=True, port=23456)

# ================================================== #
#                        EOF                         #
# ================================================== #
