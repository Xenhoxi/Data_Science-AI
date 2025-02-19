# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ljerinec <ljerinec@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/18 15:37:57 by ljerinec          #+#    #+#              #
#    Updated: 2025/02/19 13:38:13 by ljerinec         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import pandas as pd
from dataset import Dataset


def main():
    try:
        assert len(sys.argv) == 2, "Wrong numbers of arguments"
        dataset = Dataset(sys.argv[1])
        dataset.display_statistics()
    except (AssertionError) as err:
        print(f"AssertionError: {err}")
    except (KeyboardInterrupt):
        pass


if __name__ == '__main__':
    main()