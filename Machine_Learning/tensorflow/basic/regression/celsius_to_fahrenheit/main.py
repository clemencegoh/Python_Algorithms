"""
Regression problem
conversion between Celcius to Farenheight

:complete:
"""


import tensorflow as tf
import numpy as np
import sklearn.metrics
from data_generator import Generator


n = 100
tempGen = Generator(n)
tempCelc, tempFaren = tempGen.getData()
features = np.array(tempCelc)
labels = np.array(tempFaren)

# check examples
assert features.shape == labels.shape == (n,)

# parameters to adjust
learning_rate = 1

dense_layer = tf.keras.layers.Dense(units=1, input_shape=[1], activation='relu')

# build model, single dense layer
model = tf.keras.Sequential([
    dense_layer,
])

model.compile(
    loss='mean_squared_error',
    optimizer=tf.optimizers.Adam(learning_rate)
)

hist = model.fit(features, labels, epochs=100, verbose=False)

prediction_features = [0, 20, 40, 100]

prediction_labels = model.predict(prediction_features)
actual_labels = []

print("Estimated\t| Actual")
for i in range(len(prediction_features)):
    predicted = prediction_labels[i][0]
    actual = prediction_features[i] * 9 / 5 + 32
    actual_labels.append([actual])
    print("{}\t| {}".format(
        predicted,
        actual
    ))
print("MSE:", sklearn.metrics.mean_squared_error(prediction_labels, actual_labels))
