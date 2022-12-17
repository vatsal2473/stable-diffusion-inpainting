from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
from flask_cors import CORS, cross_origin
from src import load_models, inpaint, helper_functions
import requests

# global pipe
# pipe = load_models.load_stable_diffusion_inpainting_model()

app = Flask(__name__)
CORS(app)

@app.route('/inpaint', methods=['GET', 'POST'])
def inpaint_image():
    if request.method == "POST":
        image = request.files['image']
        mask_image = request.files['mask_image']
        image.save('input/image.png')
        mask_image.save('input/mask_image.png')
        prompt = request.form.get('prompt')
        print("====Data Received====")

    try:
        images = inpaint.stable_diffusion_inpaint(prompt, pipe, image_path='input/image.png', mask_path='input/mask_image.png')
        grid = helper_functions.image_grid(images, 1, 3)
        grid.save('output/grid.png')

        files = {
            'file': open('output/grid.png', 'rb'),
        }
        response = requests.post('https://file.io', files=files)

        res = {}
        res['url'] = response.json()['link']
        return res

    except Exception as e:
        print(e)
        return e

if __name__ == "__main__":
    app.run()