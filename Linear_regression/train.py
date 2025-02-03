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
    plt.savefig("Plot repartition")
    plt.clf()


def linear_regression(data):
    normal_Theta0 = 0
    normal_Theta1 = 0
    Theta0 = 0
    Theta1 = 0
    learn_rate = .01
    real_price = np.array(data["price"])
    real_mileage = np.array(data["km"])
    print(np.sum(real_price))
    print(np.sum(real_mileage))
    # Standardized price and mileage
    price = (real_price - real_price.mean()) / real_price.std()
    mileage = (real_mileage - real_mileage.mean()) / real_mileage.std()

    for i in range(0, 3000):
        print(i)
        # display_graph(real_mileage, real_price, normal_Theta0, normal_Theta1)
        predicted_price = Theta0 + (Theta1 * mileage)
        
        cost = np.sum((predicted_price - price) ** 2)
        # print("Result of cost :\n", cost, "\n")

        derive_Theta0 = (1 / price.size) * np.sum(predicted_price - price)
        derive_Theta1 = (1 / price.size) * np.sum((predicted_price - price) * mileage)

        normal_Theta1 = (Theta1 * real_price.std()) / real_mileage.std()
        normal_Theta0 = Theta0 * real_price.std() + real_price.mean() - normal_Theta1 * real_mileage.mean()

        Theta0 = Theta0 - learn_rate * derive_Theta0
        Theta1 = Theta1 - learn_rate * derive_Theta1
    display_graph(real_mileage, real_price, normal_Theta0, normal_Theta1)
    return (normal_Theta0, normal_Theta1)


def unstandart(values, dataset):
    return values * dataset.std() + dataset.mean()


def create_csv(Theta0, Theta1):
    with open("training_result.csv", "w") as file:
        file.write("Theta0,Theta1\n")
        file.write(f"{Theta0},{Theta1}")


if __name__ == "__main__":
    main()
