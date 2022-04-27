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
