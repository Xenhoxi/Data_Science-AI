# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ljerinec <ljerinec@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/18 15:37:57 by ljerinec          #+#    #+#              #
#    Updated: 2025/02/18 16:00:51 by ljerinec         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def main():
    try:
        assert len(sys.argv) == 2, "Wrong numbers of arguments"
        check_path(sys.argv[1])
    except (AssertionError) as err:
        print(err)
    except (KeyboardInterrupt):
        pass


def check_path():
    pass


if __name__ == "__main__":
    main()
