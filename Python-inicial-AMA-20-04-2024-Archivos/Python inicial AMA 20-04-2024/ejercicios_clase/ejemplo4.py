import cv2


def show_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error al cargar la imagen: {image_path}")
        return

    cv2.namedWindow("Image Viewer", cv2.WINDOW_NORMAL)
    cv2.imshow("Image Viewer", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


show_image("images.jpeg")
