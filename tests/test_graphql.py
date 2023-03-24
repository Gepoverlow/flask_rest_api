import pytest


class TestGraphql:
    @pytest.mark.usefixtures("app_ctx")
    def test_delete_non_existent_pet_should_return_error_msg(self, graphql_client):
        result = graphql_client.execute("""
        mutation {
            deletePet(petId:"2"){
                pet{
                    name
                    age
                    isPlayful
                },
                ok
            }

        }   
        """)

        assert result["errors"][0]["message"] == 'Pet with id 2 has not been found'

    @pytest.mark.usefixtures("app_ctx")
    def test_delete_existent_pet_should_return_success_msg(self, graphql_client, client):
        client.post("/rest/pets", json={
            "name": "Rafaelis",
            "age": 34,
            "isPlayful": False
        })

        result = graphql_client.execute("""
        mutation {
            deletePet(petId:"1"){
                pet{
                    name
                    age
                    isPlayful
                },
                ok
            }

        }
        """)

        assert result["data"]["deletePet"]["ok"] is True
