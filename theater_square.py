n, m, a = map(int, input().split())
flagstones_length = (n + a - 1) // a
flagstones_width = (m + a - 1) // a
total_flagstones = flagstones_length * flagstones_width
print(total_flagstones)