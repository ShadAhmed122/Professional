import cv2

# Path to the image file
image_path = 'welcome.png'  # Change this to your image path

# Desired dimensions
new_width = 1600  # Desired width
new_height = 900  # Desired height

# Read the image from the specified path
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Unable to load image at {image_path}.")
else:
    # Display original dimensions
    original_height, original_width = image.shape[:2]
    print(f"Original Dimensions: {original_width}x{original_height}")

    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height))

    # Display new dimensions
    resized_height, resized_width = resized_image.shape[:2]
    print(f"Resized Dimensions: {resized_width}x{resized_height}")

    # Show the original image
    # cv2.imshow("Original Image", image)

    # Show the resized image
    cv2.imshow("Resized Image", resized_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
