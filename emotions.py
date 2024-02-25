import json
import os

from fer import FER
import warnings
import cv2

warnings.filterwarnings("ignore")
detector = FER()


def get_bbox_prediction(image, debug=False):
    fer_results = detector.detect_emotions(image)[0]
    fer_results["box"] = fer_results["box"].tolist()
    fer_results["emotion"] = max(fer_results["emotions"], key=fer_results["emotions"].get)

    return fer_results


if __name__ == "__main__":
    img = cv2.imread(os.path.join(os.path.dirname(__file__), "resources/happy.jpg"))

    tf_version_results = get_bbox_prediction(img)
    print(json.dumps(tf_version_results, default=float, indent=4))
