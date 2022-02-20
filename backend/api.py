from fastapi import FastAPI
import update
import schedule

app = FastAPI()


@app.get("/update.py/api_to_json")
def print_api():
    return update.api_to_json()

@app.get("/update.py/update_structure")
def print_api():
    return update.update_structure()

@app.get("/update.py/get_weeks")
def print_api():
    return update.get_weeks()

@app.get("/schedule.py/parseUserData")
def print_api():
    return schedule.parseUserData("sunday 12:30PM-04:30PM,07:30PM-10:30PM")