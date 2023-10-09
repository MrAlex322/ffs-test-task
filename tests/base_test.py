from flask_fullstack import FlaskTestClient


def test_rest_docs(client: FlaskTestClient):
    result = client.get("/doc/", get_json=False)
    assert "text/html" in result.content_type


def test_missing_url(client: FlaskTestClient):
    client.get("/this/does/not/exist/", expected_status=404, get_json=False)


def test_incomplete_request(client: FlaskTestClient):
    client.post("/sign-up/", expected_status=400, get_json=False)
