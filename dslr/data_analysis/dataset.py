import pandas as pd
import numpy as np


class Dataset:
    def __init__(self, path: pd.DataFrame):
        if type(path) is str and not None:
            self.__dataset = self.read_dataset(path)
        else:
            self.__dataset = pd.DataFrame()
    

    def read_dataset(self, path: str) -> pd.DataFrame:
        try:
            data = pd.read_csv(path)
            return (data)
        except FileNotFoundError:
            print("Unexpected error, impossible to read the dataset check the given path !")
            return (pd.DataFrame())

    def display_statistics(self):
        # Select all collums of a specific types
        col_type = self.__dataset.select_dtypes(include=float)
        # print(col_type)
        # Get all the collumns names
        col_name = col_type.columns
        # print(col_name)
        # Remove all na row
        no_na_set = col_type.dropna()
        print(no_na_set)

        test = [len(no_na_set[col]) for col in no_na_set]
        print(np.array(test))

        # stats = pd.DataFrame(columns=col_name, index=["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"])
        # print(stats)


    def get_dataset(self):
        return self.__dataset


    def display_set(self):
        if not self.__dataset.empty:
            print(self.__dataset)

    
    def count(self):
        pass