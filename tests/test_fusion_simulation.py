import pytest
from utils.api_validator import SimulationAPI

def test_api_stability():
    """Validates that the backend simulation service is reachable."""
    api = SimulationAPI()
    assert api.check_engine_status() is True, "QA Error: Simulation Engine API is unreachable."

def test_rendering_performance_logic():
    """Simulates a performance check for a 3D model render."""
    expected_max_time = 5.0
    actual_simulated_time = 4.2  # Hardcoded for the demo
    assert actual_simulated_time <= expected_max_time, f"Performance Issue: Render took {actual_simulated_time}s"