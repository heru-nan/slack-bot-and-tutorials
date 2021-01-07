import keras;
import tensorflow as tf
import tensorflowjs as tfjs

mn = tf.keras.applications.MobileNet(
    input_shape=None,
    alpha=1.0,
    depth_multiplier=1,
    dropout=0.001,
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
)
print(mn.summary())

tfjs.converters.save_keras_model(mn, '../static/tfjs-models/MobileNet')