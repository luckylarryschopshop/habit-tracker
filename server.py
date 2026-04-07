from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import json
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

HABITS_FILE = "habits.json"

if not os.path.exists(HABITS_FILE):
    with open(HABITS_FILE, "w") as f:
        json.dump([], f)

def load_habits():
    with open(HABITS_FILE, "r") as f:
        return json.load(f)

def save_habits(habits):
    with open(HABITS_FILE, "w") as f:
        json.dump(habits, f)

@app.get("/api/habits", response_model=list)
def get_habits():
    return load_habits()

@app.post("/api/habits", response_model=dict)
def create_habit(name: str):
    habits = load_habits()
    habit = {"id": len(habits), "name": name, "streaks": []}
    habits.append(habit)
    save_habits(habits)
    return habit

@app.post("/api/habits/{id}/complete")
def complete_habit(id: int):
    habits = load_habits()
    for habit in habits:
        if habit["id"] == id:
            habit["streaks"].append({"date": "today", "completed": True})
            save_habits(habits)
            return {"message": "Marked as complete"}
    raise HTTPException(status_code=404, detail="Habit not found")

@app.get("/api/habits/{id}/streaks")
def get_streaks(id: int):
    habits = load_habits()
    for habit in habits:
        if habit["id"] == id:
            return {"streaks": habit["streaks"]}
    raise HTTPException(status_code=404, detail="Habit not found")

@app.get("/", response_class=HTMLResponse)
def read_index():
    with open("static/index.html", "r") as f:
        return f.read()