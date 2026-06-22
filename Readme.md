## 📸 Face Recognition Login System (Django + DeepFace)
```
A simple facial recognition system using **Django + DeepFace + OpenCV**.
```

---

## ⚙️ Requirements
```
- Python 3.10 (IMPORTANT ❗)
- Windows 10/11
- Webcam
```

---

## 🔍 Check Python Version
```bash
py -0
```
### Note: Must be Python 3.10

---

## Create Or Switch Virtual Environment
```Bash
py -3.10  -m venv venv
```

---

## Activate Environment (Windows)
```Bash
venv\Scripts\activate
```

---

## Install Required Libraries
```Bash
pip install django deepface numpy
```
---

```Bash
pip install opencv-python==4.9.0.80
```

---

## 🧠 Install TensorFlow (IMPORTANT for DeepFace)
```Bash
pip install tensorflow==2.15.0
```

---

## 🧠 Install Keras (optional but safe)
```Bash
pip install keras==2.15.0
pip install tf-keras
```

---

## 🚀 Create Django Project
```Bash
django-admin startproject config .
```

---

## 📌 Create App
```Bash
python manage.py startapp users
```

---

## ⚙️ Add App to Django
```
INSTALLED_APPS = [
    ...
    'users',
]
```

---

## ▶️ Run Server
```
python manage.py runserver
```

---

## 📸 Face Recognition Flow
```
👤 Register Face
• Capture multiple images using webcam
• Save in:
```
```
media/faces/username/
```

---

## 🔐 Login Face
```
• Capture image
• Compare using DeepFace
• Return match result
```

---

## 🗑 Delete User
```
media/faces/username/
```

---

## Project Structure
```
face_login/
│
├── config/
├── users/
├── media/
│   └── faces/
├── venv/
└── manage.py
```

---

## ⚠️ Important Notes
```
✔ MUST use Python 3.10 (3.11/3.13 may break TensorFlow/DeepFace)
✔ Good lighting improves accuracy
✔ Webcam must be accessible
✔ First DeepFace run may be slow (model download)
```

---

## 🧠 Common Fixes
### ❌ TensorFlow error
```
pip install --upgrade pip
```

### ❌ OpenCV camera not opening
```
Check webcam permissions
```

### ❌ DeepFace slow first run
```
Normal (downloads AI models)
```

---

## 👤 1. REGISTER (Save Face)
```Open Browser
http://127.0.0.1:8000/users/register/?name=ricardo
```

---

### 📸 What happens:
```
1. Camera opens
2. You press:
    • S = save image
    • Q = quit
3. Images are saved here:

    media/faces/ricardo/
        0.jpg
        1.jpg
        2.jpg
```

### 🧠 Result:
```
User “ricardo” is now registered in the system.
````

---

## 🔐 2. LOGIN (Face Recognition)
```Open Browser
http://127.0.0.1:8000/users/login/
```
### 📸 What happens:
```
1. Camera opens
2. Takes 1 snapshot
3. Saves temporary image:
    • media/temp.jpg
4. DeepFace compares:
    • temp.jpg vs all saved faces
```

## 🧠 Result:
### If match found:
```JSON:
{
  "status": "success",
  "user": "ricardo"
}
```
### If no match:
```JSON
{
  "status": "failed"
}
```

---

## 🗑 3. DELETE USER (Remove Face Data)

``` Open Browser
http://127.0.0.1:8000/users/delete/?name=yourname
```
### 🧹 What happens:
```
Deletes folder:
    media/faces/ricardo/
```

## 🧠 Result:

### if deleted
``` JSON
{
  "status": "deleted",
  "user": "ricardo"
}
```

### If not found:
``` JSON
{
  "status": "not found"
}
```

## ⚙️ SIMPLE FLOW SUMMARY
```
👤 REGISTER → save face images in folder
🔐 LOGIN → compare camera face with saved faces
🗑 DELETE → remove user folder
```

---
## 
⚠️ IMPORTANT REMINDERS
### ✔ Always run server first:
``` Bash
```
### ✔ Always activate venv:
``` Bash
venv\Scripts\activate
```
### ✔ Use good lighting for face detection

---

## 🚀 Future Improvements
```
Real-time video recognition
Face embeddings (faster login)
Database instead of folders
Liveness detection (anti-photo spoofing)
HTML login UI
```

---

## 👨‍💻 Author
```
Name: Ricardo Jr Liera
Project: Face Recognition Login System
Stack: Django + DeepFace + OpenCV
Year: 2026
```
