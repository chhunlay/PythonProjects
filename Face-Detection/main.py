import cv2

def calculate_distance(face_width_pixels):
    """Calculate distance from the camera to the face based on its width in pixels."""
    known_face_width_cm = 15.0  # Average width of a human face in cm
    focal_length = 500  # Adjust based on your camera setup
    if face_width_pixels == 0:
        return 0
    distance = (known_face_width_cm * focal_length) / face_width_pixels
    return distance

def main():
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    # Load the Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Draw rectangles around detected faces and calculate distance
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw rectangle around face
            distance = calculate_distance(w)  # Estimate distance using width
            cv2.putText(frame, f'Distance: {distance:.2f} cm', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Display the resulting frame
        cv2.imshow('Face Detection', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
