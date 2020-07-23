import tensorflow as tf

features = tf.constant([[12, 23, 10, 17],[1,2,3,4]])
print(features)
labels = tf.constant([0, 1])
print(labels)
dataset = tf.data.Dataset.from_tensor_slices((features, labels))
for element in dataset:
    print(element)
