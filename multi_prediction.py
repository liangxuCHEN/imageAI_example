from imageai.Prediction import ImagePrediction
import os
from translate import baiduTranslate


execution_path = os.getcwd()
execution_path = ('/').join(execution_path.split('/')[:-1])

multiple_prediction = ImagePrediction()
multiple_prediction.setModelTypeAsResNet()
multiple_prediction.setModelPath(os.path.join(execution_path, "resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
multiple_prediction.loadModel()


all_images_array = []

img_path = os.path.join(execution_path, "images")

all_files = os.listdir(img_path)
for each_file in all_files:
    if(each_file.endswith(".jpg") or each_file.endswith(".png")):
        all_images_array.append(os.path.join(img_path, each_file))


results_array = multiple_prediction.predictMultipleImages(all_images_array, result_count_per_image=5)


for each_result in results_array:
    predictions, percentage_probabilities = each_result["predictions"], each_result["percentage_probabilities"]
    for index in range(len(predictions)):
        obj = None
        r = translate.run(predictions[index])
        if r['is_error']:
            obj = predictions[index]
        else:
            obj = '{}({})'.format(r['data'][0]['dst'], predictions[index])
        print(obj + " : " + percentage_probabilities[index])
        print("-----------------------")

    print('##############################')