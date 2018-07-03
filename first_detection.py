from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
# extract=true, return two object
detections, objects_path = detector.detectObjectsFromImage(
    input_image=os.path.join(execution_path , "image4.jpeg"),
    output_image_path=os.path.join(execution_path , "imagenew4.jpg"),
    extract_detected_objects=True
)

for eachObject, eachObjectPath in zip(detections, objects_path):
    print(eachObject["name"] + " : " + eachObject["percentage_probability"] )
    print("Object's image saved in " + eachObjectPath)
    print("--------------------------------")