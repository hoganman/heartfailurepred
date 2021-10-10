# heartfailurepred
Taken from https://www.kaggle.com/fedesoriano/heart-failure-prediction on October 9 2021 MDT.

In this repository, I explore the power of an artificial neural-network (ANN) from that of
a bagged random forest (BARF) and boosted decision tree (BDT) classifiers. The data is taken from
Kaggle to predict heart disease. The data set is semi-large
with ~900 patients. There is no distinction between male and female patients. The output classes are 0 (normal)
and 1 (heart disease)

# Models

## Artificial Neural Network (ANN) Model
Using TensorFlow version 2.4, I define a single, fully-connected ```tf.keras.layers.Dense``` hidden layer
multi-layer perceptron (MLP). The number of nodes in the layer 2x times the number of input-features.

## Boosted Decision Tree (BDT)
Using scikit-learn, I define a ```RandomForestClassifier``` with AdaBoost defaults. The BDT is quite robust in 
general and requires little tuning for model convergence. However, this data is not too large (much less than thousands) 
and the variance of the prediction could be high. Using bagging should help.

## Bagged Random Forest (BARF)
Using scikit-learn, I define a ```BaggingClassifier``` with the defaults. The advantage of BARF over BDT is that
with the bootstrapping enabled, we can reduce the effects of high variance from non-bagging
methods.

# Results

What I observe in the prediction data is that the ANN does really well compared to the bagged and adaBoosted methods.
I observe that the random forest methods could use more trees in the forest (larger ```n_estimators```)
Percentages are rounded to the nearest integer with floor (ceil) on values less (greater) than 0.5.

| Model        | Accuracy (%) | Sensitivity (%) | Specificity (%) | F1 Score | 
|--------------|--------------|-----------------|-----------------|----------|
| ANN          | 84           | 93              | 74              | 85       |
| BARF         | 82           | 92              | 68              | 85       |
| BDT          | 83           | 94              | 69              | 87       |
