import tkinter as tk
import cv2

class App:
    def __init__(self, window, video_source=0):
        self.window = window
        self.window.title("OpenCV Video Stream")
        
        self.video_source = video_source
        
        # Create a canvas widget to display the video stream
        self.canvas = tk.Canvas(window, width=640, height=480)
        self.canvas.pack()
        
        # Create a close button
        self.close_button = tk.Button(window, text="Close", command=self.close)
        self.close_button.pack()
        
        # Open the video source
        self.cap = cv2.VideoCapture(self.video_source)
        
        # Start the video stream
        self.update()
        
    def update(self):
        # Get a frame from the video source
        ret, frame = self.cap.read()
        
        if ret:
            # Convert the frame from BGR to RGB format
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Display the frame on the canvas
            self.photo = tk.PhotoImage(image=tk.BitmapImage(image=frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        
        # Schedule the next update after 10 milliseconds
        self.window.after(10, self.update)
        
    def close(self):
        # Release the video source and destroy the window
        self.cap.release()
        self.window.destroy()

