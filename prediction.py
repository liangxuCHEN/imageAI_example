# 判断单张图片的单个物品

from imageai.Prediction import ImagePrediction
import os
from translate import baiduTranslate

execution_path = os.getcwd()

execution_path = ('/').join(execution_path.split('/')[:-1])

prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path, "resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()

translate = baiduTranslate('en', 'zh')

predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "1.jpg"), result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    obj = None
    r = translate.run(eachPrediction)
    print(r)
    if r['is_error']:
        obj = eachPrediction
    else:
        obj = '{}({})'.format(r['data'][0]['dst'], eachPrediction)

    print(obj + " : " + eachProbability)