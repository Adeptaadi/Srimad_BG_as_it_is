# 🕉️ Srimad Bhagavad Gita – Shlok App

A full-stack web application that presents verses from the **Srimad Bhagavad Gita As It Is**, including Sanskrit text, word-by-word synonyms, English translation, and Śrīla Prabhupāda’s purports.  
The app serves a random shlok on each request and is designed for educational and devotional use.

---

## 🌐 Live Links

- **Web App (Frontend)**  
  https://srimad-bhagavad-gita-as-it-is.netlify.app/

- **REST API (Backend)**  
  https://srimad-bg-api.onrender.com/api/shlok/random

---

## ✨ Features

- 📜 Random Bhagavad Gita shlok on each request
- 🕉️ Unicode-safe Sanskrit rendering
- 📖 Word-by-word synonyms
- 🌍 English translation
- 🧠 Scrollable Śrīla Prabhupāda purports
- 🔁 “New Shlok” button for instant refresh
- 🌐 Clean REST API design
- 📱 Responsive and minimal UI

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- Flask-CORS
- Gunicorn
- JSON-based data storage

### Frontend
- HTML5
- CSS3
- Vanilla JavaScript

### Deployment
- **Backend**: Render
- **Frontend**: Netlify
- **Version Control**: Git & GitHub

---

## 📂 Project Structure

Srimad_BG_as_it_is/
│
├── Backend/
│ ├── app.py # Flask API
│ ├── gita_db.json # Bhagavad Gita shlok database
│ └── requirements.txt # Python dependencies
│
├── Frontend/
│ └── index.html # Frontend UI
│
└── README.md


---

## 🔌 API Endpoints

### Health Check


GET /


### Random Shlok


GET /api/shlok/random


### Get Shlok by Chapter & Verse


GET /api/shlok/<chapter>/<verse>


Example:


/api/shlok/1/1


---

## ⚠️ Notes

- The backend is hosted on **Render free tier**.  
  The service may **sleep during inactivity**, causing the first request to take up to ~50 seconds.
- All texts are served with **UTF-8 encoding** to preserve Sanskrit characters.
- Data is stored locally in JSON for simplicity and reliability.

---

## 🎯 Future Improvements

- Daily shlok recommendation mode
- Copy / share shlok feature
- Search by keyword or chapter
- Dark mode
- Bookmark favorite verses

---

## 📜 Disclaimer

This project is intended **strictly for educational and non-commercial purposes**.  
All spiritual content is sourced from *Bhagavad Gītā As It Is* by **A. C. Bhaktivedanta Swami Prabhupāda**.

---

## 👤 Author

**Aditya Rana**  
Computer Science (AI) Undergraduate  