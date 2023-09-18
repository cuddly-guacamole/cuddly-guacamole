#include <iostream> // 包含iostream头文件，用于输入输出操作

int main() { // 定义一个名为main的函数，返回类型是int
   int n; // 定义一个整型变量n，用于存储用户输入的n的值
   std::cout << "请输入循环的次数："; // 输出提示信息，提示用户输入n的值
   std::cin >> n; // 使用std::cin从用户那里读取n的值，并将其存储在变量n中

   int count = 0; // 定义一个整型变量count，用于存储当前循环的次数
   while (count < n) { // 当count小于n时，执行以下操作
       std::cout << "hello,world!" << std::endl; // 输出"hello,world!"
       count++; // 将count的值加1，准备下一次循环
   }

   return 0; // 程序执行结束，返回0
}