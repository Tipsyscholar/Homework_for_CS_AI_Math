#pragma once
#include <array>
#include <concepts>
#include <iostream>  
#include <cstddef>
#include <stdexcept> // 需要这个来抛出异常

// 定义 Concept
template<typename T, std::size_t N>
concept law = (N > 0) && (N < 10000) && requires(const T& a, const T& b) {
    { a < b } -> std::convertible_to<bool>;
};

template<typename T, std::size_t N>
requires law<T, N> 
class Mathvector {
private:
    std::array<T, N> a_;

public:
    Mathvector() = default;
    explicit Mathvector(const std::array<T, N>& b) : a_(b) {};
    ~Mathvector() = default;

    std::array<T, N>& copy();
    
    // 注意：这里返回类型去掉引用 &，改为按值返回
    Mathvector<T, N> operator+(const Mathvector<T, N>& other);
    
    const T& at(std::size_t n) const;
    T& at(std::size_t n);
    
    mutable int count = 0;
};

// ==========================================
// 模板的实现必须放在头文件中 (Header-Only)
// ==========================================

template<class T, std::size_t N>
requires law<T, N>
const T& Mathvector<T, N>::at(std::size_t n) const {
    if (n >= N) {
        // 必须抛出异常，只打印cerr没法阻止程序崩溃
        throw std::out_of_range("Index out of bounds");
    }
    return a_[n];
}

template<class T, std::size_t N>
requires law<T, N>
T& Mathvector<T, N>::at(std::size_t n) {
    if (n >= N) {
        throw std::out_of_range("Index out of bounds");
    }
    return a_[n];
}

template<class T, std::size_t N>
requires law<T, N>
std::array<T, N>& Mathvector<T, N>::copy() {
    return a_;
}

template<class T, std::size_t N>
requires law<T, N>
Mathvector<T, N> Mathvector<T, N>::operator+(const Mathvector<T, N>& other) {
    Mathvector<T, N> result;
    for (std::size_t i = 0; i < N; i++) {
        // 修正：使用 other.a_[i] 而不是 other[i]
        // result.a_[i] 需要确保 result 初始化是安全的（对于int是随机值，但这里立刻赋值了所以没问题）
        result.a_[i] = other.a_[i] + this->a_[i];
    }
    return result; // 按值返回
}