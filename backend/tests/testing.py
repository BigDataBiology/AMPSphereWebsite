from fastapi.testclient import TestClient
from ..src.main import app
from .utils import test_read_by_filter
from .inputs import *


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200


def test_read_amps_by_filters():
    filter_by_options = ['family', 'host', 'sample', 'habitat', 'origin']
    filter_by_categories = [
        family_accessions.union(unexpected_inputs),
        hosts.union(unexpected_inputs),
        samples.union(unexpected_inputs),
        habitats.union(unexpected_inputs),
        origins.union(unexpected_inputs)
    ]
    for option, categories in zip(filter_by_options, filter_by_categories):
        test_read_by_filter(client, query_type='amp', filter_by=option, categories=categories)


def test_read_amp():
    url_prefix = '/v1/amps/'
    base_urls = {'', '/features', '/distributions', '/metadata'}
    input_accs = AMP_accessions.union(unexpected_inputs)
    for base_url in base_urls:
        url = url_prefix + '{}' + base_url
        for acc in input_accs:
            response = client.get(url.format(acc))
            assert response.status_code == 200
            if acc in unexpected_inputs:
                assert response.json() == {}
            else:
                assert response.json()['accession'] == acc


def test_read_family_by_filters():
    filter_by_options = ['host', 'sample', 'habitat', 'origin']
    filter_by_categories = [
        hosts.union(unexpected_inputs),
        samples.union(unexpected_inputs),
        habitats.union(unexpected_inputs),
        origins.union(unexpected_inputs)
    ]
    for option, categories in zip(filter_by_options, filter_by_categories):
        test_read_by_filter(client, query_type='family', filter_by=option, categories=categories)


def test_read_family():
    url_prefix = '/v1/families/'
    base_urls = {'', '/features', '/distributions', '/downloads'}
    input_accs = family_accessions.union(unexpected_inputs)
    for base_url in base_urls:
        url = url_prefix + '{}' + base_url
        for acc in input_accs:
            response = client.get(url.format(acc))
            assert response.status_code == 200
            if acc in unexpected_inputs:
                assert response.json() == {}
            else:
                assert response.json()['accession'] == acc


def test_sequence_search():
    input_sequences = sequences.union(unexpected_inputs)
    url_base = '/v1/search/{}?query={}'
    methods = {'mmseqs', 'hmmer'}
    for method in methods:
        for seq in input_sequences:
            print(f'testing search method `{method}` with input `{seq}`')
            url = url_base.format(method, seq)
            response = client.get(url)
            assert response.status_code == 200
            assertion_result = dict(status_code_checking=response.status_code == 200, data_checking=None)
            if seq not in sequences:
                assert response.json() == []
                assertion_result['data_checking'] = response.json() == []
            else:
                assert type(response.json()) == list
                assertion_result['data_checking'] = type(response.json()) == list
            print(assertion_result)