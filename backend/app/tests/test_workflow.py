# backend/app/tests/test_workflow.py

import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_generate_workflow_match():
    response = client.post("/v1/workflow/generate", json={"goal": "fastapi"})
    assert response.status_code == 200

    data = response.json()
    # Change this based on actual response structure
    assert data["name"] == "Deploy an API"  # probably "name" not "workflow_name"
    assert len(data["steps"]) == 3
    assert data["steps"][0]["action_description"] == "Create FastAPI application"


def test_generate_workflow_no_match():
    response = client.post("/v1/workflow/generate", json={"goal": "blockchain"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Couldn't find the matching workflow"  # Updated message
