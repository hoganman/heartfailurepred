from collections import UserDict
from typing import Dict


class SexTypes(UserDict):
    """Male and Female sexes mapping from str -> float"""
    M: float = -1.0  # Male
    F: float = +1.0  # Female

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data: Dict[str, float]
        self.data = {
            'M': self.M,
            'F': self.F
        }


class ChestPainTypes(UserDict):
    """Chest pain classifications mapping from str -> float"""
    TA: float = -1.0  # Typical Angina
    ATA: float = -1./3  # Atypical Angina
    NAP: float = 1./3  # Non - Anginal Pain
    ASY: float = 1.0  # Asymptomatic

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data: Dict[str, float]
        self.data = {
            'TA': self.TA,
            'ATA': self.ATA,
            'NAP': self.NAP,
            'ASY': self.ASY
        }


class RestingECGTypes(UserDict):
    """Resting ECG classification mappings from str -> float"""
    Normal: float = -1.0  # Normal
    ST: float = 0.0  # Having ST-T wave abnormality
    LVH: float = 1.0  # Showing probable or definite left ventricular hypertrophy by Estes' criteria

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data: Dict[str, float]
        self.data = {
            'Normal': self.Normal,
            'ST': self.ST,
            'LVH': self.LVH
        }


class ExerciseAnginaTypes(UserDict):
    """Exercise angina mapping from str -> float"""
    Y: float = 1.0
    N: float = -1.0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data: Dict[str, float]
        self.data = {
            'Y': self.Y,
            'N': self.N
        }


class STSlopeTypes(UserDict):
    """ST-wave slope type mapping from str -> float"""
    Up: float = 1.0  # upsloping
    Flat: float = 0.0  # flat
    Down: float = -1.0  # downsloping

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data: Dict[str, float]
        self.data = {
            'Up': self.Up,
            'Flat': self.Flat,
            'Down': self.Down
        }


class HeartDiseaseClassification(UserDict):
    """The output classification mapping from int -> str"""
    Normal: int = 0
    HeartDisease: int = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data: Dict[str, int]
        self.data = {
            self.Normal: 'Normal',
            self.HeartDisease: 'Heart disease',
        }

