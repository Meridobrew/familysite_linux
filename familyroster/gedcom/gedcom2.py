import sys
from ged4py.parser import GedcomReader

# open GEDCOM file
with GedcomReader(r"C:\Python\Python38\Django\familysite\ca1z66_78236416fprf45ca4e51z3.ged") as parser:
    # iterate over each INDI record in a file
    for i, indi in enumerate(parser.records0("INDI")):
        # Print a name (one of many possible representations)
        print(f"{i}: {indi.name.format()}")

        father = indi.father
        if father: 
            print(f"    father: {father.__dict__['xref_id']}")

        mother = indi.mother
        if mother: 
            print(f"    mother: {mother.name.format()}")

        # Get _value_ of the BIRT/DATE tag
        birth_date = indi.sub_tag_value("BIRT/DATE")
        if birth_date:
            print(f"    birth date: {birth_date}")

        # Get _value_ of the BIRT/PLAC tag
        birth_place = indi.sub_tag_value("BIRT/PLAC")
        if birth_place:
            print(f"    birth place: {birth_place}")