def unique_styles(styles: list[str]) -> int:
    genres = set()
    for style in styles:
        data = style.split(",")
        for d in data:
            genres.add(d)
    return len(genres)

# TEST

us1 = unique_styles([
  "Dub,Dancehall",
  "Industrial,Heavy Metal",
  "Techno,Dubstep",
  "Synth-pop,Euro-Disco",
  "Industrial,Techno,Minimal"
])

us2 = unique_styles([
  "Soul",
  "House,Folk",
  "Trance,Downtempo,Big Beat,House",
  "Deep House",
  "Soul"
])

print(us1)
'''
Expected Output: 9
'''

print(us2)
'''
Expected Output: 7
'''