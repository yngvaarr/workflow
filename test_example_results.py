"""
- 1. Имя фото
- 2. Массив с ожидаемым текстом из консоли
- 3. Словарь со значениями
"""

no_faces = [
    (
        '1920x1080_no_faces.jpg',
        ['Starting detection',
         'Faces found: 0'],
        None
    )
]

one_face = [
    (
        '1920x1080_ONE_FACE.JPG',
        [
            'Starting detection',
            'Faces found: 1',
            'Loading attributes models',
            'Extracting attributes:'
        ],
        {
            'Face 1': {
                'Gender': {
                    'male': 0.0,
                    'female': 1.0
                },
                'Glasses': {
                    'none': 1.0,
                    'optical': 0.0,
                    'sun': 0.0
                },

                'Underexposure': 0.07,
                'Headpose': {
                    'roll': -6.0,
                    'pitch': -20.0,
                    'yaw': 25.0,
                },
                'Race': {
                    'indian': 0.21,
                    'white': 0.56,
                    'black': 0.04,
                    'asian': 0.19
                },
                'Overexposure': 0.76,
                'Quality': -0.0,
                'Beard': 0.02,
                'Age': 16.0,
                'Liveness': 0.87,
                'Emotions': {
                    'angry': 0.0,
                    'disgust': 0.0,
                    'surprise': 0.0,
                    'sad': 0.0,
                    'happy': 0.0,
                    'fear': 0.0,
                    'neutral': 1.0
                },
                'Sharpness': 2535.73,
                'Medmask': {
                    'correct': 0.90,
                    'none': 0.10,
                    'incorrect': 0.00
                }
            }
        },
        None
    ),
    (
        '850x565_child.jpg',
        [
            'Starting detection',
            'Faces found: 1',
            'Loading attributes models',
            'Extracting attributes:'
        ],
        {
            'Face 1': {
                'Age': 6.0,
                'Beard': 0.02,
                'Emotions': {
                    'angry': 0.0,
                    'disgust': 0.0,
                    'fear': 0.0,
                    'happy': 0.78,
                    'neutral': 0.22,
                    'sad': 0.0,
                    'surprise': 0.0
                },
                'Gender': {
                    'female': 1.0,
                    'male': 0.0
                },
                'Glasses': {
                    'none': 1.0,
                    'optical': 0.0,
                    'sun': 0.0
                },
                'Liveness': 1.0,
                'Overexposure': 0.56,
                'Quality': -0.0,
                'Race': {
                    'asian': 0.02,
                    'black': 0.03,
                    'indian': 0.01,
                    'white': 0.93
                },
                'Headpose': {
                    'yaw': 5.0,
                    'pitch': -21.0,
                    'roll': -14.0
                },
                'Sharpness': 189.4,
                'Underexposure': 0.15,
                'Medmask': {
                    'correct': 0.94,
                    'none': 0.05,
                    'incorrect': 0.00
                }
            }
        },
        None
    ),
    (
        '570x380_ded.jpg',
        [
            'Starting detection',
             'Faces found: 1',
             'Loading attributes models',
             'Extracting attributes:'
        ],
        {
            'Face 1': {
                'Age': 69.0,
                'Beard': 0.04,
                'Emotions': {
                    'angry': 0.0,
                    'disgust': 0.0,
                    'fear': 0.0,
                    'happy': 0.99,
                    'neutral': 0.0,
                    'sad': 0.0,
                    'surprise': 0.0
                    },
                'Gender': {
                    'female': 0.0,
                    'male': 1.0
                },
                'Glasses': {
                    'none': 0.99,
                    'optical': 0.0,
                    'sun': 0.0
                },
                'Liveness': 0.72,
                'Overexposure': 0.63,
                'Quality': -1.46,
                'Race': {
                    'asian': 0.06,
                    'black': 0.05,
                    'indian': 0.13,
                    'white': 0.76
                },
                'Headpose': {
                    'yaw': -1.0,
                    'pitch': 0.0,
                    'roll': 0.0
                },
                'Sharpness': 186.68,
                'Underexposure': 0.01,
                'Medmask': {
                    'correct': 0.00,
                    'none': 1.00,
                    'incorrect': 0.00
                }
            }
        },
        None
    ),
    (
        '723x1343_beard_man.jpg',
        [
            'Starting detection',
             'Faces found: 1',
             'Loading attributes models',
             'Extracting attributes:'
        ],
        {
            'Face 1': {
                'Age': 39.0,
                'Beard': 1.0,
                'Emotions': {
                    'angry': 0.0,
                    'disgust': 0.0,
                    'fear': 0.0,
                    'happy': 0.0,
                    'neutral': 1.0,
                    'sad': 0.0,
                    'surprise': 0.0
                },
                'Gender': {
                    'female': 0.0,
                    'male': 1.0
                },
                'Glasses': {
                    'none': 1.0,
                    'optical': 0.0,
                    'sun': 0.0
                },
                'Liveness': 0.02,
                'Overexposure': 0.48,
                'Quality': -0.0,
                'Race': {
                    'asian': 0.1,
                    'black': 0.1,
                    'indian': 0.3,
                    'white': 0.5
                },
                'Headpose': {
                    'yaw': 35.0,
                    'pitch': -5.0,
                    'roll': -5.0
                },
                'Sharpness': 2678.45,
                'Underexposure': 0.38,
                'Medmask': {
                    'correct': 0.00,
                    'none': 1.00,
                    'incorrect': 0.00
                }
            }
        },
        None
    ),
    (
        '736x736_sun_glasses_women.jpg',
        [
            'Starting detection',
             'Faces found: 1',
             'Loading attributes models',
             'Extracting attributes:'
        ],
        {
            'Face 1': {
                'Age': 25.0,
                'Beard': 0.03,
                'Emotions': {
                    'angry': 0.0,
                    'disgust': 0.0,
                    'fear': 0.0,
                    'happy': 0.01,
                    'neutral': 0.99,
                    'sad': 0.0,
                    'surprise': 0.0
                },
                'Gender': {
                    'female': 1.0,
                    'male': 0.0
                },
                'Glasses': {
                    'none': 0.01,
                    'optical': 0.13,
                    'sun': 0.86
                },
                'Liveness': 1.0,
                'Overexposure': 0.58,
                'Quality': -0.0,
                'Race': {
                    'asian': 0.05,
                    'black': 0.44,
                    'indian': 0.47,
                    'white': 0.04
                },
                'Headpose': {
                    'yaw': 15.0,
                    'pitch': -28.0,
                    'roll': -5.0
                },
                'Sharpness': 2370.45,
                'Underexposure': 0.27,
                'Medmask': {
                    'correct': 0.92,
                    'none': 0.08,
                    'incorrect': 0.00
                }
            }
        },
        None
    )
]

