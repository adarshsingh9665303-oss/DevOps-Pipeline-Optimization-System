import json

DB_FILE = "app/database.json"


def read_data():
    with open(DB_FILE, "r") as file:
        return json.load(file)


def write_data(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)


def create_pipeline(pipeline):
    data = read_data()
    data["pipelines"].append(pipeline)
    write_data(data)


def get_all_pipelines():
    return read_data()["pipelines"]


def update_pipeline(pipeline_id, updated_data):
    data = read_data()
    for pipeline in data["pipelines"]:
        if pipeline["id"] == pipeline_id:
            pipeline.update(updated_data)
            write_data(data)
            return pipeline
    return None


def delete_pipeline(pipeline_id):
    data = read_data()
    data["pipelines"] = [
        p for p in data["pipelines"] if p["id"] != pipeline_id
    ]
    write_data(data)
