from fer import FER
import cv2
import movie

img = cv2.imread("tanay.jpg")
detector = FER()
detector.detect_emotions(img)