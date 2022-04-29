from src.processing.reshaping import sequences_convert


def preprocess(data, len_sq, train_split):
    """_summary_

    Args:
        data (_type_): _description_
        len_sq (_type_): _description_
        train_split (_type_): _description_

    Returns:
        _type_: _description_
    """
    data = sequences_convert(data, len_sq)
    num_train = int(train_split * data.shape[0])

    X_train = data[:num_train, :-1, :]
    y_train = data[:num_train, -1, :]
    X_test = data[num_train:, :-1, :]
    y_test = data[num_train:, -1, :]

    return X_train, y_train, X_test, y_test
