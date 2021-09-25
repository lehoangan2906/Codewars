#include <string>
bool solution(std::string const &str, std::string const &ending) {
    if(str.size() >= ending.size() &&
            str.compare(str.size() - ending.size(), ending.size(), ending) == 0)
            return true;
        else
            return false;
}