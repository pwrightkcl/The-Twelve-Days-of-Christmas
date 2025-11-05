# The-Twelve-Days-of-Christmas
The Twelve Days of Christmas in Python

## Description
This project generates the lyrics to "The Twelve Days of Christmas" using Python lists to store and organize the gifts that "my true love gave to me."

## Features
- Uses lists to store gifts for each day
- Generates individual verses for each day (1-12)
- Generates the complete song with all 12 verses
- Properly formats the lyrics with correct ordinals and capitalization

## Usage

### Run the complete song
```bash
python3 twelve_days.py
```

### Use as a module
```python
from twelve_days import generate_song, generate_verse, get_gifts

# Generate the complete song
song = generate_song()
print(song)

# Generate a specific verse (e.g., day 5)
verse = generate_verse(5)
print(verse)

# Get the list of all gifts
gifts = get_gifts()
print(gifts)
```

## Testing
Run the unit tests to verify the implementation:
```bash
python3 -m unittest test_twelve_days.py -v
```

## Implementation Details
- `get_gifts()`: Returns a list of all 12 gifts
- `get_day_ordinal(day)`: Converts a day number (1-12) to its ordinal form (first, second, etc.)
- `generate_verse(day)`: Generates the verse for a specific day
- `generate_song()`: Generates the complete song with all 12 verses
