# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ljerinec <ljerinec@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/01/31 14:27:25 by ljerinec          #+#    #+#              #
#    Updated: 2025/02/03 16:54:38 by ljerinec         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    data = read_dataset()
    if not data.empty:
        linear_regression(data)


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
    plt.axline((0, Theta0), slope=Theta1, color='green')
    plt.savefig("Plot repartition")
    # plt.show()
    plt.clf()


def linear_regression(data):
    normal_Theta0 = 0
    normal_Theta1 = 0
    Theta0 = 0
    Theta1 = 0
    learn_rate = .1
    real_price = np.array(data["price"])
    real_mileage = np.array(data["km"])
    # price = np.array([2, 3, 4])
    # mileage = np.array([1, 2, 3])
    print(np.sum(real_price))
    print(np.sum(real_mileage))
    # Standardized price and mileage
    price = (real_price - real_price.mean()) / real_price.std()
    mileage = (real_mileage - real_mileage.mean()) / real_mileage.std()
    # Normalized price and mileage
    # price = (real_price - np.min(real_price)) / (np.max(real_price) - np.min(real_price))
    # mileage = (real_mileage - np.min(real_mileage)) / (np.max(real_mileage) - np.min(real_mileage))
    # print("Normalized price :\n", norm_price, "\n")
    # print("Normalized mileage :\n", norm_mileage, "\n")

    for i in range(0, 3000):
        predicted_price = Theta0 + (Theta1 * mileage)
        print("Predicted price for each mileage of the dataset:\n", predicted_price, "\n")
        
        cost = np.sum((predicted_price - price) ** 2)
        print("Result of cost :\n", cost, "\n")

        derive_Theta0 = (1 / price.size) * np.sum(predicted_price - price)
        print("sum :", np.sum(predicted_price - price))
        print("Derive theta0 :", derive_Theta0)
        derive_Theta1 = (1 / price.size) * np.sum((predicted_price - price) * mileage)
        print("sum :", np.sum((predicted_price - price) * mileage))
        print("Derive theta1 :", derive_Theta1)
        # display_graph(real_mileage, real_price, normal_Theta0, normal_Theta1)
        print("Theta0 =", Theta0)
        print("Theta1 =", Theta1)
        normal_Theta1 = (Theta1 * real_price.std()) / real_mileage.std()
        normal_Theta0 = Theta0 * real_price.std() + real_price.mean() - normal_Theta1 * real_mileage.mean()
        print("Normal T0:", normal_Theta0)
        print("Normal T1:", normal_Theta1)
        Theta0 = Theta0 - learn_rate * derive_Theta0
        Theta1 = Theta1 - learn_rate * derive_Theta1
        print(unstandart(mileage, real_mileage))
        print(unstandart(price, real_price))
    display_graph(real_mileage, real_price, normal_Theta0, normal_Theta1)


def undo_normalisation(value, dataset):
    return value * ((np.max(dataset) - np.min(dataset)) + np.min(dataset))


def unstandart(values, dataset):
    return values * dataset.std() + dataset.mean()


if __name__ == "__main__":
    main()
