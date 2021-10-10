# import tensorflow as tf
import pandas as pd
import os
import numpy as np
from typing import Tuple
from src import enums


def get_csv_features_labels(filename: str) -> Tuple[np.ndarray, ...]:
    """Get the features and labels from a CSV file

    :param filename: The path to a input file
    :return: features, labels
    """
    if not os.path.isfile(filename):
        raise OSError(f'File {filename} does not exist')
    dataframe: pd.DataFrame
    dataframe = pd.read_csv(filename)
    dataframe['Sex'] = dataframe['Sex'].map(enums.SexTypes().data)
    dataframe['ChestPainType'] = dataframe['ChestPainType'].map(enums.ChestPainTypes().data)
    dataframe['RestingECG'] = dataframe['RestingECG'].map(enums.RestingECGTypes().data)
    dataframe['ExerciseAngina'] = dataframe['ExerciseAngina'].map(enums.ExerciseAnginaTypes().data)
    dataframe['ST_Slope'] = dataframe['ST_Slope'].map(enums.STSlopeTypes().data)
    for key_name in ['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak', 'HeartDisease']:
        dataframe[key_name] = dataframe[key_name].map(float)
    labels = np.array(dataframe.pop('HeartDisease'))
    features = np.array(dataframe)
    return features, labels
