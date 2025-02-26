from dataset import Dataset
import matplotlib.pyplot as plt
import numpy as np
import sys
import math


def main() -> None:
    try:
        dataset = Dataset(sys.argv[1])
        set = dataset.get_dataset()
        print(set)
        print(set.columns)
        print(set.index)

        features_name = dataset.clean_data_describe().columns
        ncols = round(math.sqrt(len(features_name)))
        fig, ax = plt.subplots(ncols=ncols, nrows=ncols, figsize=(29, 18))

        for a in ax.ravel():
            a.axis("off")

        i = 0
        all_house = set['Hogwarts House'].unique()
        for feature_name in features_name:
            x = math.floor(i / ncols)
            y = math.floor(i % ncols)
            for house in all_house:
                data_by_house = set.loc[set['Hogwarts House'] == house]
                feature = data_by_house[feature_name]
                ax[x,y].hist(feature)
                ax[x,y].title.set_text(feature_name)
                ax[x,y].axis("on")
            i += 1

        plt.show()
    except (KeyboardInterrupt) as err:
        pass


if __name__ == '__main__':
    main()