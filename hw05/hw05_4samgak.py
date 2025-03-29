import math

print("각 / 라디안 / sin / cos / tan ")
print("-"*50)

for gak in range(0,11):
    rad = math.radians(gak)
    sin_value = math.sin(rad)
    cos_value = math.cos(rad)
    tan_value = math.tan(rad)

    print(f"{gak}∘ / {rad:.4f} / {sin_value:.4f} / {cos_value:.4f} / {tan_value:.4f}")
    print("-"*50)