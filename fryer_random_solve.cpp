#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <utility>

int main() {
    char s[] = "1_n3}f3br9Ty{_6_rHnf01fg_14rlbtB60tuarun0c_tr1y3";
    size_t len = strlen(s);
    unsigned int seed = 322401073;

    // Record the swaps
    std::vector<std::pair<size_t, size_t>> swaps;

    for (size_t i = 0; i < len - 1; ++i) {
        unsigned int rnd = rand_r(&seed);
        size_t j = i + rnd % (len - i);
        swaps.push_back({i, j});
    }

    // Reverse the swaps
    for (auto it = swaps.rbegin(); it != swaps.rend(); ++it) {
        size_t i = it->first;
        size_t j = it->second;
        char tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
    }

    printf("Original string: %s\n", s);

    return 0;
}

