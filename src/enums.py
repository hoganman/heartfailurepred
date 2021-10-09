from collections import UserDict
from typing import Final


class SexTypes(UserDict[str, float]):

    M: Final[float] = 0.0
    F: Final[float] = 1.0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = {
            'M': self.M,
            'F': self.F
        }


class ChestPainTypes(UserDict[str, float]):
    TA: Final[float] = 0.0  # Typical Angina
    ATA: Final[float] = 1.0  # Atypical Angina
    NAP: Final[float] = 2.0  # Non - Anginal Pain
    ASY: Final[float] = 3.0  # Asymptomatic

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = {
            'TA': self.TA,
            'ATA': self.ATA,
            'NAP': self.NAP,
            'ASY': self.ASY
        }


class RestingECGTypes(UserDict):
    Normal: Final[float] = 0.0  # Normal
    ST: Final[float] = 1.0  # Having ST-T wave abnormality
    LVH: Final[float] = 2.0  # Showing probable or definite left ventricular hypertrophy by Estes' criteria

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = {
            'Normal': self.Normal,
            'ST': self.ST,
            'LVH': self.LVH
        }


class ExerciseAnginaTypes(UserDict[str, float]):

    Y: Final[float] = 1.0
    N: Final[float] = 0.0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = {
            'Y': self.Y,
            'N': self.N
        }


class STSlopeTypes(UserDict[str, float]):
    Up: Final[float] = 1.0  # upsloping
    Flat: Final[float] = 0.0  # flat
    Down: Final[float] = -1.0  # downsloping

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = {
            'Up': self.Up,
            'Flat': self.Flat,
            'Down': self.Down
        }


class HeartDiseaseClassification(UserDict[int, str]):
    Normal: Final[int] = 0
    HeartDisease: Final[int] = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = {
            self.Normal: 'Normal',
            self.HeartDisease: 'Heart disease',
        }
