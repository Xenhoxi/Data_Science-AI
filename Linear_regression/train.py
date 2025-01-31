# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ljerinec <ljerinec@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/01/31 14:27:25 by ljerinec          #+#    #+#              #
#    Updated: 2025/01/31 18:44:55 by ljerinec         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import matplotlib.pyplot as plt


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


def display_graph(data: pd.DataFrame) -> None:
    if not data.empty:
        data.plot.scatter(x="km", y="price")
        plt.savefig("Plot repartition")


def linear_regression(data):
    standardisation_data = (data - data.mean()) / data.std()

    print(standardisation_data)


if __name__ == "__main__":
    main()
