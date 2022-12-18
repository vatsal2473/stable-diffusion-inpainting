from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
from flask_cors import CORS, cross_origin
from src import load_models, inpaint, helper_functions, restore_face
import requests

global pipe
pipe = load_models.load_stable_diffusion_inpainting_model()

app = Flask(__name__)
CORS(app)

@app.route('/face-restoration', methods=['GET', 'POST'])
def restore():
    if request.method == "POST":
        print("hi")
        image = request.files['image']
        image.save('input/image.png')
    try:
        restore_face.restore('input/image.png', 'output')
                
            
        files = {
            'file': open('output/final_results/image.png', 'rb'),
        }


        response = requests.post('https://tmpfiles.org/api/v1/upload', files=files)

        res = {}
        res['url'] = response.json()['data']['url']
        return res
    
    except Exception as e:
        print(e)

@app.route('/inpaint-face-restoration', methods = ['GET', 'POST'])
def inpaint_restore():
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
        
        li = []
        for i, img in enumerate(images):
            name = 'output/image{0}.png'.format(i)
            img.save(name)
        # grid = helper_functions.image_grid(images, 1, 3)
        # grid.save('output/grid.png')


            files = {
                'file': open(name, 'rb'),
            }

            response = requests.post('https://tmpfiles.org/api/v1/upload', files=files)
            li.append(response.json()['data']['url'])

        res = {}
        res['url'] = li
        return res

    except Exception as e:
        print(e)
        return e

if __name__ == "__main__":
    app.run()