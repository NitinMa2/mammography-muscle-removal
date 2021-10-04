# ## Import Libraries
import base64
import sys
from io import BytesIO
# import cv2
import numpy as np
from PIL import ImageEnhance, Image


# ## Preprocessing
# 1. Left align 
# 2. Perform contrast
# 3. Remove bar


def left_align(img):
    """
    Determines whether the breast is aligned to the right or left side of the image
    by measuring the mean gray level of either half. Flips the image to the left if it
    is right-aligned.
    
    Parameters:
        img: The numpy array representing the image.
    
    Assumptions:
        - The half of the image on which the majority of the breast region lies has a higher mean than the othe half
        - The input image is LCC view
    
    Returns:
        numpy array with the left aligned image.
    """
    pixels = np.asarray(img)
    if np.mean(pixels[0:256, 0:128]) < np.mean(pixels[0:256, 128:256]):
        return pixels[:, ::-1]
    return pixels


def perform_contrast(img):
    """
    Adjusts the contrast of the given image by a specific factor.
    
    Parameters:
        img: PIL image to be adjusted
    Assumptions:
        None
    Returns:
        PIL image with the contrast adjusted.
    """
    enhancer = ImageEnhance.Contrast(img)
    factor = 1.3  # increase contrast
    img = enhancer.enhance(factor)
    return img


def remove_bar(img):
    """
    Finds the width of the black bar on the left of the image by checking iteratively until a pixel whose value is greater than
    the mean of the grey values of the image is found. Then crops the image to remove the bar.
    
    Parameters:
        img: numpy array of the image to be adjusted
    Assumptions:
        - There is no blank space at the top of the image (not even 1px)
        - The image is left-aligned
        - The black bar is darker than the mean grey level of the image, and the pectoral muscle region is brighter.
    Returns:
        Numpy array of the cropped image
    """
    width = 0
    while img[1, width] <= np.mean(img):
        width += 1
    return img[:, width:256]


def preprocess_image(img):
    """
    Combines all of the above preprocessing steps together on a given image.
    
    Parameters:
        img: PIL image to be adjusted
    Assumptions:
        - There is no blank space at the top of the image (not even 1px).
        - We want to optimize for speed over precision.
        - The input image is LCC view.
        - The half of the image on which the majority of the breast region lies has a higher mean than the other half.
        
    Returns:
        PIL image ready for the level set algorithm.
    """
    img = img.resize((256, 256))
    img = left_align(img)
    img = remove_bar(img)
    img = np.interp(img, [np.min(img), np.max(img)], [0, 255])
    return img


# Region Growing Algorithm
def is_pixel_inside_image(pixel, img_shape):
    return 0 <= pixel[0] < img_shape[0] and 0 <= pixel[1] < img_shape[1]


class Region_Growing():
    def __init__(self, img, max_iter, threshold, conn=4):
        self.img = img
        self.segmentation = np.empty(shape=img.shape)
        self.segmentation.fill(255)
        self.max_iter_to_change_threshold = max_iter

        self.threshold = threshold
        self.seeds = [(1, 1)]
        if conn == 4:
            self.orientations = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        elif conn == 8:
            self.orientations = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]  # 8 connectivity
        else:
            raise ValueError("(%s) Connectivity type not known (4 or 8 available)!" % sys._getframe.f_code.co_name)

    def segment(self):
        """
        Segment the image with the provided user seeds using region growing
        """
        for seed in self.seeds:
            curr_pixel = [seed[1], seed[0]]
            if self.segmentation[curr_pixel[0], curr_pixel[1]] == 0:
                continue  # pixel already explored
            contour = []
            seg_size = 1
            mean_seg_value = (self.img[curr_pixel[0], curr_pixel[1]])
            dist = 0
            iterations = 0
            while dist < self.threshold:
                if iterations > self.max_iter_to_change_threshold and self.threshold != 2.5:
                    return 0
                # Include current pixel in segmentation
                self.segmentation[curr_pixel[0], curr_pixel[1]] = 0
                # Explore neighbours of current pixel
                contour = self.__explore_neighbours(contour, curr_pixel)
                # Get the nearest neighbour
                nearest_neighbour_idx, dist = self.__get_nearest_neighbour(contour, mean_seg_value)
                # If no more neighbours to grow, move to the next seed
                if nearest_neighbour_idx == -1: break
                # Update Current pixel to the nearest neighbour and increment size
                curr_pixel = contour[nearest_neighbour_idx]
                seg_size += 1
                # Update Mean pixel value for segmentation
                mean_seg_value = (mean_seg_value * seg_size + float(self.img[curr_pixel[0], curr_pixel[1]])) / (
                        seg_size + 1)
                # Delete from contour once the nearest neighbour as chosen as the current node for expansion
                iterations += 1
                del contour[nearest_neighbour_idx]
        return self.segmentation

    def display_and_resegment(self, name="Region Growing"):
        # Display original image where segmentation was not done
        result = np.minimum(self.img, self.segmentation)
        result = np.array(result, dtype=np.uint8)

        # Display the result
        return result

    def __explore_neighbours(self, contour, current_pixel):
        for orientation in self.orientations:
            neighbour = self.__get_neighbouring_pixel(current_pixel, orientation, self.img.shape)
            if neighbour is None:
                continue
            if self.segmentation[neighbour[0], neighbour[1]] == 255:
                contour.append(neighbour)
                self.segmentation[neighbour[0], neighbour[1]] = 150
        return contour

    def __get_neighbouring_pixel(self, current_pixel, orient, img_shape):
        neighbour = (current_pixel[0] + orient[0], current_pixel[1] + orient[1])
        if is_pixel_inside_image(pixel=neighbour, img_shape=img_shape):
            return neighbour
        else:
            return None

    def __get_nearest_neighbour(self, contour, mean_seg_value):
        dist_list = [abs(self.img[pixel[0], pixel[1]] - mean_seg_value) for pixel in contour]
        if len(dist_list) == 0: return -1, 1000
        min_dist = min(dist_list)
        index = dist_list.index(min_dist)
        return index, min_dist


def region_growing(image_data, max_iter, neighbours, segmentation_name="Region Growing"):
    thresholds = [60, 40, 30, 20, 10, 5, 2.5]
    for i in thresholds:
        region_growing = Region_Growing(image_data, max_iter, threshold=i, conn=neighbours)
        result = region_growing.segment()
        if isinstance(result, int):
            continue
        else:
            return region_growing.display_and_resegment(name=segmentation_name)


def preprocessing(image_base64):
    contrasted_img = perform_contrast(image_base64)
    processed_img = preprocess_image(contrasted_img)
    return processed_img


def run_region_growing_on_image(image_base64):
    if isinstance(image_base64, str):
        image_base64 = image_base64.encode('utf-8')
    im_bytes = base64.b64decode(image_base64)  # im_bytes is a binary image
    im_file = BytesIO(im_bytes)
    image = Image.open(im_file)
    image = image.convert("L")
    preprocessed_image = preprocessing(image)
    segmented_img = region_growing(preprocessed_image, 6200, neighbours=4)
    # _, imagebytes = cv2.imencode('.png', segmented_img)
    pil = Image.fromarray(np.uint8(segmented_img)).convert('L')
    buffered = BytesIO()
    pil.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue())
    return img_str.decode('utf-8')


# testing function only the api will call run_region_growing_on_image with base64 image
def img2string(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        run_region_growing_on_image(encoded_string)


print(run_region_growing_on_image('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'))
