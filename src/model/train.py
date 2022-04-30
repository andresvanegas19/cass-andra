from keras.callbacks import Callback
import imp
from create import create_model
from src.processing.split import preprocess
from src.processing.reshaping import scaling
from src.data.load import nasqad_historical


def train_lstm():
    """
    training the lstm model
    """
    len_sq = 100
    df = nasqad_historical()

    X_train, y_train, X_test, y_test = preprocess(
        scaling(df),
        len_sq,
        train_split=0.80
    )

    model = create_model()
    model.fit(
        X_train,
        y_train,
        epochs=30,
        batch_size=64,
        shuffle=False,
        validation_split=0.1
    )
    model.save('save/lstm')

    model.evaluate(X_test, y_test)


class EarlyStoppingByLossVal(Callback):
    def __init__(self, monitor='val_loss', value=0.0016, verbose=0):
        super(Callback, self).__init__()
        self.monitor = monitor
        self.value = value
        self.verbose = verbose

    def on_epoch_end(self, epoch, logs={}):
        current = logs.get(self.monitor)
        if current is None:
            print("stopping requires %s " %
                  self.monitor, RuntimeWarning)

        if current <= self.value:
            if self.verbose > 0:
                print("Epoch %05d: stopping THR" % epoch)
            self.model.stop_training = True


def train_gru(model, X_train, y_train, X_test, y_test):

    # callbacks = [
    #     EarlyStoppingByLossVal(monitor='val_loss', value=0.0016, verbose=1),
    # ]
    model.fit(
        X_train,
        y_train,
        validation_data=(X_test, y_test),
        epochs=100,
        batch_size=3,
        verbose=1
    )
    model.save('model/save/gru')
