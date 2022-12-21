"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW13.2.1 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - handwritten digits recognition machine learning
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.12.02
* ==========================================================================
* 프로그램 수정 / 보완 이력
* ==========================================================================
* 프로그램 수정자		일자			    버전		수정내용
* JH KIM			2022.12.02	    v1.0	최초 작성
"""
import tensorflow as tf
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
kr_utils = tf.keras.utils
import matplotlib.pyplot as plt


def main():
    print("Loading MNIST data . . . .")
    mnist_npz_path = 'C://MyPyPackage//MNIST//mnist.npz'        # data path
    (X_train, y_train), (X_test, y_test) = mnist.load_data(path=mnist_npz_path) # load_data
    digit_names = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    plt.figure(figsize=(10, 5))                 # figure size = (10, 5)
    for i in range(10):
        plt.subplot(2, 5, i + 1)
        plt.imshow(X_train[i], cmap="gray")     # show
        plt.title(digit_names[y_train[i]])
        plt.axis('off')
    plt.show()

    print("Reshaping format . . . .")
    X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32')    # reshape
    X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype('float32')       # reshape

    print("Converting class vector . . . .")

    y_train = tf.keras.utils.to_categorical(y_train)
    y_test = tf.keras.utils.to_categorical(y_test)

    X_train = X_train / 255
    X_test = X_test / 255
    print("Preparing a CNN model . . . .")

    num_classes = 10
    model = Sequential([
        Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        Flatten(),
        Dense(256, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')])  # setting model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])      # compile
    print("Fitting the model . . . .")

    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20, batch_size=200, verbose=2)
    print("The model has successfully trained")

    model.save("CNN_model_Digits")                  # save
    print("The model has successfully saved !!")
    model.summary()                                 # print model

    scores = model.evaluate(X_test, y_test, verbose=0)      # evaluate
    print("CNN error: {}".format(100 - (scores[1] * 100)))  # error rate

if __name__ == "__main__":
    main()
