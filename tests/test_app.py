class TestRest:
    def test_get_all_pets_should_be_empty_list(self, client):
        response = client.get("/rest/pets")

        assert response.status_code == 200
        assert response.json == []

    def test_get_all_pets_should_not_be_empty_list(self, client):
        client.post("/rest/pets", json={

            "name": "Rafaelis",
            "age": 34,
            "isPlayful": False

        })

        response = client.get("/rest/pets")

        assert response.status_code == 200
        assert len(response.json) is 1
        assert response.json[0]['name'] == 'Rafaelis'
        assert response.json[0]['age'] is 34
        assert response.json[0]['isPlayful'] is False
