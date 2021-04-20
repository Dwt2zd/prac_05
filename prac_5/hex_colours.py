def main():
    color_table={"aliceblue": "#f0f8ff", "aquamarine1": "#7fffd4", "azure1": "#f0ffff",
                 "black": "#000000", "blue1": "#0000ff", "lawngreen": "#7cfc00",
                 "lightskyblue": "#87cefa", "maroon1": "maroon1", "palegreen": "#98fb98", "plum": "#dda0dd"}
    colorname=input("Enter the name of color: ").lower()
    while colorname != '':
        if colorname in color_table:
            print(colorname, "is", color_table[colorname])
        else:
            print("Invalid input.")
        colorname=input("Enter the name of color: ").lower()
main()