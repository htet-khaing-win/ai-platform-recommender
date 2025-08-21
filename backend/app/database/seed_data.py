from . import SessionLocal, initdb
from . models import Tool, WorkflowStep, Workflow

def seed():
    initdb() # to ensure the table exists
    db = SessionLocal()

    #clear old data
    # db.query(Workflow).delete()
    # db.query(WorkflowStep).delete()
    # db.query(Tool).delete()


    #------------list of Tools----------------

    tool1 = Tool(
        name = "Chatgpt",
        description = "AI chat bot that can generate text, answer queries and assist with tasks",
        category = "Text Generation",
        pricing = "Freemium",
        website = "www.chatgpt.com"
    )

    tool2 = Tool(
        name = "Claude",
        description = "AI powered agent that can generate code, answer queries and assist with tasks",
        category = "Coding",
        pricing = "Freemium",
        website = "www.claude.com"
    )

    tool3 = Tool(
        name = "Grammarly",
        description = "AI powered grammar and writing assistant",
        category = "Writing",
        pricing = "Freemium",
        website = "www.grammarly.com"
    )

    tool4 = Tool(
        name = "Mid Journey",
        description = "AI powered Image generation platform",
        category = "Design",
        pricing = "Freemium",
        website = "www.midjourney.com"
    )

    db.add_all([tool1,tool2,tool3,tool4])
    db.commit

    #------------list of work flows--------------

    Workflow1 = Workflow(
        name="Research Paper Writing",
        description="Step-by-step process for writing a research paper with AI tools.",
        trigger_keywords="research, paper, academic, thesis"
    )

    Workflow2 = Workflow(
        name="School Presentation",
        description="Create a school presentation using AI tools.",
        trigger_keywords="presentation, pitch deck, academic"
    )

    db.add_all([Workflow1,Workflow2])
    db.commit()

    #--------Workflow Steps-----------------
    steps = [
        WorkflowStep(
            workflow_id = Workflow1.id,
            step_number = 1,
            tool_id = tool1.id,
            action_description = "Use ChatGPT to generate an outline for your research paper."
        ),
        WorkflowStep(
            workflow_id = Workflow1.id,
            step_number = 2,
            tool_id = tool3.id,
            action_description = "Use Grammarly to proofread and correct grammar in your draft."
        ),
        WorkflowStep(
            workflow_id = Workflow1.id,
            step_number = 3,
            tool_id = tool1.id,
            action_description = "Use ChatGPT to generate key talking points for your presentation."
        ),
        WorkflowStep(
            workflow_id = Workflow1.id,
            step_number = 4,
            tool_id = tool4.id,
            action_description = "Use Midjourney to generate images to use in your presentation."
        )
    ]

    db.add_all(steps)
    db.commit()
    db.close()
    print("Database is seeded successfully!")

if __name__ == "__main__":
    seed()
    print("Database seeded")

