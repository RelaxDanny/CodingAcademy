#전역변수와 지역변수가 함께 사용된 프로그램
seconds_per_minute = 60  # 1분은 60초 ❶

def minutes_to_seconds(minutes):
    """분을 입력받아 같은 시간만큼의 초를 반환한다."""
    seconds = minutes * seconds_per_minute  # ❷
    return seconds

print(minutes_to_seconds(3))  # 화면에 180이 출력된다
print(seconds)  # ❸ 오류! 함수 밖에서 지역변수를 불렀다


# #다음 프로그램에서 사용된 전역변수와 지역변수를 각각 나열해 보아라. 각 지역변수가 어느 함수에 속하는지도 구분해 보아라.
# pi = 3.141592653589793

# def area_of_circle(radius):
#     """원의 반지름(radius)을 입력받아 넓이를 반환한다."""
#     area = radius * radius * pi
#     return area

# def volume_of_cylinder(radius, height):
#     """원기둥의 반지름(radius)과 높이(height)를 입력받아
#     부피를 반환한다."""
#     top_area = area_of_circle(radius)
#     volume = top_area * height
#     return volume

# result = volume_of_cylinder(5, 10)
# print(result)



# #함수 안에서 전역변수를 수정하려는 오류
# num_stamp = 0  # 쿠폰 스탬프가 찍힌 횟수 (전역변수)

# def stamp():
#     """쿠폰 스탬프가 찍힌 횟수를 증가시키고, 화면에 출력한다."""
#     num_stamp = num_stamp + 1  # ❶ 전역변수를 수정하려고 시도함
#     print(num_stamp)



# #global 문의 사용
# num_stamp = 0  # 쿠폰 스탬프가 찍힌 횟수 (전역변수)

# def stamp():
#     """쿠폰 스탬프가 찍힌 횟수를 증가시키고, 화면에 출력한다."""
#     global num_stamp           # ❶ num_stamp는 전역변수다
#     num_stamp = num_stamp + 1  # 이제 오류가 발생하지 않는다
#     print(num_stamp)

# stamp()  # 화면에 1이 출력된다
# stamp()  # 화면에 2가 출력된다


##매개변수와 반환을 이용한 stamp() 함수
# num_stamp = 0  # ❶ 쿠폰 스탬프가 찍힌 횟수 (전역변수)

# def stamp(num_stamp):  # ❷ 지역변수(매개변수) num_stamp
#     """쿠폰 스탬프가 찍힌 횟수를 증가시키고, 화면에 출력한다."""
#     num_stamp = num_stamp + 1
#     print(num_stamp)
#     return num_stamp

# num_stamp = stamp(num_stamp)  # ❸ 전역변수에 함수의 반환값을 대입한다
# num_stamp = stamp(num_stamp)