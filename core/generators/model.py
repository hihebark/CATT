from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Activation, Dropout, Dense
from keras.layers import Flatten, Input, Lambda
from keras.models import Model, Sequential

def create_cnn(width, height, depth, filters=(16, 32, 64), regress=False):
    input_shape = (height, width, depth)
    model = Sequential()

    model.add(Lambda(lambda x: x/255.0, input_shape=input_shape))

    model.add(Conv2D(64, (3, 3),
        kernel_initializer='uniform', activation='elu', strides=(2, 2)))
    model.add(Conv2D(32, (3, 3),
        kernel_initializer='uniform', activation='elu', strides=(2, 2)))
    model.add(Conv2D(16, (3, 3),
        kernel_initializer='uniform', activation='elu', strides=(2, 2)))

    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(BatchNormalization())

    model.add(Flatten())
    model.add(Dense(4, activation='elu'))
    model.add(Dropout(.5))
    model.add(Dense(1))
    return model