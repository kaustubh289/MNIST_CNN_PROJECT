import numpy as np
import matplotlib.pyplot as plt
import random

def random_predictions(model, x_test, y_test, num_samples=5):
    for _ in range(num_samples):
        index = random.randint(0, len(x_test) - 1)
        img = x_test[index].reshape(28, 28)

        true_label = np.argmax(y_test[index])
        prediction = model.predict(np.expand_dims(x_test[index], axis=0))
        predicted_label = np.argmax(prediction)

        plt.imshow(img, cmap='gray')
        plt.title(f"Actual: {true_label} | Predicted: {predicted_label}")
        plt.axis('off')
        plt.show()
