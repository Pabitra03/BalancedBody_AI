# Fitness AI

Fitness AI is an intelligent biological optimization system that analyzes your precise biological metrics — Age, Gender, Weight, Height, and Activity Level — to build personalized diet and fitness protocols.

## 🚀 Features

- **Personalized Diet**: Exact daily macro break-downs of breakfast, lunch, and dinner mapped to your caloric goal.
- **Workout Plans**: Calculated metabolic routines built to burn fat or build muscle based on your capabilities.
- **Progress Tracking**: Visual charts and history curves ensuring your biometrics trend correctly.
- **AI Health Insights**: Automated calculations for BMI, BMR, and TDEE based on continuous profile analysis.

## 🛠️ Tech Stack

- **Frontend**: HTML5, Tailwind CSS, JavaScript (Vanilla), Feather Icons, Chart.js.
- **Backend**: Python (Flask), MySQL.
- **Deployment**: Configured for Vercel.

## 📦 Setup & Installation

### Prerequisites
- Python 3.8+
- MySQL Server

### Backend Setup
1. Navigate to the `backend` directory.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/python  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file based on the template and provide your MySQL credentials.
5. Run the server:
   ```bash
   python app.py
   ```

### Frontend Setup
1. Simply open `frontend/index.html` in your browser or serve it using a local static file server.
2. Ensure the `API_BASE_URL` in `frontend/js/app.js` points to your running backend.
