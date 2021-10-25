import requests


PORT = 5000
MODEL_ADDRESS = 'https://github.com/howespt/model-server-interview/raw/master/models/rfcmodel.joblib'
BAD_MODEL_ADDRESS = 'https://github.com/howespt/model-server-interview/raw/master/models/non-existent-model.joblib'


def test_api_predict():
    """
    Test API predict
    """
    url = f'http://localhost:{PORT}/predict'
    inputs = {'inputs': [[1,2,3,4]]}
    response = requests.post(url, json=inputs)
    assert response.status_code == 200
    assert response.json() == {'predictions': [0]}


def test_api_predict_multiple():
    """
    Test API predict multiple
    """
    url = f'http://localhost:{PORT}/predict'
    inputs = {'inputs': [[1,2,3,4], [1,2,3,4]]}
    response = requests.post(url, json=inputs)
    assert response.status_code == 200
    assert response.json() == {'predictions': [0, 0]}


def test_api_predict_invalid_input():
    """
    Test API predict invalid input
    """
    url = f'http://localhost:{PORT}/predict'
    inputs = {'inputs': [[1,2,3,4,5]]}
    response = requests.post(url, json=inputs)
    assert response.status_code == 400
    assert response.json() == {'error': 'Invalid input'}


def test_api_predict_invalid_input_type():
    """
    Test API predict invalid input type
    """
    url = f'http://localhost:{PORT}/predict'
    inputs = {'inputs': {'inputs': [[1,2,3,4]]}}
    response = requests.post(url, json=inputs)
    assert response.status_code == 400
    assert response.json() == {'error': 'Invalid input type'}


def test_update_model():
    """
    Test API update model
    """
    url = f'http://localhost:{PORT}/update-model'
    data = {'model_url': MODEL_ADDRESS}
    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert response.json() == {'success': True}


def test_update_model_invalid_url():
    """
    Test API update model invalid url
    """
    url = f'http://localhost:{PORT}/update-model'
    data = {'model_url': BAD_MODEL_ADDRESS}
    response = requests.post(url, json=data)
    assert response.status_code == 400
    assert response.json() == {'error': 'Invalid model url'}
