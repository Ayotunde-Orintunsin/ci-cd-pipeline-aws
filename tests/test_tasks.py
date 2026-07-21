def test_create_and_get_task(client):
    create_resp = client.post("/tasks", json={"title": "Write tests"})
    assert create_resp.status_code == 201
    task = create_resp.json()
    assert task["title"] == "Write tests"
    assert task["status"] == "todo"

    task_id = task["id"]
    get_resp = client.get(f"/tasks/{task_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == task_id

def test_list_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_task_status(client):
    create_resp = client.post("/tasks", json={"title": "Temp task"})
    task_id = create_resp.json()["id"]

    update_resp = client.patch(f"/tasks/{task_id}", json={"status": "done"})
    assert update_resp.status_code == 200
    assert update_resp.json()["status"] == "done"

def test_delete_task(client):
    create_resp = client.post("/tasks", json={"title": "Delete me"})
    task_id = create_resp.json()["id"]

    delete_resp = client.delete(f"/tasks/{task_id}")
    assert delete_resp.status_code == 204

    get_resp = client.get(f"/tasks/{task_id}")
    assert get_resp.status_code == 404
