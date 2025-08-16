from . import SessionLocal, initdb
from .models import Tool, Workflow, WorkflowStep

def seed_data():
    db = SessionLocal()

    #clearing old queries

    db.query(Tool).delete()
    db.query(Workflow).delete()
    db.query(WorkflowStep).delete()


    #----TOOLS--------
    docker_tool = Tool(
        name = "Docker",
        description = "Containerization platform to package applications",
        website = "https://www.docker.com",
        category = "Dev",
        pricing = "Free"
    )

    fastapi_tool = Tool(
        name = "Fast API",
        description = "Modern Python web framework for building APIs",
        website = "https://fastapi.tiangolo.com",
        category = "Dev",
        pricing = "Free"
    )

    sqlite_tool = Tool(
        name = "Sqlite3",
        description = "Lightweight SQL database",
        website = "https://www.sqlite.org",
        category = "Dev",
        pricing = "Free"
    )

    db.add_all([docker_tool,fastapi_tool,sqlite_tool])
    db.commit()

    #workflows

    deploy_api_workflow = Workflow(
        name = "Deploy an API",
        description = "Steps to containerize and deploy a FastAPI application",
        trigger_keywords = "deploy api, fastapi, docker"
    )

    db.add(deploy_api_workflow)
    db.commit()

    #workflowsteps

    steps = [
        WorkflowStep(
            workflow_id = deploy_api_workflow.id,
            step_number = 1,
            action_description = "Create FastAPI application",
            tool_id = fastapi_tool.id
        ),
        WorkflowStep(
            workflow_id = deploy_api_workflow.id,
            step_number = 2,
            action_description = "Use SQLite for data storage",
            tool_id = sqlite_tool.id
        ),
        WorkflowStep(
            workflow_id = deploy_api_workflow.id,
            step_number = 3,
            action_description = "Containerize application using Docker",
            tool_id = docker_tool.id

        )

    ]

    db.add_all(steps)
    db.commit()
    db.close()

if __name__ == "__main__":
    initdb()
    seed_data()
    print ("Sample Data is seeded successfully")
else:
    print("Something went wrong")