many_faces = [
    (
        '1920x1080_party_5_person.jpg',
        [
            'Starting detection',
            'Faces found: 5',
            'Loading attributes models',
            'Extracting attributes:'
        ],
        {
            'Face 1': {
                'Gender': {
                    'male': 0.0,
                    'female': 1.0
                },
                'Glasses': {
                    'none': 1.0,
                    'optical': 0.0,
                    'sun': 0.0
                },
                'Underexposure': 0.02,
                'Race': {
                    'indian': 0.05,
                    'white': 0.88,
                    'black': 0.04,
                    'asian': 0.04
                },
                'Headpose': {
                    'roll': -7.0,
                    'pitch': -23.0,
                    'yaw': -13.0,
                },
                'Overexposure': 0.62,
                'Quality': -0.0,
                'Beard': 0.03,
                'Age': 20.0,
                'Liveness': 0.11,
                'Emotions': {
                    'neutral': 0.0,
                    'disgust': 0.0,
                    'surprise': 0.02,
                    'angry': 0.0,
                    'sad': 0.0,
                    'happy': 0.98,
                    'fear': 0.0
                },
                'Sharpness': 559.44,
                'Medmask': {
                    'none': 0.68, 'correct': 0.32, 'incorrect': 0.00
                }
            },
            'Face 4': {
                'Gender': {
                    'male': 0.0,
                    'female': 1.0
                },
                'Glasses': {
                    'none': 1.0,
                    'optical': 0.0,
                    'sun': 0.0
                },
                'Underexposure': 0.01,
                'Race': {
                    'indian': 0.01,
                    'white': 0.94,
                    'black': 0.03,
                    'asian': 0.02
                },
                'Headpose': {
                    'roll': -8.0,
                    'pitch': -6.0,
                    'yaw': -25.0,
                },
                'Overexposure': 0.7,
                'Quality': -0.0,
                'Beard': 0.03,
                'Age': 26.0,
                'Liveness': 0.12,
                'Emotions': {
                    'neutral': 0.0,
                    'disgust': 0.0,
                    'surprise': 0.01,
                    'angry': 0.0,
                    'sad': 0.0,
                    'happy': 0.99,
                    'fear': 0.0
                },
                'Sharpness': 473.17,
                'Medmask': {
                    'none': 0.98, 'correct': 0.02, 'incorrect': 0.00
                }
            },
            'Face 5': {
                'Gender': {
                    'male': 1.0,
                    'female': 0.0
                },
                'Glasses': {
                    'none': 0.99,
                    'optical': 0.0,
                    'sun': 0.0
                },
                'Underexposure': 0.05,
                'Race': {
                    'indian': 0.21,
                    'white': 0.56,
                    'black': 0.12,
                    'asian': 0.11
                },
                'Headpose': {
                    'roll': -11.0,
                    'pitch': 2.0,
                    'yaw': 0.0,
                },
                'Overexposure': 0.53,
                'Quality': -0.0,
                'Beard': 0.14,
                'Age': 56.0,
                'Liveness': 0.01,
                'Emotions': {
                    'neutral': 0.0,
                    'disgust': 0.0,
                    'surprise': 0.03,
                    'sad': 0.0,
                    'happy': 0.97,
                    'fear': 0.0,
                    'angry': 0.0
                },
                'Sharpness': 1278.51,
                'Medmask': {
                    'none': 0.99, 'correct': 0.01, 'incorrect': 0.00
                }
            },
            'Face 2': {
                'Gender': {
                    'male': 1.0,
                    'female': 0.0
                },
                'Glasses': {
                    'none': 0.96,
                    'optical': 0.04,
                    'sun': 0.0
                },
                'Underexposure': 0.04,
                'Race': {
                    'indian': 0.01,
                    'white': 0.96,
                    'black': 0.02,
                    'asian': 0.01
                },
                'Headpose': {
                    'roll': -5.0,
                    'pitch': -18.0,
                    'yaw': 6.0,
                },
                'Overexposure': 0.56,
                'Quality': -0.0,
                'Beard': 0.27,
                'Age': 28.0,
                'Liveness': 0.1,
                'Emotions': {
                    'neutral': 0.01,
                    'disgust': 0.0,
                    'surprise': 0.07,
                    'sad': 0.0,
                    'happy': 0.93,
                    'fear': 0.0,
                    'angry': 0.0
                },
                'Sharpness': 1218.16,
                'Medmask': {
                    'none': 1.00, 'correct': 0.00, 'incorrect': 0.00
                }
            },
            'Face 3': {
               'Gender': {
                    'male': 0.0,
                    'female': 1.0
               },
               'Glasses': {
                    'none': 1.0,
                    'optical': 0.0,
                    'sun': 0.0
               },
               'Underexposure': 0.02,
               'Race': {
                    'indian': 0.2,
                    'white': 0.58,
                    'black': 0.14,
                    'asian': 0.09
               },
               'Headpose': {
                    'roll': -6.0,
                    'pitch': -3.0,
                    'yaw': 14.0,
               },
               'Overexposure': 0.53,
               'Quality': -0.0,
               'Beard': 0.03,
               'Age': 27.0,
               'Liveness': 0.69,
               'Emotions': {
                    'neutral': 0.0,
                    'disgust': 0.0,
                    'surprise': 0.03,
                    'angry': 0.0,
                    'sad': 0.0,
                    'happy': 0.97,
                    'fear': 0.0
               },
               'Sharpness': 670.98,
                'Medmask': {
                    'none': 0.96, 'correct': 0.04, 'incorrect': 0.00
                }
            }
        },
        None
    )
]
