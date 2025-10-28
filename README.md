🧠 DeepFace Emotion Detection App
😊 Detect emotions from facial expressions using AI — powered by DeepFace & Streamlit.
📸 Overview

The DeepFace Emotion Detection App is an AI-based web application built using Streamlit and DeepFace, allowing users to detect emotions from images or live webcam input.
The app utilizes state-of-the-art deep learning models to classify facial emotions such as Happy, Sad, Angry, Surprise, Fear, Disgust, and Neutral.

It provides an interactive and visually appealing interface where users can upload a photo or capture one in real-time using their webcam, and instantly view the detected emotion with a confidence chart.

🌟 Key Features

📂 Image Upload Mode – Upload any face image for instant emotion detection

🎥 Webcam Mode – Capture your image in real-time directly from your camera

💡 Deep Learning Model – Uses DeepFace pre-trained models under the hood

📊 Confidence Visualization – Displays a bar chart showing confidence scores for all emotions

🎨 Modern UI – Clean, responsive Streamlit interface with styled emotion results

⚙️ Error Handling – Gracefully handles missing faces or unsupported images

🧩 Fully Deployable – Works both locally and on Streamlit Cloud

🧰 Tech Stack
Category	Technologies
Frontend / UI	Streamlit
Backend / ML	DeepFace, TensorFlow, Keras
Image Processing	OpenCV, Pillow
Visualization	Streamlit built-in charts
Language	Python 3.10+
🏗️ Project Structure
emotion-detection-ai/
│
├── app.py                # Main Streamlit application file
├── requirements.txt      # Dependencies for easy installation
├── README.md             # Project documentation (this file)
└── venv/ (optional)      # Virtual environment (not uploaded to GitHub)

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/Snehith1302/emotion-detection-ai.git
cd emotion-detection-ai

2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate       # For Windows
# OR
source venv/bin/activate    # For Mac/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the app
streamlit run app.py


Your app will start locally at:
👉 http://localhost:8501

☁️ Deployment on Streamlit Cloud

Push your code to a public GitHub repository.

Go to https://share.streamlit.io
.

Sign in and click “New App”.

Connect your GitHub repo and select your app.py file.

Click Deploy.

You’ll get a live URL like:
https://<your-username>-emotion-detection-ai.streamlit.app

🧪 Example Output
✅ Detected Emotion:

Happy 😄
Confidence: 96.4%

📊 Emotion Chart:
Emotion	Confidence (%)
Happy	96.4
Neutral	2.1
Surprise	1.5
🧩 Troubleshooting
Issue	Solution
Face could not be detected	Try a clearer image or ensure your face is visible and well-lit.
No module named DeepFace	Run pip install deepface
Streamlit not found	Run pip install streamlit
Webcam not showing	Use Chrome browser and allow camera access.
👨‍💻 Author

Anuka Snehith Reddy
💻 GitHub: https://github.com/Snehith1302

📜 License


This project is open-source and available under the MIT License.
