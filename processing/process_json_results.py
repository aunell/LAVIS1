import json

path= '/pasteur/u/aunell/LAVIS/lavis/output/BLIP2/Image_eval/20240412112/result/val_epochbest_rank0.json'
with open(path, 'r') as file:
    data = json.load(file)

def check_accuracy(data):
    """
    data is a list of dictionaries with keys "image_id" and "caption"
    """
    def preprocess(generated: str):
        generated = generated.lower()
        return generated.split('\n')[0]

    correct = 0
    total = 0
    for item in data:
        generated = item["caption"]
        caption =preprocess(generated)
        if caption in item["image_id"] or item["image_id"] in caption:
            correct += 1
            print(generated)
            print("GAP")
            print(caption)
        total+=1

    return correct/total
