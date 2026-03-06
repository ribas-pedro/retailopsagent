import pytest


def test_health_endpoint() -> None:
    fastapi = pytest.importorskip('fastapi')
    testclient = pytest.importorskip('fastapi.testclient')
    app_module = __import__('retailops.api.main', fromlist=['app'])
    client = testclient.TestClient(app_module.app)
    response = client.get('/health')
    assert response.status_code == fastapi.status.HTTP_200_OK
    assert response.json() == {'status': 'ok'}
