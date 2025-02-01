# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ljerinec <ljerinec@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/01/31 14:27:25 by ljerinec          #+#    #+#              #
#    Updated: 2025/02/01 18:16:17 by ljerinec         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    data = read_dataset()
    if not data.empty:
        linear_regression(data)
        display_graph(data)


def read_dataset() -> pd.DataFrame:
    try:
        data = pd.read_csv("data.csv")
        print("Dataset successfully open !")
        return (data)
    except FileNotFoundError:
        print("Unexpected error, impossible to read the dataset !")
        return (None)


def display_graph(data: pd.DataFrame) -> None:
    if not data.empty:
        data.plot.scatter(x="km", y="price")
        plt.axline((0, 0), slope=0, color='green')
        plt.savefig("Plot repartition")
        # plt.show()


def linear_regression(data):
    Theta0 = 0.5
    Theta1 = 0

    price = np.array(data['price'])
    mileage = np.array(data['km'])
    standt_price = (price - price.mean()) / price.std()
    standt_mileage = (mileage - mileage.mean()) / mileage.std()
    print("Standardized price :\n", standt_price, "\n")
    print("Standardized mileage :\n", standt_mileage, "\n")

    predicted_price = Theta0 + (Theta1 * standt_mileage)
    print("Predicted price for each mileage of the dataset:\n", predicted_price, "\n")
    # predicted_price.rename(columns={"km": "price"}, inplace=True)
    # print(predicted_price)
    # print(standt_data["price"])
    # print(predicted_price.subtract(standt_data["price"]))
    # mse = 1 / predicted_price.size() * (predicted_price - price).pow(2)
    mse = np.array(predicted_price - standt_price)
    mse = np.power(mse, 2)
    print("Result of pow:\n", np.around(mse, 2), "\n")
    sum_mse = np.sum(mse)
    real_sum = 0
    for i in mse:
        real_sum += i
    print("Result of real_sum:\n", real_sum, "\n")
    print("Result of sum:\n", sum_mse, "\n")
    print("MSE size:\n", mse.size, "\n")
    res_mse = 1 / mse.size * sum_mse
    print("Res MSE size:\n", res_mse, "\n")
    
    # print(predicted_price.shape[0])
        # new_t0 = 
        # new_t1 = 

    # print(standt_data)


if __name__ == "__main__":
    main()
