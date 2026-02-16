```c
#include <stdio.h>

struct Nijal {
    int a;
    int b;
};
void Nijalll(struct Nijal *nijalInstance) {
    printf("%d\n", nijalInstance->a + nijalInstance->b);
}

int main() {
    struct Nijal nijalInstance;
    nijalInstance.a = 1;
    nijalInstance.b = 0;
    Nijalll(&nijalInstance);
    printf("%d\n", nijalInstance.b);
    return 0;
}
```