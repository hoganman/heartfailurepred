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
See the [tensorflow_nn.ipynb](https://github.com/hoganman/heartfailurepred/blob/main/tensorflow_nn.ipynb) notebook for the data model and results.

## Bagged Random Forest (BARF)
Using scikit-learn, I define a ```BaggingClassifier``` with a random forest (NOT decision tree). 
This is unorthodox, but interesting to try. See the 
[sklearn_baggingclassifier.ipynb](https://github.com/hoganman/heartfailurepred/blob/main/sklearn_baggingclassifier.ipynb) notebook for the data model and results.

## Boosted Decision Tree (BDT)
Using scikit-learn, I define a ```DecisionTreeClassifier``` with AdaBoost. The BDT is quite robust in
general and requires little tuning for model convergence. However, I observe that the specificity is lower than the
bagging classifier. See the [sklearn_adaboostclassier.ipynb](https://github.com/hoganman/heartfailurepred/blob/main/sklearn_adaboostclassier.ipynb)
notebook for the data model and results. 

# Results

What I observe in the prediction data is that the ANN does really well compared to the bagged and adaBoosted methods.
I observe that the random forest methods could use more trees in the forest (larger ```n_estimators```)
Percentages are rounded to the nearest integer with floor (ceil) on values less (greater) than 0.5.

| Model        | Accuracy (%) | Sensitivity (%) | Specificity (%) | F1 Score |
|--------------|--------------|-----------------|-----------------|----------|
| ANN          | 84           | 91              | 74              | 86       |
| BARF         | 82           | 92              | 70              | 86       |
| BDT          | 78           | 96              | 58              | 82       |
