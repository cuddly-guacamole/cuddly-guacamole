# 定义两个函数：一个用于将摄氏度转换为华氏度，另一个用于将华氏度转换为摄氏度
def celsius_to_fahrenheit(celsius):
   return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
   return (fahrenheit - 32) * 5/9

while True:
   # 获取用户输入的摄氏度或华氏度
   temp = input("请输入温度（例如，36℃）：")

   # 判断用户输入的类型并执行相应的函数
   if temp.endswith('℃'):
      # 将摄氏度转换为华氏度并输出
      fahrenheit = celsius_to_fahrenheit(float(temp[:-1]))
      print("华氏度为：", fahrenheit, "℉")
   elif temp.endswith('℉'):
      # 将华氏度转换为摄氏度并输出
      celsius = fahrenheit_to_celsius(float(temp[:-1]))
      print("摄氏度为：", celsius, "℃")
   else:
      # 输入错误，输出提示信息
      print("输入错误，请输入正确的温度值，例如，36℃或86℉")
      continue