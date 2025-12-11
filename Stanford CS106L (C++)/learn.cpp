#include <iostream>
#include <string>
#include <sstream>

void foo() {
    /// partial Bjarne Quote
    std::string initial_quote = "Bjarne Stroustrup C makes it easy to shoot yourself in the foot\n";
    
    /// create a stringstream
    std::stringstream ss(initial_quote);
    
    /// data destinations
    std::string first;
    std::string last;
    std::string language, extracted_quote;
    
    ss >> first >> last >> language;
    std::getline(ss, extracted_quote);
    
    std::cout << first << " " << last << " said this: '" << language << " " << extracted_quote + "'" << std::endl;
}

#include <fstream>
int main()  {
    std::string a,b;
    std::cin>>a>>b;
    std::cout<<a<<'\n';
    std::cout <<b<<'\n';
    return 0;

}