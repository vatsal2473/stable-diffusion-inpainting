from models.CodeFormer import inference_codeformer

def restore(input_path, output_path):
    inference_codeformer.main(input_path, output_path)