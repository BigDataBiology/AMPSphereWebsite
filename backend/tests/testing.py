import pytest
from fastapi.testclient import TestClient
from ..src.main import app
import pandas as pd

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200


inputs = pd.read_table('tests/inputs.tsv', sep='\t').fillna('')
inputs['Test path'] = inputs.apply(
    lambda x: x['API path'].format(accession=x['Input accession']) +
              ('?{}'.format(x['Input query']) if x['Input query'] != '' else ''),
    axis=1)
print(inputs[['Test path', 'Response code']].values.tolist())


@pytest.mark.parametrize('test_path, response_code', inputs[['Test path', 'Response code']].values.tolist())
def test_all(test_path, response_code):
    response = client.get(test_path)
    assert response.status_code == response_code
