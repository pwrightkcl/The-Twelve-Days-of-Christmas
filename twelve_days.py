"""
The Twelve Days of Christmas
Build the song lyrics using lists of gifts
"""


def get_gifts():
    """Return a list of gifts for each day of Christmas"""
    return [
        "a partridge in a pear tree",
        "two turtle doves",
        "three French hens",
        "four calling birds",
        "five gold rings",
        "six geese a-laying",
        "seven swans a-swimming",
        "eight maids a-milking",
        "nine ladies dancing",
        "ten lords a-leaping",
        "eleven pipers piping",
        "twelve drummers drumming"
    ]


def get_day_ordinal(day):
    """Return the ordinal string for a given day number (1-12)"""
    if not 1 <= day <= 12:
        raise ValueError(f"Day must be between 1 and 12, got {day}")
    
    ordinals = [
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]
    return ordinals[day - 1]


def generate_verse(day):
    """Generate a verse for the given day (1-12)"""
    if not 1 <= day <= 12:
        raise ValueError(f"Day must be between 1 and 12, got {day}")
    
    gifts = get_gifts()
    ordinal = get_day_ordinal(day)
    
    # Start with the opening line
    verse = f"On the {ordinal} day of Christmas, my true love gave to me\n"
    
    # Add gifts in reverse order (from current day down to day 1)
    for i in range(day - 1, -1, -1):
        if i == 0 and day > 1:
            # Add "and" before the last gift on days after the first
            verse += f"And {gifts[i]}.\n"
        else:
            # Capitalize only the first letter while preserving rest of the string
            gift = gifts[i]
            verse += f"{gift[0].upper()}{gift[1:]}.\n"
    
    return verse


def generate_song():
    """Generate the complete Twelve Days of Christmas song"""
    verses = []
    for day in range(1, 13):
        verses.append(generate_verse(day))
    
    return "\n".join(verses)


if __name__ == "__main__":
    print(generate_song())
