import pytest
import re
import json
import math
from results import attributes_results as results
from base import SDKBase


class Attribute():
    _rotation = (-90, 90, 5.0)
    _roll = (-180, 180, 5.0)
    _gender = (0.0, 1.0, 0.2)
    _race = (0.0, 1.0, 0.2)
    _emotions = (0.0, 1.0, 0.2)
    _glasses = (0.0, 1.0, 0.2)
    _expose = (0.0, 1.0, 0.2)
    _age = (0, 91, 2.0)
    _beard = (0.0, 1.0, 0.2)
    _quality = (-math.inf, math.inf, 0.2)
    _sharpness = (0.0, math.inf, 250.0)
    _liveness = (0.0, 1.0, 0.3)
    _medmask = (0.0, 1.0, 0.2)

    _face_attr = {
        'Age': _age,
        'Gender': {
            'male': _gender,
            'female': _gender
        },
        'Race': {
            'white': _race,
            'indian': _race,
            'asian': _race,
            'black': _race
        },
        'Emotions': {
            'neutral': _emotions,
            'sad': _emotions,
            'happy': _emotions,
            'angry': _emotions,
            'surprise': _emotions,
            'fear': _emotions,
            'disgust': _emotions
        },
        'Liveness': _liveness,
        'Quality': _quality,
        'Beard': _beard,
        'Glasses': {
            'none': _glasses,
            'optical': _glasses,
            'sun': _glasses
        },
        'Headpose': {
            'yaw': _rotation,
            'pitch': _rotation,
            'roll': _roll
        },
        'Overexposure': _expose,
        'Underexposure': _expose,
        'Sharpness': _sharpness,
        'Medmask': {
            'correct': _medmask,
            'none': _medmask,
            'incorrect': _medmask}
    }

    def __init__(self, attr, param=None):
        if param is None:
            self.min, self.max, self.delta = self._face_attr[attr]
        else:
            self.min, self.max, self.delta = self._face_attr[attr][param]


class FaceAttributes():
    attributes = None
    face_id = 0
    face = None

    def __init__(self, attributes_strings):
        """ Метод парсит атрибуты каждого 'Face N' и сохраняет в формате json:
        {'Face 1': {'Age': 20, 'Beard': 0.02, ... }}
        """
        attributes = {}
        for attr_sting in attributes_strings:
            attr_name, attr_value = attr_sting.split(':', maxsplit=1)
            attr_features_list = attr_value.split(', ')

            # Если строка содержит ID лица
            if not attr_value:
                self.face_id = attr_name
                continue

            # Если значение атрибута - число
            if len(attr_features_list) == 1:
                attributes[attr_name] = float(attr_value)
                continue

            # Если значенияе атрибута - словарь
            attributes[attr_name] = {}
            for feature_str in attr_features_list:
                feature_name, feature_value = feature_str.split(': ')
                if feature_name.startswith(' '):
                    feature_name = feature_name[1:]

                attributes[attr_name][feature_name] = float(feature_value)
        self.attributes = attributes
        self.face = {self.face_id: attributes}


class AttributesResponse():
    header = None
    faces = {}
    face_info_length = 14
    header_length = 4

    def __init__(self, tool_response):
        """ Пример tool_response:

        ['Starting detection',
        'Faces found: 1',
        'Loading attributes models',
        'Extracting attributes:',
        'Age: 16',
        'Gender: male: 0.00, female: 1.00',
        'Race: white: 0.58, indian: 0.20, asian: 0.18, black: 0.04',
        'Emotions: neutral: 1.00, sad: 0.00, happy: 0.00, angry: 0.00, surprise: 0.00, fear: 0.00, disgust: 0.00',
        'Liveness: 0.96',
        'Quality: -0.03385',
        'Beard: 0.02',
        'Glasses: none: 1.00, optical: 0.00, sun: 0.00',
        'Headpose: yaw: 24, pitch: -21, roll: -6',
        'Overexposure: 0.76',
        'Underexposure: 0.07',
        'Sharpness: 2465.88',
        'Medmask: correct: 0.90, none: 0.10, incorrect: 0.00']
        """
        self.header = tool_response[:self.header_length]
        faces_data = tool_response[self.header_length:]
        faces_count = int(len(faces_data) / self.face_info_length)
        for face_number in range(0, faces_count):
            start_face = face_number * self.face_info_length
            end_face = (face_number + 1) * self.face_info_length
            face_strings = faces_data[start_face:end_face]
            self.faces.update(FaceAttributes(face_strings).face)

    @staticmethod
    def compare(sdk_response, expect_result):
        """ Сравнивает ответ экзампла с ожидаемым результатом
        """
        def _compare_attr(face_id, attr_name, attr_value, expected_value):
            if isinstance(attr_value, float):
                values = {attr_name: attr_value}
                expected_value = {attr_name: expected_value}
            else:
                values = attr_value

            for attr_k, attr_v in values.items():
                param = None if attr_k == attr_name else attr_k
                attr_object = Attribute(attr_name, param)
                min, max, delta = attr_object.min, attr_object.max, attr_object.delta
                if min <= attr_v <= max and abs(attr_v - expected_value[attr_k]) <= delta:
                    continue
                else:
                    print('{face}:[{param}]'.format(face=face_id, param=param), attr_v, expected_value[attr_k])
                    return False
            return True

        for face_id, atrrs in sdk_response.items():
            for attr_name, attr_value in atrrs.items():
                expected_value = expect_result[face_id][attr_name]
                isequal = _compare_attr(face_id, attr_name, attr_value, expected_value)
                if not isequal:
                    return False
        return True


class TestFFSDKAttributes(FFSDKBase):

    @pytest.mark.tlcode_ff_391
    @pytest.mark.parametrize(
        'photo_name, result, error', results.no_faces,
        ids=[i[0] for i in results.no_faces]
    )
    def test_attr_no_faces(self, photo_name, result, error):
        exit_code, stdout, stderr = self.attribute(photos=[photo_name])
        assert exit_code == 1, (stdout, stderr)
        assert stdout == result
        assert stderr == error

    @pytest.mark.tlcode_ff_392
    @pytest.mark.parametrize(
        'photo_name, result, attributes, error', results.one_face,
        ids=[i[0] for i in results.one_face]
    )
    def test_attr_one_face(self, photo_name, result, attributes, error):
        exit_code, stdout, stderr = self.attribute(photos=[photo_name])
        assert exit_code == 0, (stdout, stderr)
        face_attributes = AttributesResponse(stdout)
        init_result, attributes_result = face_attributes.header, face_attributes.faces
        assert init_result == result
        assert AttributesResponse.compare(attributes_result, attributes)
        assert stderr == error

    @pytest.mark.tlcode_ff_393
    @pytest.mark.parametrize(
        'photo_name, result, attributes, error', results.many_faces,
        ids=[i[0] for i in results.many_faces]
    )
    def test_attr_many_faces(self, photo_name, result, attributes, error):
        exit_code, stdout, stderr = self.attribute(photos=[photo_name])
        assert exit_code == 0, (stdout, stderr)
        face_attributes = AttributesResponse(stdout)
        init_result, attributes_result = face_attributes.header, face_attributes.faces
        assert init_result == result
        assert AttributesResponse.compare(attributes_result, attributes)
        assert stderr == error
