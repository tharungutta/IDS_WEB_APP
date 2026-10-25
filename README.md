# 🛡️ Intrusion Detection System (IDS) Web App

A web-based **Intrusion Detection System (IDS)** built with Python and Flask. The application allows users to upload a CSV file containing network-traffic records, analyze the data with a trained machine-learning model, and view prediction results through a web interface.

🔗 **Repository:** https://github.com/tharungutta/IDS_WEB_APP

---

## 📌 Project Overview

Network traffic can contain both normal activity and suspicious patterns. Manually reviewing large traffic datasets can be time-consuming, so this project provides a web interface for submitting traffic data to a trained model and displaying its predictions.

The application connects a Flask backend, a saved machine-learning model, and a browser-based interface. It is intended as an educational project demonstrating how machine learning can be integrated into a web application for network-traffic analysis.

## ✨ Features

- **CSV upload:** Submit a CSV file containing network-traffic records for analysis.
- **Machine-learning predictions:** Process uploaded records using the saved model.
- **Results display:** Present prediction results in the web interface.
- **Data visualization:** View visual summaries of the analysis where supported by the application.
- **Browser-based workflow:** Use the application through a web interface instead of running predictions manually from a notebook.

> **Note:** Predictions depend on the model, training data, and the features supplied in the uploaded CSV. This project should be treated as a learning/demo tool, not as a replacement for a production network-security system.

## 🧰 Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| Web framework | Flask |
| Machine learning | Trained model loaded from `ids_model.joblib` |
| Data input | CSV files |
| Data processing and visualization | Python libraries used by the project |

## 🔄 How It Works

1. **Upload traffic data** — The user selects a CSV file containing network-traffic records.
2. **Read and prepare the data** — The Flask application loads the uploaded data and prepares its features for inference.
3. **Run model inference** — The saved machine-learning model processes the prepared records.
4. **Display results** — The application presents the prediction output and available visualizations.

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/tharungutta/IDS_WEB_APP.git
cd IDS_WEB_APP
```

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

If the repository contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If it does not, install the packages listed or imported by the project code. Flask, pandas, and the model's required machine-learning library may be needed, depending on the implementation.

### 4. Start the application

Run the Flask entry-point file used by the repository (for example, `app.py`):

```bash
python app.py
```

Open the local URL printed in the terminal, commonly `http://127.0.0.1:5000`, if that is the address configured by the application.

## 📄 Input Data Notes

- Upload a CSV file with the columns expected by the model.
- Column names, feature order, and data types must match the model's training/inference requirements.
- If the application reports missing features (for example, `duration`), use a dataset that matches the expected schema or update the preprocessing logic consistently with the model.
- Do not upload sensitive or confidential network logs to a publicly accessible deployment.

## ⚠️ Limitations

- Model quality depends on the training dataset and evaluation process.
- Results are model predictions, not a guarantee that traffic is safe or malicious.
- CSV-based analysis is not necessarily real-time packet monitoring.
- A model trained with a fixed feature schema may reject datasets with missing, extra, or incompatible columns.
- This project is intended for demonstration and learning. Do not rely on it alone to protect a live network.

## 🔮 Possible Future Improvements

- Add sample CSV files and clearer input validation.
- Display model evaluation metrics and a confusion matrix.
- Improve error messages for missing or incorrectly formatted columns.
- Add downloadable reports of prediction results.
- Add authentication and deployment hardening before exposing the application publicly.

## 👨‍💻 Author

**Tharun Gutta**

- GitHub: https://github.com/tharungutta
- Project repository: https://github.com/tharungutta/IDS_WEB_APP

---

⭐ If you find this project useful, feel free to explore the source code and share feedback.
