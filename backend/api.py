from fastapi import FastAPI
import update
import schedule
import structures

app = FastAPI()

@app.get("/schedule/")
def return_best_times(dayString, levelString, timeString):
    return schedule.get_best_times(dayString, levelString, timeString)


@app.get("/update/api_to_json")
def print_api():
    return update.api_to_json()


@app.get("/update/update_structure")
def print_api():
    return update.update_structure()


@app.get("/update/get_weeks")
def print_api():
    return update.get_weeks()

@app.get("/schedule/get_intervals_avgs")
def print_api():
    return schedule.get_intervals_avgs(structures.level3_week, "Sunday", [["15:00", "15:30", "16:00"]])

@app.get("/schedule/get_best_interval")
def print_api():
    return schedule.get_best_interval([["15:00", "15:30", "16:00"]], [[27, 0, 0]])

@app.get("/schedule.py/get_best_times/day/{day}/level/{level}/timeString/{timeString}")
def print_api(day: str, level: str, timeString: str ):
    return schedule.get_best_times(day, level, timeString)

