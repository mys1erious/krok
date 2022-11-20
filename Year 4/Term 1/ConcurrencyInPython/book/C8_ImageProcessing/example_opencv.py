import cv2


if __name__ == '__main__':
    im = cv2.imread('input/ship.jpg')
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    mean_thresh_im = cv2.adaptiveThreshold(
        im, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY, 11, 2
    )
    gauss_thresh_im = cv2.adaptiveThreshold(
        im, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2
    )

    cv2.imshow('Mean', mean_thresh_im)
    cv2.imshow('Gauss', gauss_thresh_im)
    cv2.waitKey(0)
