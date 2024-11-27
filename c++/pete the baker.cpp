#include <unordered_map>
#include <string>
#include <algorithm>
using namespace std;

using Ingredients = unordered_map<std::string, int>;

int cakes(const Ingredients& recipe, const Ingredients& available) {
    int ans = INT_MAX; // Initialize with the maximum possible value for an integer
    
    for (const auto& x : recipe) {
        auto it = available.find(x.first);
        if (it == available.end()) {
            return 0; // Ingredient missing, can't bake any cakes
        }
        ans = min(ans, it->second / x.second);
    }
    
    return ans;
}
