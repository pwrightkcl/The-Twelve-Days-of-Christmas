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
        "a Partridge in a Pear Tree",
        "Two Turtle Doves",
        "Three French Hens",
        "Four Calling Birds",
        "Five Gold Rings",
        "Six Geese-a-Laying",
        "Seven Swans-a-Swimming",
        "Eight Maids-a-Milking",
        "Nine Ladies Dancing",
        "Ten Lords-a-Leaping",
        "Eleven Pipers Piping",
        "Twelve Drummers Drumming"
    ]
    
    # Print each verse of the song
    for day_num in range(12):
        print(f"On the {days[day_num]} day of Christmas,")
        print("my true love gave to me")
        
        # Print gifts in reverse order for this verse
        for gift_num in range(day_num, -1, -1):
            if gift_num == 0 and day_num > 0:
                # Add "and" before the last gift (except on the first day)
                print(f"and {gifts[gift_num]}.")
            elif gift_num == 0:
                # First day only - just the partridge
                print(f"{gifts[gift_num]}.")
            else:
                # All other gifts without ending punctuation
                print(gifts[gift_num])
        
        # Add a blank line between verses (except after the last one)
        if day_num < 11:
            print()


if __name__ == "__main__":
    main()
