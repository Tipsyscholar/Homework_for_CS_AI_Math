#pragma once
#include <array>
#include <concepts>
#include <iostream>  
#include <cstddef>
#include <stdexcept> 

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

    Mathvector<T, N> operator+(const Mathvector<T, N>& other);
    
    const T& at(std::size_t n) const;
    T& at(std::size_t n);
    
    mutable int count = 0;
};



template<class T, std::size_t N>
requires law<T, N>
const T& Mathvector<T, N>::at(std::size_t n) const {
    if (n >= N) {
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
        result.a_[i] = other.a_[i] + this->a_[i];
    }
    return result; 
}