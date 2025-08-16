from . import SessionLocal, initdb
from . import crud, schemas

#create tables

initdb()

#Open session

db = SessionLocal()

#create

platform_data = schemas.PlatformCreate(
    name = "Grok",
    description = "This is for the test description",
    category = "Chatbot",
    website = "https://grok.com/"
)

new_platform = crud.create_platform(db, platform_data)
print(f"Created: {new_platform}")

#read

all_platforms = crud.get_platforms(db)
print("here are all platforms:", all_platforms)

#update

update_data = schemas.PlatformUpdate(description="Description just got updated")
updated_platform = crud.update_platform(db, new_platform.id, update_data)
print("Successfuly Updated:", updated_platform)

#delete

deleted = crud.delete_platform(db, new_platform.id)
print("Successfully Deleted", deleted)