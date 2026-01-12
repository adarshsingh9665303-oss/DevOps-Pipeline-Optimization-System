from fastapi import FastAPI, HTTPException
from app.models import Pipeline
from app import crud

app = FastAPI(title="DevOps Pipeline Optimization System")


@app.post("/pipelines")
def create_pipeline(pipeline: Pipeline):
    crud.create_pipeline(pipeline.dict())
    return {"message": "Pipeline created successfully"}


@app.get("/pipelines")
def read_pipelines():
    return crud.get_all_pipelines()


@app.put("/pipelines/{pipeline_id}")
def update_pipeline(pipeline_id: int, pipeline: Pipeline):
    result = crud.update_pipeline(pipeline_id, pipeline.dict())
    if not result:
        raise HTTPException(status_code=404, detail="Pipeline not found")
    return result


@app.delete("/pipelines/{pipeline_id}")
def delete_pipeline(pipeline_id: int):
    crud.delete_pipeline(pipeline_id)
    return {"message": "Pipeline deleted successfully"}
