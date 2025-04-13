
# 💬 Financial ChatBot 💰

A Python-based Financial ChatBot built using **Google Generative AI** and **Streamlit**. This chatbot answers user queries related to finance, helping users with topics like budgeting, investments, and personal finance management.

## 🚀 Features
- ✅ **Finance-related Insights** powered by Google Generative AI
- ✅ **Real-Time Responses**: Instant answers generated via Google Generative AI
- ✅ **Responsive Web Interface**: Hosted using **Streamlit**, providing a smooth and user-friendly experience on all devices.

## 🛠 Tech Stack
- **Backend**: Google Generative AI
- **Frontend**: Streamlit
- **Language**: Python

## 📂 Setup & Installation

### 1️⃣ Clone the Repository
Run the following command to clone the project:

```bash
git clone https://github.com/ayush-r-nair/Financial-ChatBot.git
cd Financial-ChatBot
```

### 2️⃣ Create & Activate Virtual Environment (Optional but Recommended)

#### For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
Make sure you have `requirements.txt` in the project folder and install dependencies:

```bash
pip install -r requirements.txt
```

### 4️⃣ Set up Google Generative AI API Key
To interact with Google's Generative AI, you need to set up your API key:

```bash
export GOOGLE_API_KEY=your_api_key_here
```

### 5️⃣ Run the Streamlit App
Launch the chatbot application:

```bash
streamlit run app.py
```

### 6️⃣ Open in Browser
After running the app, open it in your browser:

```bash
http://127.0.0.1:8501
```

## 📜 Requirements
This project requires:

- Python 3.x
- Streamlit 1.14+
- google-generativeai (for generating AI responses)

All dependencies are listed in `requirements.txt`. To install them, run:

```bash
pip install -r requirements.txt
```

## 📂 File Structure
Financial-ChatBot/
│── app.py                    # Main Streamlit application
│── requirements.txt           # Required dependencies
│── README.md                 # Documentation
│── .env                      # Environment variables (for Google API key)
