# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ljerinec <ljerinec@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/01/31 13:50:41 by ljerinec          #+#    #+#              #
#    Updated: 2025/01/31 15:11:02 by ljerinec         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def main():
    mileage = None

    while not mileage:
        mileage = input_mileage()
    mileage = int(mileage)
    result = predict_price(mileage)
    print("The estimate price is", str(result) + "$")


def input_mileage():
    try:
        mileage = input("What's the mileage you want to estimate the price ? ")
        int(mileage)
        return (mileage)
    except ValueError:
        print("Input a valid mileage please ! Should be an integer in Km")
        return (None)


def predict_price(mileage):
    Theta0 = 0
    Theta1 = 0
    # Retrieve T0 and T1 from the training resutl file
    return (Theta0 + (Theta1 * mileage))


if __name__ == "__main__":
    main()
