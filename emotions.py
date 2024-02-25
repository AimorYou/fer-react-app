import base64
import json
import os

from fer import FER
import numpy as np
import warnings
import cv2

warnings.filterwarnings("ignore")
detector = FER()


def get_bbox_prediction(image_b64, debug=False):
    """
    Getting emotional analysis of face on the given image (in case of few faces, algorithm takes first one)

    :param str image_b64: image in base64 format
    :param bool debug: not yet implemented
    :returns str fer_results: emotions with relative probs
    """
    np_arr = np.fromstring(base64.b64decode(image_b64), np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    fer_results = detector.detect_emotions(image)[0]
    fer_results["box"] = fer_results["box"].tolist()
    fer_results["emotion"] = max(fer_results["emotions"], key=fer_results["emotions"].get)

    return fer_results


if __name__ == "__main__":
    img = cv2.imread(os.path.join(os.path.dirname(__file__), "resources/happy.jpg"))

    tf_version_results = get_bbox_prediction(img)
    print(json.dumps(tf_version_results, default=float, indent=4))
