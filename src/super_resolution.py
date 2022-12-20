import os, glob
import glob
import shutil
import cv2
from models.Real_ESRGAN.SwinIR import main_test_swinir
from PIL import Image

def imread(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img



def increase_resolution(input_folder, output_folder):

    test_patch_wise = False

    dir = 'models/Real_ESRGAN/BSRGAN/testsets/RealSRSet'
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist:
        os.remove(f)

    upload_folder = input_folder
    result_folder = 'models/Real_ESRGAN/results'

    if os.path.isdir(upload_folder):
        shutil.rmtree(upload_folder)
    if os.path.isdir(result_folder):
        shutil.rmtree(result_folder)
    os.mkdir(upload_folder)
    os.mkdir(result_folder)


    # upload files in folder
    
    images = os.listdir('input/swinir')
    for i in range(len(images)):
        src = os.path.join('input/swinir', images[i])
        dst = os.path.join('models/Real_ESRGAN/BSRGAN/testsets/RealSRSet', images[i])
        shutil.copyfile(src, dst)
    
    dir = 'models/Real_ESRGAN/results'
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist:
        os.remove(f)

    test_patch_wise = True
    if test_patch_wise:
        main_test_swinir.main()
        #!python SwinIR/main_test_swinir.py --task real_sr --model_path experiments/pretrained_models/003_realSR_BSRGAN_DFOWMFC_s64w8_SwinIR-L_x4_GAN.pth --folder_lq BSRGAN/testsets/RealSRSet --scale 4 --large_model --tile 640
        
    else:
        print("swinir will not work")
        #!python SwinIR/main_test_swinir.py --task real_sr --model_path experiments/pretrained_models/003_realSR_BSRGAN_DFOWMFC_s64w8_SwinIR-L_x4_GAN.pth --folder_lq BSRGAN/testsets/RealSRSet --scale 4 --large_model

    shutil.move('models/Real_ESRGAN/results/swinir_real_sr_x4', output_folder)
    #for path in sorted(glob.glob(os.path.join('models/Real_ESRGAN/results/SwinIR_large', '*.png'))):
    #    os.rename(path, path.replace('SwinIR.png', 'SwinIR_large.png'))

def resizing_high_quality_images():
    #resizing images without compromising quality
    names = os.listdir('models/Real_ESRGAN/results/SwinIR')
    for i in range(len(names)):
        foo = Image.open('models/Real_ESRGAN/results/SwinIR/'+names[i])
        print(foo.size)
        foo = foo.resize((768, 1024), Image.ANTIALIAS)
        save_path = 'output/test/test/unpaired/generator/output_sr/'+names[i]
        foo.save(save_path, optimize=True, quality=85)
