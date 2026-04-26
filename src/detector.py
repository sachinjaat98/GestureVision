import cv2 as cv
import math

def count_fingers(thresh, roi):
    contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    
    if not contours:
        return 0

    max_cnt = max(contours, key=cv.contourArea)

    hull = cv.convexHull(max_cnt)
    area_hull = cv.contourArea(hull)
    area_cnt = cv.contourArea(max_cnt)

    if area_cnt == 0:
        return 0

    area_ratio = ((area_hull - area_cnt) / area_cnt) * 100

    hull = cv.convexHull(max_cnt, returnPoints=False)
    defects = cv.convexityDefects(max_cnt, hull)

    if defects is None:
        return 0

    count = 0

    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]

        start = tuple(max_cnt[s][0])
        end = tuple(max_cnt[e][0])
        far = tuple(max_cnt[f][0])

        a = math.dist(start, end)
        b = math.dist(start, far)
        c = math.dist(end, far)

        if b * c == 0:
            continue

        angle = math.degrees(math.acos((b**2 + c**2 - a**2) / (2*b*c)))

        if angle < 90:
            count += 1

    return count