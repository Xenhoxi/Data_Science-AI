# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ljerinec <ljerinec@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/01/31 14:27:25 by ljerinec          #+#    #+#              #
#    Updated: 2025/02/03 15:34:49 by ljerinec         ###   ########.fr        #
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


def display_graph(data: pd.DataFrame, Theta0, Theta1) -> None:
    if not data.empty:
        data.plot.scatter(x="km", y="price")
        plt.axline((0, Theta0), slope=Theta1, color='green')
        # plt.savefig("Plot repartition")
        plt.show()


def linear_regression(data):
    Theta0 = 0
    Theta1 = 0
    learn_rate = 0.1
    price = np.array(data['price'])
    mileage = np.array(data['km'])
    norm_price = (price - np.min(price)) / (np.max(price) - np.min(price))
    norm_mileage = (mileage - np.min(mileage)) / (np.max(mileage) - np.min(mileage))
    print("Normalized price :\n", norm_price, "\n")
    print("Normalized mileage :\n", norm_mileage, "\n")

    for i in range(0, 1):
        predicted_price = Theta0 + (Theta1 * mileage)
        print("Predicted price for each mileage of the dataset:\n", predicted_price, "\n")
        # mse = np.array(predicted_price - norm_price)
        # mse = np.power(mse, 2)
        # sum_mse = np.sum(mse)
        # res_mse = 1 / mse.size * sum_mse
        # print("Result of MSE :\n", res_mse, "\n")

        # test = np.sum(predicted_price - norm_price)
        # print("Sum of norm values ", test)

        new_t0 = learn_rate * (1 / price.size) * np.sum(predicted_price - price)
        print(np.sum(predicted_price - price))
        new_t1 = learn_rate * (1 / price.size) * np.sum((predicted_price - price) * mileage)
        print(np.sum((predicted_price - price) * mileage))
        Theta0 = new_t0
        Theta1 = new_t1
        print("Theta0 =", Theta0)
        print("Theta1 =", Theta1)
        display_graph(data, Theta0, Theta1)
    # print(standt_data)


def undo_normalisation(value, dataset):
    return value * ((np.max(dataset) - np.min(dataset)) + np.min(dataset))







# standt_price = (price - price.mean()) / price.std()
    # standt_mileage = (mileage - mileage.mean()) / mileage.std()
    # print("Standardized price :\n", standt_price, "\n")
    # print("Standardized mileage :\n", standt_mileage, "\n")

    # for i in range(0, 20):
        # predicted_price = Theta0 + (Theta1 * standt_mileage)
        # print("Predicted price for each mileage of the dataset:\n", predicted_price, "\n")
        # mse = np.array(predicted_price - standt_price)
        # mse = np.power(mse, 2)
        # sum_mse = np.sum(mse)
        # res_mse = 1 / mse.size * sum_mse
        # print("Result of MSE :\n", res_mse, "\n")

        # test = np.sum(np.round(predicted_price, 4) - np.round(standt_price, 4))
        # print("test ", test)

        # new_t0 = learn_rate * (1 / mse.size) * np.sum(predicted_price - standt_price)
        # print("\n", learn_rate, (1 / mse.size), np.sum(predicted_price - standt_price))
        # print(new_t0)
        # new_t1 = learn_rate * (1 / mse.size) * np.sum((predicted_price - standt_price) * standt_mileage)
        # print(new_t1)
        # Theta0 = new_t0
        # Theta1 = new_t1
        # print("Theta0 =", Theta0)
        # print("Theta1 =", Theta1)
        # display_graph(data, Theta0 * price.std() + price.mean(), Theta1 * mileage.std() + mileage.mean())
    # print(standt_data)






if __name__ == "__main__":
    main()
