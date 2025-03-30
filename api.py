from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is working!"}

@app.get("/api/rover-data")
def get_rover_data():
    return {"rover_data": "Sample Data"}


import random
import time

app = FastAPI()

def generate_sensor_data():
    """Simulates rover sensor data"""
    return {
        "timestamp": time.time(),
        "rover_id": f"Rover-{random.randint(100, 999)}",
        "soil_moisture": round(random.uniform(20, 80), 2),
        "soil_pH": round(random.uniform(5.5, 7.5), 2),
        "temperature": round(random.uniform(10, 40), 2),
        "battery_level": round(random.uniform(10, 100), 2)
    }

@app.get("/api/rover-data")
def get_rover_data():
    return generate_sensor_data()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
