import tensorflow as tf
import tensorflowjs as tfjs

vgg16 = tf.keras.applications.VGG16(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
)
print(vgg16.summary()) 

tfjs.converters.save_keras_model(vgg16, '../static/tfjs-models/VGG16')
