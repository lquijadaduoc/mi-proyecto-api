from pathlib import Path

from flask import Flask, jsonify

app = Flask(__name__)


def get_version():
    version_file = Path("VERSION.txt")
    if version_file.exists():
        return version_file.read_text(encoding="utf-8").strip()
    return "sin-version"


@app.get("/health")
def health():
    return jsonify({"status": "ok", "version": get_version()})


@app.get("/tasks")
def tasks():
    return jsonify([
        {"id": 1, "title": "Validar CI/CD"},
        {"id": 2, "title": "Probar Docker"},
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
