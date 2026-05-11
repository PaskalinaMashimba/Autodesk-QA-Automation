import requests

class SimulationAPI:
    def __init__(self):
        # Using a public placeholder API to simulate a backend engine
        self.base_url = "https://jsonplaceholder.typicode.com/posts"

    def check_engine_status(self):
        """Simulates checking the health of a 3D rendering engine."""
        try:
            response = requests.get(f"{self.base_url}/1", timeout=5)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False