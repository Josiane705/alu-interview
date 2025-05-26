# Rain

This project calculates how much rainwater can be trapped between walls of different heights, simulating a cross-section of a relief map.

## Requirements

- Python 3.4.3
- No external imports
- PEP8 style
- Ubuntu 14.04 LTS

## How to Use

Example:

```python
#!/usr/bin/python3
rain = __import__('0-rain').rain

walls = [0, 1, 0, 2, 0, 3, 0, 4]
print(rain(walls))  # Output: 6

