# from fastapi.testclient import TestClient
# from backend.app.main import app

# client = TestClient(app)

# def test_generate_workflow_match():
#     response = client.post("/v1/workflow/generate", json={"goal": "fastapi"})
#     assert response.status_code == 200
#     data = response.json()
#     assert "steps" in data
#     assert len(data["steps"]) > 0
#     assert "action_description" in data["steps"][0]

# def test_generate_workflow_no_match():
#     response = client.post("/v1/workflow/generate", json={"goal": "blockchain"})
#     assert response.status_code == 404
#     assert response.json()["detail"] == "Couldn't find the matching workflow"
