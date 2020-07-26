import requests
import os
import json
import datetime, time
import base64
import threading
from queue import Queue


``` 
Scripted tool for multi-thread generating events
from photo-direcroty "PHOTO_PATH"
```

def get_list_directory():
    files = os.listdir(PHOTO_PATH)
    file_list = []
    for name in sorted(files, reverse=False):
        file_list.append(name)
    return file_list


class Downloader(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            photo = self.queue.get()
            self.posting(photo)
            self.queue.task_done()

    def bbox_massive(self, args):
        b = args['bottom']
        t = args['top']
        r = args['right']
        l = args['left']
        return [l, t, r, b]

    def photo_detect(self, photo):
        start_time = time.time()
        file_detect = {'photo': open('{}/{}'.format(PHOTO_PATH, photo), 'rb')}
        detect_result = requests.post(DETECTOR, headers=HEADERS, files=file_detect)
        serealize = detect_result.json()
        if not serealize['faces']:
            return 0
        else:
            bbox_dict = serealize['faces'][0]['bbox']
            score = serealize['faces'][0]['detection_score']
            detect_dict = {"score": score,
                           "bbox": self.bbox_massive(bbox_dict)}
            print('detect-time: {}'.format(time.time()-start_time))
            return detect_dict

    def get_normalized(self, photo):
        start_time = time.time()
        data = {
            'request': '{"requests": [{"image": "multipart:sample", '
                       '"detector": "cheetah", "auto_rotate": false, '
                       '"need_face":false, "need_normalized": true}]}'
        }
        file = {'sample': (photo, open('{}/{}'.format(PHOTO_PATH, photo), 'rb'), 'image/jpeg')}

        response = requests.post(EXT_API, data={**data}, files=file)
        full_json = json.loads(response.text)
        normalized = full_json['responses'][0]['faces'][0]['normalized']
        crop2x = base64.b64decode(normalized)
        print('extract-time: {}'.format(time.time() - start_time))
        return crop2x

    def posting(self, photo):
        photo_detect_result = self.photo_detect(photo)
        if photo_detect_result == 0:
            print('Faces not found. File removed')
            os.remove("{}/{}".format(PHOTO_PATH, photo))
        else:
            start_time = time.time()
            current_time = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%dT%H:%M:%S')
            data = {"cam_id": (None, "{}".format(CAMERA), None),
                    "bbox": (None, json.dumps([photo_detect_result['bbox']]), None),
                    "detectorParams": (None, json.dumps({"score": photo_detect_result['score']}), None),
                    "timestamp": (None, current_time, None),
                    "bs_type": (None, "overall", None),
                    }
            file_event = {'photo': (photo, open('{}/{}'.format(PHOTO_PATH, photo), 'rb'), 'image/jpeg'),
                          'normalized': self.get_normalized(photo)}
            requests.post(TARGET_MODULE, headers=VIDEO_HEADERS, data={**data}, files=file_event)
            print("{}, time-posting: {}".format(photo, start_time-time.time()))


def main(photos):
    queue = Queue()

    for i in range(25):
        t = Downloader(queue)
        t.setDaemon(True)
        t.start()

    for photo in photos:
        queue.put(photo)

    queue.join()


if __name__ == '__main__':
    TARGET_URL = 'http://127.0.0.1'
    EXT_API = '{}:1488'.format(TARGET_URL)
    TARGET_MODULE = '{}/video-detector/frame/'.format(TARGET_URL)
    DETECTOR = '{}/detect/'.format(TARGET_URL)
    CAMERA = 2
    PHOTO_PATH = '/alan/nginx-upload/photoset'

    HEADERS = {
        'Authorization': 'Token secret_token'
    }

    VIDEO_HEADERS = {
        'Authorization': 'Token secret_token_2'
    }
    photos = get_list_directory()
    main(photos)
