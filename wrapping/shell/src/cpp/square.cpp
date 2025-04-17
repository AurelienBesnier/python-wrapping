#include <string>

float square(float x) { return x * x; }


int main(int argc, char **argv)
{
        float res = square(std::stof(argv[1]));
        return res;
}