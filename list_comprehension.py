# https://www.youtube.com/watch?v=AhSvKGTh28Q

# list: [1, 2, "a", 3.14]

# list comprehensions:
#     [expr for val in collection]
#     [expr for val in collection if <test>]
#     [expr for val in collection if <test1> and <test2>]
#     [expr for val1 in collection1 and val2 in collection2]

# squares = []
# for i in range(1, 101):
#     squares.append(i**2)
#
# print(squares)
#
# squares2 = [i**2 for i in range (1, 101)]
# print(squares2)

# remainders5 = [x**2 % 5 for x in range (1, 101)]
# print(remainders5)
#
# remainders11 = [x**2 % 11 for x in range (1, 101)]
# print(remainders11)

movies = ["Star Wars", "Ghandi", "Casablanca", "Shawshank Redemption", "Toy Story", "Gone with the Wind",
          "Citizen Kane", "It's a Wonderful Life", "The Wizard of Oz", "Gattaca", "Rear Window", "Ghostbusters",
          "To Kill A Mockingbird", "Good Will Hunting", "2001: A Space Odyssey", "Raiders of the Lost Ark",
          "Groundhog Day", "Close Encounters of the Third Kind"]

# gmovies = []
# for title in movies:
#     if title.startswith("G"):
#         gmovies.append(title)

# print(gmovies)

gmovies = [title for title in movies if title.startswith("G")]
print(gmovies)
