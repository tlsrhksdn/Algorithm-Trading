# 5-1
# def myaverage(a,b):
#     return (a+b)/2

# print(myaverage(2,4))

# 5-2
# def get_max_min(data_list):
#     max_val=max(data_list)
#     min_val=min(data_list)
#     return (max_val,min_val)

# max_val,min_val=get_max_min([1,2,3,4,5])

# max_val
# min_val

# 5-3
# import os
# def get_txt_list(path):
#     org_list=os.listdir(path)
#     ret_list=[]
#     for x in org_list:
#         if x.endswith('txt'):
#             ret_list.append(x)
#     return ret_list
# print(get_txt_list('c:/'))

# 5-4
# def check_bmi(weight,height):
#     height=height*0.01
#     BMI=weight/(height*height)
#     if BMI<18.5:
#         print("마른체형")
#     elif 18.5<=BMI<25:
#         print("표준")
#     elif 25.0<=BMI<30:
#         print("비만")
#     else:
#         print("고도 비만")
        
# check_bmi(63,170)

# 5-5
# def check_bmi(height,weight):
#     height=height*0.01
#     BMI=weight/(height*height)
#     print("BMI: ",BMI)
#     if BMI<18.5:
#         print("마른체형")
#     elif 18.5<=BMI<25:
#         print("표준")
#     elif 25.0<=BMI<30:
#         print("비만")
#     else:
#         print("고도 비만")
        
# while 1:
#     height=input("키(cm)를 입력하십시오: ")
#     weight=input("몸무게(kg)를 입력하십시오: ")
#     check_bmi(float(height),float(weight))
    
# 5-6
# def get_triangle_area(width,height):
#     return width*height/2


# 5-7
# def add_start_to_end(start,end):
#     return sum(range(start,end+1))

# print(add_start_to_end(1,5))    

from unittest import result


5-8
def return_three_str(data_list):
    result=[]
    for x in data_list:
        result.append(x[:3])
    return result

print(return_three_str(['Seoul','Daegu','Busan']))