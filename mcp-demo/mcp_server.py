# mcp_server.py
import httpx
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Iris Classifier", log_level="WARNING")


@mcp.tool()
def classify_iris(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float) -> str:
    """Classify an iris flower from its four measurements, in centimeters.
    Returns the predicted species: setosa, versicolor, or virginica.
    """
    response = httpx.post(
        "http://127.0.0.1:8000/predict",
        json={
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width,
        },
    )
    return f"Predicted species: {response.json()['species']}"


@mcp.tool()
def iris_probabilities(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float) -> str:
    """Get the model's confidence for each iris species from four measurements, in centimeters.
    Returns a probability (0 to 1) for setosa, versicolor, and virginica.
    Use this instead of classify_iris when the user asks how sure the model is,
    wants to compare species, or the flower might be borderline between two species.
    Use classify_iris when the user just wants a single answer.
    """
    response = httpx.post(
        "http://127.0.0.1:8000/probabilities",
        json={
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width,
        },
    )
    probs = response.json()
    return "Probabilities: " + ", ".join(f"{s} {p:.0%}" for s, p in probs.items())


if __name__ == "__main__":
    mcp.run()
