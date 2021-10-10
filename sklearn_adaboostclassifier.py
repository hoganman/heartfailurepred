import numpy as np
from sklearn import preprocessing
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.model_selection import train_test_split

from src import datareader, enums

filename = '/Users/mhogan/Documents/heartfailurepred/heart.csv'

keys, features, labels = datareader.get_csv_features_labels(filename)
tt_splits = train_test_split(features, labels, test_size=0.33)
features_train, features_test, labels_train, labels_test = tt_splits

normalized_features_train = preprocessing.normalize(features_train.swapaxes(0, 1)).swapaxes(0, 1)
normalized_features_test = preprocessing.normalize(features_test.swapaxes(0, 1)).swapaxes(0, 1)
normalized_features_test = normalized_features_test.reshape((len(normalized_features_test), len(keys)-1))

n_estimators_forest = 10000
n_estimators_adaboost = 20
random_forest_classifier: RandomForestClassifier = RandomForestClassifier(n_estimators=n_estimators_forest,
                                                                          max_depth=3,
                                                                          bootstrap=True,
                                                                          verbose=True,
                                                                          n_jobs=2)
adaboost_classifier: AdaBoostClassifier = AdaBoostClassifier(base_estimator=random_forest_classifier,
                                                             n_estimators=n_estimators_adaboost)

adaboost_classifier.fit(normalized_features_train, labels_train)

predictions_class = adaboost_classifier.predict(features_test)
true_classes = enums.HeartDiseaseClassification()
true_positive = np.count_nonzero(np.logical_and(predictions_class == true_classes.HeartDisease,
                                                labels_test == true_classes.HeartDisease).astype(int))
false_positive = np.count_nonzero(np.logical_and(predictions_class == true_classes.HeartDisease,
                                                 labels_test == true_classes.Normal).astype(int))
false_negative = np.count_nonzero(np.logical_and(predictions_class == true_classes.Normal,
                                                 labels_test == true_classes.HeartDisease).astype(int))
recall = true_positive / (false_negative + true_positive)
precision = true_positive / (true_positive + false_positive)
true_negative = np.count_nonzero(np.logical_and(predictions_class == true_classes.Normal,
                                                labels_test == true_classes.Normal).astype(int))
positives = np.count_nonzero((labels_test == true_classes.HeartDisease).astype(int))
negatives = len(labels_test) - positives


# Sensitivity, specificity, and F-score
sensitivity = float(true_positive) / positives
specificity = float(true_negative) / negatives
accuracy = (true_positive + true_negative) / (positives + negatives)
f1_score = 2. / (1./recall + 1./precision)
mcc = (true_positive * true_negative) - (false_positive * false_negative)
mcc /= np.sqrt((true_positive + false_positive) * (true_positive + false_negative) *
               (true_negative + false_positive) * (true_negative + false_negative))
print('accuracy = ', accuracy)
print('sensitivity = ', sensitivity)
print('specificity = ', specificity)
print('f1_score = ', f1_score)
print('mcc = ', mcc)
