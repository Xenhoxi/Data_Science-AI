# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ljerinec <ljerinec@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/18 15:37:57 by ljerinec          #+#    #+#              #
#    Updated: 2025/02/18 17:22:10 by ljerinec         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import pandas as pd


def main():
    try:
        assert len(sys.argv) == 2, "Wrong numbers of arguments"
        Dataset = read_dataset(sys.argv[1])
        if Dataset is not None:
            print("Dataset read successfully")
    except (AssertionError) as err:
        print(f"AssertionError: {err}")
    except (KeyboardInterrupt):
        pass


def read_dataset(path: str) -> pd.DataFrame:
    try:
        data = pd.read_csv(path)
        return (data)
    except FileNotFoundError:
        print("Unexpected error, impossible to read the dataset !")
        return (None)


if __name__ == "__main__":
    main()
