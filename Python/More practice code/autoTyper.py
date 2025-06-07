import pyautogui
from PIL import Image
import pytesseract
import time

# Configure pytesseract path (if needed)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Step 1: Capture a screenshot of the specific region
def capture_text_area():
    # Define the region to capture (x, y, width, height)
    # You can use pyautogui.position() to determine these coordinates
    region = (600, 300, 800, 200)  # Example region

    # Capture the screenshot of the defined region
    screenshot = pyautogui.screenshot(region=region)

    # Save the screenshot for debugging purposes
    screenshot.save("type_racer_text_area.png")

    return screenshot

# Step 2: Extract text from the screenshot using OCR
def extract_text_from_image(image):
    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(image)

    # Return the extracted text
    return text

# Main function to capture the screen and extract text
def main():
    time.sleep(5)  # Give you time to switch to the Type Racer window

    # Capture the text area from the screen
    screenshot = capture_text_area()

    # Extract the text from the screenshot
    extracted_text = extract_text_from_image(screenshot)

    # Print the extracted text
    print("Extracted Text:", extracted_text)

if __name__ == "__main__":
    main()
