from flask import Flask, render_template, request
from PIL import Image
import io

app = Flask(__name__)

def encode_message(image, message):
    # Encode message into image
    # Same encode_message function as before

def decode_message(encoded_image):
    # Decode message from encoded image
    # Same decode_message function as before

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    image_file = request.files['image']
    message = request.form['message']
    if image_file and message:
        image = Image.open(io.BytesIO(image_file.read()))
        encoded_image_path = encode_message(image, message)
        return encoded_image_path
    else:
        return "Error: Image or message not provided."

@app.route('/decode', methods=['POST'])
def decode():
    encoded_image_file = request.files['encoded_image']
    if encoded_image_file:
        encoded_image = Image.open(io.BytesIO(encoded_image_file.read()))
        decoded_message = decode_message(encoded_image)
        return render_template('index.html', decoded_message=decoded_message)
    else:
        return "Error: Encoded image not provided."

if __name__ == '__main__':
    app.run(debug=True)
