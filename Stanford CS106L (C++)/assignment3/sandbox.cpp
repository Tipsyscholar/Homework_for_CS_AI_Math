#include "class.h"
#include <iostream>
#include <array>

void sandbox() {
    std::array<int, 5> b = {1, 2, 3, 4, 5};
    Mathvector<int, 5> vec1(b);
    Mathvector<int, 5> vec2(b);
    std::cout << "Vec1 elements: ";
    for(int i = 0; i < 5; i++){
        std::cout << vec1.at(i) << " ";
    }
    std::cout << "\n";

    Mathvector<int, 5> sum = vec1 + vec2; 
    
    std::cout << "Sum elements: ";
    for(int i = 0; i < 5; i++){
        std::cout << sum.at(i) << " ";
    }
    std::cout << "\n";
}