import os

cwd = os.getcwd()

if not os.path.exists('model'):
    os.mkdir('model')

if not os.path.exists(f'{cwd}/result'):
    os.mkdir(f'{cwd}/result')

TRAIN_DATASET_PATH = f'{cwd}/dataset/train'
VALID_DATASET_PATH = f'{cwd}/dataset/valid'
TEST_DATASET_PATH = f'{cwd}/dataset/test'
MODEL_PATH = f'{cwd}/model'

MODEL = 'efficientdet_lite0'
MODEL_NAME = 'fish.tflite'
CLASSES = ['helmet','not_helmet', 'not_reflective','reflective']
EPOCHS = 100
BATCH_SIZE = 32