import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt


IMAGE_SIZE = 256
BATCH_SIZE = 32
data_set = tf.keras.preprocessing.image_dataset_from_directory(
    "D:\DataSets\Sugarcane Dataset",
    shuffle = True,
    image_size = (IMAGE_SIZE,IMAGE_SIZE),
    batch_size = BATCH_SIZE,
)
class_names = data_set.class_names
