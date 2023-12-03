import cv2
import time
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class FaceDetectionApp:
    def __init__(self, root, video_source=0):
        self.root = root
        self.root.title("Face Detection App")

        self.video_source = video_source
        self.cap = cv2.VideoCapture(self.video_source)

        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        self.canvas = tk.Canvas(root, width=self.cap.get(3), height=self.cap.get(4))
        self.canvas.pack()

        self.label_fps = ttk.Label(root, text="FPS: 0")
        self.label_fps.pack()

        self.label_detection = ttk.Label(root, text="No Face Detected", font=("Helvetica", 16))
        self.label_detection.pack()

        self.update()

        root.protocol("WM_DELETE_WINDOW", self.on_close)

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        cap = cv2.VideoCapture(0)

        p_time = 0

    def update(self):
        ret, frame = self.cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            c_time = time.time()
            fps = 1 #/ (c_time - self.p_time)
            self.p_time = c_time

            # self.label_fps.config(text=f"FPS: {int(fps)}")

            if len(faces) > 0:
                self.label_detection.config(text="Face Detected", foreground="green")
            else:
                self.label_detection.config(text="No Face Detected", foreground="red")

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            self.photo = self.convert_to_photo(frame)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        self.root.after(10, self.update)

    def convert_to_photo(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=img)
        return photo

    def on_close(self):
        self.cap.release()
        self.root.destroy()

def main():
    root = tk.Tk()
    app = FaceDetectionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
