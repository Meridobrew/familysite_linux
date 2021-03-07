from ged4py import GedcomReader

path = r"C:\Python\Python38\Django\familysite\ca1z66_78236416fprf45ca4e51z3.ged"
with GedcomReader(path) as parser:
    for i, indi in enumerate(parser.records0("INDI")):
        # Print a name (one of many possible representations)
        print(f"{i}: {indi.name.format()}")
        pointer = indi.__dict__['xref_id']
        if pointer:
            print(f"ref_id: {pointer}")
        place_death = indi.sub_tag_value("DEAT/PLAC")
        if place_death:
            print(f"место смерти: {place_death}")
        
        place_birth = indi.sub_tag_value("BIRT/PLAC")
        if place_birth:
            print(f'место рождения: {place_birth}')
    
        name_married = indi.sub_tag_value("_MARNM")
        if name_married:
            print(f'фамилия после замужества: {name_married}')

        name_maiden = indi.name.maiden
        if name_maiden:
            print(f'фамилия до замужества:{name_maiden}')
        
        name_last = indi.name.surname
        if name_last:
            print(f'фамилия:{name_last}')
        
        name_first = indi.name.first
        if name_first:
            print(f'имя:{name_first}')
        
        patronym = indi.name.given.split(" ")[-1]
        if patronym:
            print(f'отчество:{patronym}')

        gender = indi.sex
        if gender:
            print(f'пол: {gender}')
        date_death = indi.sub_tag_value("DEAT/DATE")
        if date_death:
            print(f'Дата смерти: {date_death}')
        date_birth = indi.sub_tag_value("BIRT/DATE")
        if date_birth:
            print(f'Дата рождения: {date_birth}')

        individual_notes = indi.sub_tag_value("NOTE")
        if individual_notes:
            print(f'Заметки: {individual_notes}')
        father = indi.father
        if father:
            print(f"    father: {father.name.format()}")

        mother = indi.mother
        if mother:
            print(f"    mother: {mother.name.format()}")
