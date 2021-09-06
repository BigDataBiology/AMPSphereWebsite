from .inputs import unexpected_inputs
import pytest


@pytest.fixture
def test_read_by_filter(client, query_type, filter_by, categories):
    """

    :param query_type: query type: amp or family
    :param filter_by: one of {family, host, sample, origin, habitat}
    :param categories: a list of filter inputs. eg. {SPHERE-III.000_000, foo, bar}
    :return:
    """
    for category in categories:
        response = client.get(f'/v1/{query_type}?{filter_by}={category}')
        assert response.status_code == 200
        if category in unexpected_inputs:
            assert response.json() == []
        else:
            assert all([obj[filter_by] == category for obj in response.json()])