import cv2
from segmentation import Region_Growing
import pydicom
import os, sys, getopt


def run_region_growing_on_image(image_path):

    image_data, image_name = get_image_data(image_path)

    image_data = resize_image(image_data)

    image_data_post_smoothing = apply_gaussian_smoothing(image_data)

    region_growing(image_data_post_smoothing, segmentation_name=image_name + " segmentation", neighbours=CONN)


def region_growing(image_data, neighbours, threshold=60, segmentation_name="Region Growing"):
    thresholds = [60, 40, 30, 20]
    for i in thresholds:
        region_growing = Region_Growing(image_data, threshold=i, conn=neighbours)
        result = region_growing.segment()
        if isinstance(result, int):
            continue
        else:
            region_growing.display_and_resegment(name=segmentation_name)
            print(i)
            break

def get_image_data(image_path):
    name, ext = os.path.splitext(image_path)
    if ext == DICOM_IMAGE_EXT:
        return (pydicom.read_file(image_path).pixel_array, name)
    elif ext in OTHER_IMAGE_EXT:
        return (cv2.imread(image_path, 0), name)
    else:
        print("Invalid Image Format. Supported Image Formats are: {}, {}".format(DICOM_IMAGE_EXT, OTHER_IMAGE_EXT))
        sys.exit()


def resize_image(image_data):
    if image_data.shape[0] > 1000:
        image_data = cv2.resize(image_data, (0, 0), fx=0.25, fy=0.25)
    if image_data.shape[0] > 500:
        image_data = cv2.resize(image_data, (0, 0), fx=0.5, fy=0.5)
    return image_data


def apply_gaussian_smoothing(image_data, filter_size=3):
    return cv2.GaussianBlur(image_data, (filter_size, filter_size), 0)


def set_cmd_line_arguments():
    global IMAGE_PATH
    global CONN
    n_args = len(sys.argv)
    if n_args == 1:
        print("No image path specified. TERMINATING!!")
        sys.exit()
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "", ["image_path=", "conn="])
    for opt, arg in opts:
        if opt == "--image_path":
            IMAGE_PATH = arg
        elif opt == "--conn":
            print(arg)
            CONN = int(arg)
        else:
            print("Make sure to spell 'image_path' correctly")
            sys.exit()
    print("Image Path: {}".format(IMAGE_PATH))


DICOM_IMAGE_EXT = '.dcm'
OTHER_IMAGE_EXT = ['.jpg', '.png', '.jpeg', '.pgm']
IMAGE_PATH = "mdb023.png"
# Default image path
CONN = 4

run_region_growing_on_image(IMAGE_PATH)


