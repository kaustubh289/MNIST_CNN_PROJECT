from src.data_loader import load_data
from src.model import build_model
from src.train import train_model
from src.evaluate import evaluate_model
from src.predict import random_predictions
from outputs.plots import plot_accuracy, plot_loss

def main():
    # Load data
    x_train, y_train, x_test, y_test = load_data()

    # Build model
    model = build_model()

    # Train
    history = train_model(model, x_train, y_train)

    # Plot results
    plot_accuracy(history)
    plot_loss(history)

    # Evaluate
    evaluate_model(model, x_test, y_test)

    # Predictions
    random_predictions(model, x_test, y_test)

if __name__ == "__main__":
    main()