def try_me():
    print("Hello this is Filippo's first function")

def simple_sum(a,b):
    return a+b

def get_model(n_units1, n_units2, n_units3):
    from tensorflow.keras import Sequential, layers
    model = Sequential()
    model.add(layers.Dense(n_units1, input_shape = (10,), activation = 'relu'))
    model.add(layers.Dense(n_units2, activation = 'relu'))
    model.add(layers.Dense(n_units3, activation = 'softmax'))
    return model

def get_summary_func(n_units1, n_units2, n_units3):
    model = get_model(n_units1, n_units2, n_units3)
    print(model.summary())
    return model.summary()

    