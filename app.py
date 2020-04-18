# ================================================== #
#                        APP                         #
# ================================================== #
# Author: Brady Hammond                              #
# Created: 04/16/2020                                #
# Last Edited: 04/17/2020                            #
# ================================================== #
#                      IMPORTS                       #
# ================================================== #

from encode import Encoder
from flask import Flask, render_template, request, abort, make_response, jsonify

# ================================================== #
#                    APP CONFIG                      #
# ================================================== #

# Initialize flask server
app = Flask(__name__,
            static_folder='./client/dist/static',
            template_folder='./client/dist')

# ================================================== #
#                      ROUTES                        #
# ================================================== #


# Setup home route
@app.route('/')
def index():
    return render_template('index.html')


# Setup API route
@app.route('/api/encode', methods=['POST'])
def encode():
    # Validate request
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

    # Encode and save message
    encoder = Encoder(request.json['Shift'], request.json['Message'])
    encoder.encode()
    encoder.save()

    # Return response
    return jsonify({'EncodedMessage': encoder.encoded_message}), 200

# ================================================== #
#                       MAIN                         #
# ================================================== #

# Entry point for starting server
if __name__ == "__main__":
    app.run(debug=True, port=23456)

# ================================================== #
#                        EOF                         #
# ================================================== #
