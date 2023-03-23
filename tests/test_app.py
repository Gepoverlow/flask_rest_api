def test_get_all_pets(client):
    response = client.get("/rest/pets")
    assert response.json == []

