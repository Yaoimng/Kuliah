import math

def pythagoras(total_distance, remaining_distance, rect_x, rect_y, rect_width, rect_height, point_x, point_y):
    distance = math.sqrt((rect_x - point_x)**2 + (rect_y - point_y)**2)

    if point_x >= rect_x - rect_width / 2 and point_x <= rect_x + rect_width / 2 and point_y >= rect_y - rect_height / 2 and point_y <= rect_y + rect_height / 2:
        print("KAMU SUDAH SAMPAI")
    else:
        print("{:.2f} METER LAGI".format(distance))

total_distance, remaining_distance = map(int, input().split())
rect_x, rect_y, rect_width, rect_height = map(int, input().split())
point_x, point_y = map(int, input().split())

pythagoras(total_distance, remaining_distance, rect_x, rect_y, rect_width, rect_height, point_x, point_y)
