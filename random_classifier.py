from collections import Counter
from random import choices


class RandomClassifier:

    def fit(self, X, y):
        """
            X -- заглушка для единообразия
        """
        counts = Counter(y)

        paired_probas = []

        for class_label in counts:
            paired_probas.append((class_label, counts[class_label] / counts.total()))

        self.classes = []
        self.weights = []

        for cls_, weight_ in paired_probas:
            self.classes.append(cls_)
            self.weights.append(weight_)

    def predict(self, X):

        preds = list()

        for _ in X:
            preds.append(
                choices(
                    population=self.classes,
                    weights=self.weights,
                    k=1
                )[0]
            )

        return preds

    def get_params(self, *args, **kwargs):
        return dict()
