from flask import Flask, render_template, request
import cv2
import mediapipe as mp
import math
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Mediapipe setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]
EAR_THRESHOLD = 0.25
CONSEC_FRAMES = 2

def euclidean_dist(p1, p2):
    return math.dist(p1, p2)

def eye_aspect_ratio(landmarks, eye_indices):
    eye = [landmarks[i] for i in eye_indices]
    A = euclidean_dist(eye[1], eye[5])
    B = euclidean_dist(eye[2], eye[4])
    C = euclidean_dist(eye[0], eye[3])
    return (A + B) / (2.0 * C)

def eye_health_analysis(blinks):
    if blinks < 10:
        return "⚠️ Low Blink Rate – Possible eye irritation, eye pain, dry eye."
    elif 10 <= blinks <= 20:
        return "✅ Normal Blink Rate – Eyes appear healthy."
    elif blinks > 25:
        return "⚠️ High Blink Rate – Possible watery eyes, fatigue, allergy."
    else:
        return "⚠️ Uncertain – Blink rate not interpretable."

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    blink_count = 0
    frame_counter = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(frame_rgb)

        if results.multi_face_landmarks:
            for landmarks in results.multi_face_landmarks:
                h, w, _ = frame.shape
                mesh_points = [(int(pt.x * w), int(pt.y * h)) for pt in landmarks.landmark]

                left_ear = eye_aspect_ratio(mesh_points, LEFT_EYE)
                right_ear = eye_aspect_ratio(mesh_points, RIGHT_EYE)
                avg_ear = (left_ear + right_ear) / 2

                if avg_ear < EAR_THRESHOLD:
                    frame_counter += 1
                else:
                    if frame_counter >= CONSEC_FRAMES:
                        blink_count += 1
                    frame_counter = 0
    cap.release()
    return blink_count

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    if "video" not in request.files:
        return render_template("index.html", result={"blinks": 0, "report": "No video uploaded!"})

    video = request.files["video"]
    video_path = os.path.join(UPLOAD_FOLDER, video.filename)
    video.save(video_path)

    blinks = process_video(video_path)
    report = eye_health_analysis(blinks)

    return render_template("index.html", result={"blinks": blinks, "report": report})

if __name__ == "__main__":
    app.run(debug=True)
