
# Insurance Premium Predictor

Predict insurance premiums based on personal information such as age, sex, BMI, number of children, smoking habits, and region. This project uses a machine learning model deployed with FastAPI as the backend and Streamlit as the frontend.

---

## 🚀 Features

- Predict insurance premiums using user input
- Interactive web interface with Streamlit
- Backend API powered by FastAPI
- Model stored locally or can be loaded from cloud storage (S3)
- Ready for deployment using Docker, Render, or AWS

---

## 🛠 Technology Stack

- **Backend**: FastAPI  
- **Frontend**: Streamlit  
- **Machine Learning**: Python, scikit-learn  
- **Model Storage**: Pickle (`.pkl` file) or AWS S3  
- **Deployment**: Docker, AWS EC2, Render, or Streamlit Cloud  

---

## 📁 Project Structure

```

Insurance-Premium-Predictor/
│
├── main.py             # FastAPI backend entry point
├── frontend.py         # Streamlit frontend
├── requirements.txt    # Python dependencies
├── Dockerfile          # Optional Dockerfile for containerization
├── model/
│   └── Model.pkl       # Trained ML model
├── config/             # Configuration files (optional)
├── schema/             # Request/response schemas (optional)
└── **pycache**/        # Auto-generated Python cache

````

---

## ⚡ Installation

1. Clone the repository:
```bash
git clone https://github.com/hammadshah18/Insurance-Premium-Predictor.git
cd Insurance-Premium-Predictor
````

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🖥 Running the Project

### Backend (FastAPI):

```bash
uvicorn main:app --reload
```

* API endpoint: `http://127.0.0.1:8000/predict`

### Frontend (Streamlit):

```bash
streamlit run frontend.py
```

* Streamlit app opens in your browser
* Make sure the API URL in `frontend.py` points to your FastAPI endpoint

---

## 📦 Deployment

* **Backend**: Deploy on Render, Railway, or AWS EC2 using Docker
* **Frontend**: Deploy on Streamlit Cloud
* **Model Storage**: Keep locally in backend or use AWS S3

---

## 🧠 Usage

1. Open the Streamlit frontend
2. Enter user details: Age, Sex, BMI, Children, Smoker, Region
3. Click **Predict**
4. View predicted insurance premium

---

## 📈 Model

* Model: Machine learning regression model (Linear Regression / Decision Tree / Random Forest)
* Trained on historical insurance data
* Stored in `model/Model.pkl`

---

## 📄 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make changes and commit (`git commit -m "Description"`)
4. Push to branch (`git push origin feature-name`)
5. Create a Pull Request

---

## ⚖️ License

This project is licensed under the MIT License.

---

## 📞 Contact

* **Author**: Muhammad Hammad
* **Email**: 03042812430
* **GitHub**: [hammadshah18](https://github.com/hammadshah18)

---

```

---

If you want, I can also **create an enhanced version with screenshots, API examples, and deployment instructions** specifically for **free platforms** like Streamlit Cloud + Render. This will make your repo **LinkedIn-ready and professional**.  

Do you want me to do that next?
```
