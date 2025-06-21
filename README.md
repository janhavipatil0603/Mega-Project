
# Aadhaar-Based Disaster Relief Management System 🚨🇮🇳

A secure, face-recognition-powered disaster relief system built using **Streamlit**, **OpenCV**, and **Twilio**, designed for fair and efficient distribution of relief resources to citizens based on their **Aadhaar ID** and verified face identity.

---

## 🌟 Features

- 🎯 **Multi-role Login**: Distributor, Admin, and User (Feedback)
- 🧑‍💻 **Admin Dashboard**: Allocation log, scam detection, feedback analysis
- 👤 **Face Recognition**: LBPH model for admins and beneficiaries
- 📲 **Twilio SMS Alerts**: On duplicate allocations or summary exports
- 📊 **Visual Reports**: Feedback analytics via pie charts
- ✅ **One-time Allocation & Feedback Submission**
- 💡 **Scam Detection**: Compares allocations vs. feedback for suspicious activity

---

## 📁 Project Structure

```bash
📦 disaster-relief-app/
├── aadhar_relief_management.py      # Main Streamlit App
├── requirements.txt                 # Required Python packages
├── admins.csv                       # Admin login credentials
├── aadhaar_data.csv                 # Aadhaar ID + Name database
├── allocation_log.csv               # Allocation history
├── user_feedback.csv                # Feedback from users
├── admin_model.yml                  # Trained model for admin face recognition
├── ben_model.yml                    # Trained model for beneficiary face recognition
├── admin_label_map.npy              # Admin label mapping
├── ben_label_map.npy                # Beneficiary label mapping
├── admin_faces/                     # Admin face images (JPGs)
├── faces_db/                        # Beneficiary face images (JPGs)
└── assets/
    ├── home_bg.jpg
    ├── admin_bg.jpg
    ├── distributor_bg.jpg
    └── user_bg.jpg
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.8+
- Webcam (for local testing)
- GitHub account (for deployment)
- Twilio account (for SMS alerts)

---

### 📦 Installation

1. **Clone this repository**
```bash
git clone https://github.com/yourusername/disaster-relief-app.git
cd disaster-relief-app
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the app**
```bash
streamlit run aadhar_relief_management.py
```

4. Open in browser:  
`http://localhost:8501`

---

## 🔐 Twilio Configuration

Add your Twilio credentials in `aadhar_relief_management.py`:

```python
TWILIO_SID = 'your_twilio_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_FROM = '+1XXXXXXXXXX'
ADMIN_PHONE = '+91XXXXXXXXXX'
```

> 💡 Consider securing these using `.env` or `st.secrets`.

---

## 🌐 Deploy on Streamlit Cloud

> Streamlit Cloud doesn’t support `cv2.VideoCapture()`. Replace it with `st.file_uploader()` or `st.camera_input()` for deployment.

1. Push your code to GitHub
2. Add `requirements.txt`
3. Go to https://streamlit.io/cloud
4. Select your repo and deploy

---

## 📊 Feedback and Scam Detection Logic

- Compares user feedback to allocated resources
- Flags **Clean**, **Suspicious**, and **No Feedback**
- Visual summary shown in pie chart (positive vs. negative)

---

## 📸 Face Recognition

- Uses OpenCV’s **LBPH recognizer**
- Stores `.jpg` face images in:
  - `admin_faces/username.jpg`
  - `faces_db/aadhaar_id.jpg`
- Trains model on launch and uses it to verify face

---

## 💡 Future Improvements

- ✅ Replace webcam with upload for cloud support
- 📱 Convert into a mobile app (Kivy or WebView)
- 🔒 Encrypt Aadhaar and sensitive data
- 🧠 Add AI-based fraud scoring
- 📍 Location tagging with GPS

---

## 📜 License

This project is intended for research, academic, and humanitarian use only. Please credit the original author if reused or modified.

---

## 🤝 Author
**Janhavi Patil**
**Prerna Jadhav**
**Riya Desai**
**Utkarsha Velhal**
**Ganesh Kakde**  
Built using: Streamlit, OpenCV, Twilio  
For queries or contributions, please open an issue or pull request.
