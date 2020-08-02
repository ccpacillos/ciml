from typing import List, Tuple, Any

FeatureValue = Tuple[List[Any], Any]


class Dataset:
    def __init__(self, features: List[str], feature_values: List[FeatureValue]):
        if all(len(tup[0]) == len(features) for tup in feature_values) == False:
            raise Exception(
                'Feature values does not match features/dimensions.')

        self.features = features
        self.feature_values = feature_values
