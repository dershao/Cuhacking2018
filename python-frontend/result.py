import cv2, numpy, base64, requests
from PIL import Image
from io import BytesIO

def getResult():
    cap = cv2.VideoCapture(0)
    ret = 0
    frame = 0
    for i in range(0, 5):
        ret, frame = cap.read()

    # # Debug
    # cv2.imshow('Image', frame)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # # End Debug
    cap.release()

    buffered = BytesIO()
    image = Image.fromarray(frame, 'RGB')
    image.save(buffered, format='JPEG')
    image_str = base64.b64encode(buffered.getvalue())

    address = 'http://127.0.0.1:8000/feelsgood/emotion'

    r = requests.get(address, params={'image':image_str})

    return r.content.decode('utf-8').split(',')
