import tensorflow as tf

classes = 3
labels = tf.constant([1, 0, 2],dtype=tf.float32)  # 输入的元素值最小为0，最大为2
print(labels)
output = tf.one_hot(labels, depth=classes)
print("result of labels1:", output)
print("\n")
