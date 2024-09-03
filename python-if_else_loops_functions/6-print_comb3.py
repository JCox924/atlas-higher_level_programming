#!/usr/bin/python3
print(", ".join(f"{i:01d}{j:01d}" for i in range(10) for j in range(i + 1, 10)), end="\n")
