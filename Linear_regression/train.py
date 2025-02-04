import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    data = read_dataset()
    if not data.empty:
        Theta0, Theta1 = linear_regression(data)
        create_csv(Theta0, Theta1)


def read_dataset() -> pd.DataFrame:
    try:
        data = pd.read_csv("data.csv")
        print("Dataset successfully open !")
        return (data)
    except FileNotFoundError:
        print("Unexpected error, impossible to read the dataset !")
        return (None)


def display_graph(mileage, price, Theta0, Theta1) -> None:
    plt.scatter(mileage, price, color='blue')
    plt.axline((0, Theta0), slope=Theta1, color='red')
    plt.ylim(0, 10000)
    # plt.show()
    plt.savefig("Plot repartition")
    plt.clf()


def linear_regression(data):
    learn_rate = .1
    Theta0 = 0
    Theta1 = 0
    real_price = np.array(data["price"])
    real_mileage = np.array(data["km"])

    # Standardized price and mileage
    price = standadized(real_price)
    mileage = standadized(real_mileage)

    for i in range(0, 100):
        # Values are standardized
        predicted_price = Theta0 + (Theta1 * mileage)
        cost = np.sum((predicted_price - price) ** 2)
        print("Result of cost :\n", cost, "\n")

        derive_Theta0 = (1 / price.size) * np.sum(predicted_price - price)
        derive_Theta1 = (1 / price.size) * np.sum((predicted_price - price) * mileage)
        print(f"derive theta0: {derive_Theta0:.4f}, derive theta1: {derive_Theta1:.4f}")

        Theta0 = Theta0 - learn_rate * derive_Theta0
        Theta1 = Theta1 - learn_rate * derive_Theta1

    # Values are no more standardized back to og values
    Theta0, Theta1 = unstandardized(Theta0, Theta1, real_price, real_mileage)
    display_graph(real_mileage, real_price, Theta0, Theta1)
    return (Theta0, Theta1)


def unstandardized(Theta0, Theta1, real_price, real_mileage):
    normal_Theta1 = (Theta1 * real_price.std()) / real_mileage.std()
    normal_Theta0 = Theta0 * real_price.std() + real_price.mean() - normal_Theta1 * real_mileage.mean()
    return normal_Theta0, normal_Theta1


def standadized(values):
    return (values - values.mean()) / values.std()


def create_csv(Theta0, Theta1):
    with open("training_result.csv", "w") as file:
        file.write("Theta0,Theta1\n")
        file.write(f"{Theta0},{Theta1}")


if __name__ == "__main__":
    main()
