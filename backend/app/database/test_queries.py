# from . import SessionLocal
# from .models import Workflow

# def test_query():
#     db = SessionLocal()

#     Workflows = db.query(Workflow).all()
#     for wf in Workflows:
#         print(f"\n Workflow: {wf.name}")
#         print(f"\n Description: {wf.description}")
#         print(f"\n Keywords: {wf.trigger_keywords}")

#         for step in wf.steps:
#             print(f"\n Step {step.step_number} : {step.action_description}")
#             print(f"\n Tool {step.tool.name} ({step.tool.website})")

#     db.close()

# if __name__ == "__main__":
#     test_query()
