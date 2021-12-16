from pathlib import Path
from process import process_file

if __name__ == '__main__':
    models = Path("models")
    Path("output").mkdir(exist_ok=True)
    for model in models.glob("**/*.obj"):
        process_file(str(model))
