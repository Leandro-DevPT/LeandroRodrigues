import os
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename.endswith(".csv"):
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            # Processamento básico com Pandas
            df = pd.read_csv(filepath)
            resumo = {
                "linhas": len(df),
                "colunas": len(df.columns),
                "colunas_numericas": list(df.select_dtypes(include="number").columns),
                "media_por_coluna": df.mean(numeric_only=True).to_dict()
            }

            result = resumo

    return render_template("templates/index1.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
