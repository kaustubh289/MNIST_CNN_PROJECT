def train_model(model, x_train, y_train):
    history = model.fit(
        x_train,
        y_train,
        epochs=8,
        batch_size=64,
        validation_split=0.1
    )
    return history