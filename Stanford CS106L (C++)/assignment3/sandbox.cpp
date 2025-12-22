#include "class.h"
#include <iostream>
#include <array>

void sandbox() {
    // 1. 创建基础数组
    std::array<int, 5> b = {1, 2, 3, 4, 5};
    
    // 2. 实例化 Mathvector
    Mathvector<int, 5> vec1(b);
    Mathvector<int, 5> vec2(b);

    // 3. 测试 at()
    std::cout << "Vec1 elements: ";
    for(int i = 0; i < 5; i++){
        std::cout << vec1.at(i) << " ";
    }
    std::cout << "\n";

    // 4. 测试 operator+
    // 如果不按值返回，这里会崩溃或乱码
    Mathvector<int, 5> sum = vec1 + vec2; 
    
    std::cout << "Sum elements: ";
    for(int i = 0; i < 5; i++){
        std::cout << sum.at(i) << " ";
    }
    std::cout << "\n";
}