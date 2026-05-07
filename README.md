# Eye Blink Detection Using Deep Learning for Eye Safety
## 📌 Overview
**Eye Blink Detection Using Deep Learning** is a workplace wellness tool designed to protect the eye health of digital workers.  
By monitoring blink rates during short, randomized 1-minute intervals, the system detects reduced blinking — a common cause of eye strain, dryness, and discomfort.
This project aligns with **UNITED NATIONS Sustainable Development Goal 3: Good Health and Well-being** by promoting preventive eye care in the workplace.
---
## 🎯 Problem Statement
Employees who spend long hours in front of computer screens often forget to blink at a healthy rate, leading to:
- Eye irritation
- Digital eye strain
- Headaches
- Potential long-term vision issues
---
## 💡 Solution
Our **MobileNetV2-based deep learning model**:
- Randomly monitors employees for 1-minute intervals (no full-day tracking)
- Counts blinks to assess eye health
- Generates **daily/weekly eye health reports**
- Runs over the organization’s **LAN server** to maintain privacy
---
## ✨ Features
- 🖥 **Short Random Monitoring** – Only 1 min at random times
- 📊 **Eye Blink Reports** – Daily or weekly
- 🔒 **Privacy-Friendly** – No continuous recording
- ⚡ **Lightweight Model** – Based on MobileNetV2
- 🌍 **Workplace Health Support** – Aligns with UN SDG 3
---
## 🛠 Tech Stack
- **Frontend:** N/A (Backend-based system)
- **Backend/ML:** TensorFlow, Keras, Python
- **Model:** MobileNetV2
- **Data Processing:** ImageDataGenerator
- **Deployment:** LAN Server Integration
---
## 📂 Project Structure
eye-blink-detection/
│-- dataset/
│-- model/
│-- scripts/
│ └── train_model.py
│-- requirements.txt
│-- README.md

yaml
Copy
Edit

---

## 🚀 Installation
```bash
# Clone the repository
git clone https://github.com/SaravanavelE/eye_blink_detection_using_deep_learning.git

# Navigate to the project folder
cd eye-blink-detection

# Install dependencies
pip install -r requirements.txt

# Train the model
python scripts/train_model.py
```
---
📌 Future Scope
📱 Mobile application integration
☁ Cloud deployment for multi-office tracking
👁 Real-time feedback and alerts
🧠 Integration with medical AI for early diagnosis
---

📧 Contact
Email: saravanavel.e.ai@gmail.com
LinkedIn: saravanavel-e
GitHub: SaravanavelE
