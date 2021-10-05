# Simple model server

## Goal

Write a basic model server that does the following

- Loads a model from disk
- Serves that model at a route `/predict`

We should be able to run

```
curl -X POST http://localhost:5000/predict -d '{ "inputs": [[1,1,1,1]]  }'
```
and get a response.

The model serialized as `models/rfcmodel.joblib` is a scikit-learn RandomForestClassifier trained on the Iris dataset. It can be loaded into memory with

```python
import joblib

model = joblib.load('models/rfcmodel.joblib')
model

{'model': RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_weight=None,
                        criterion='gini', max_depth=None, max_features='auto',
                        max_leaf_nodes=None, max_samples=None,
                        min_impurity_decrease=0.0, min_impurity_split=None,
                        min_samples_leaf=1, min_samples_split=2,
                        min_weight_fraction_leaf=0.0, n_estimators=100,
                        n_jobs=None, oob_score=False, random_state=None,
                        verbose=0, warm_start=False),
 'feature_names': ['sepal length (cm)',
  'sepal width (cm)',
  'petal length (cm)',
  'petal width (cm)'],
 'classes': ['setosa', 'versicolor', 'virginica']}
```

## Resources

- The internet
- Me
- Whatever else you need I'm not your dad

## Extension

- Add the ability to hot swap a model: given a URL, download the model and swap it out for the old one.
- Add the ability to run validations on input data and handle erroneous inputs
- Create an A/B testing framework where the predict endpoint serves one of N models with some probability specified by some config.
