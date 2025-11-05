#!/usr/bin/env python3
"""
The Twelve Days of Christmas
A Python script that prints the lyrics to the classic Christmas carol.
"""


def main():
    """Print the complete lyrics of 'The Twelve Days of Christmas' song."""
    
    # Days of Christmas in ordinal form
    days = [
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]
    
    # Gifts for each day
    gifts = [
        "a partridge in a pear tree.",
        "two turtle doves,",
        "three french hens,",
        "four calling birds,",
        "five gold rings,",
        "six geese-a-laying,",
        "seven swans-a-swimming,",
        "eight maids-a-milking,",
        "nine ladies dancing,",
        "ten lords-a-leaping,",
        "eleven pipers piping,",
        "twelve drummers drumming,"
    ]
    
    # Print each verse of the song
    for day_num in range(12):
        print(f"On the {days[day_num]} day of Christmas my true love gave to me:")
        
        # Print gifts in reverse order for this verse
        for gift_num in range(day_num, -1, -1):
            if gift_num == 0 and day_num > 0:
                # Add "and" before the last gift (except on the first day)
                print(f"and {gifts[gift_num]}.")
            elif gift_num == 0:
                # First day only - just the partridge
                print(f"{gifts[gift_num]}")
            else:
                # All other gifts without ending punctuation
                print(gifts[gift_num])
        
        # Add a blank line between verses (except after the last one)
        if day_num < 11:
            print()


if __name__ == "__main__":
    main()
