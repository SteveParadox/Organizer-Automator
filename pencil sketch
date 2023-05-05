import cv2

def nothing(x):
    pass

image = cv2.imread("dog.jpeg")
resized = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
cv2.imshow("Resized Design", resized)
cv2.waitKey(0)

gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
cv2.imshow("New Design", gray_image)
cv2.waitKey(0)

inverted_image = 255 - gray_image
cv2.imshow("Inverted", inverted_image)
cv2.waitKey()




while True:
 
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    cv2.imshow("Sketch", pencil_sketch)
    
    key = cv2.waitKey(1) & 0xFF

    # If the 's' key is pressed, save the image to a file
    if key == ord('s'):
        cv2.imwrite("pencil_sketch.png", pencil_sketch)
        print("Image saved!")
    
    if key == ord('r'):
        angle = int(input("Enter the angle to rotate the image by: "))
        rotated = cv2.rotate(resized, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow("Rotated", rotated)
    
    
    # If the 'x' key is pressed, exit the loop
    if key == ord('x'):
        break

cv2.destroyAllWindows()
