from ged4py import GedcomReader

path = r"C:\Python\Python38\Django\familysite\ca1z66_78236416fprf45ca4e51z3.ged"
people = []
with GedcomReader(path) as parser:
    for i, indi in enumerate(parser.records0("INDI")):
        people.append(i)
json = ''
json += '[ \n'
with GedcomReader(path) as parser:
    for i, indi in enumerate(parser.records0("INDI")):
        if len(indi.name.given.split(" ")) > 1:
            patronym = indi.name.given.split(" ")[-1]
        gedcom_id = indi.__dict__['xref_id']
        place_death = indi.sub_tag_value("DEAT/PLAC")
        place_birth = indi.sub_tag_value("BIRT/PLAC")
        name_maiden = indi.name.maiden
        name_last = indi.name.surname
        name_first = indi.name.first
        individual_notes = indi.sub_tag_value("NOTE")
        #individual_id
        gender = indi.sex
        date_death = indi.sub_tag_value("DEAT/DATE")
        date_birth = indi.sub_tag_value("BIRT/DATE")
        json += '\t{ \n'
        json += '\t\t"model" : "familysite.familyroster.Individual",' + ',\n'
        json += '\t\t"pk" : ' + f'{i+1}' + ',\n'
        json += '\t\t"fields" : {\n'
        json += '\t\t\t"gedcom_id" : ' + f'"{gedcom_id}"' + ',\n'
        json += '\t\t\t"name_last" : ' + f'"{name_last}"' + ',\n'
        json += '\t\t\t"name_first" : ' + f'"{name_first}"' + ',\n'
        if len(indi.name.given.split(" ")) > 1:
            json += '\t\t\t"patronym" : ' + f'"{patronym}"' + ',\n'
        if name_maiden:
            json += '\t\t\t"name_maiden" : ' + f'"{name_maiden}"' + ',\n'
        if gender:
            json += '\t\t\t"gender" : ' + f'"{gender}"' + ',\n'
        if date_birth:
            json += '\t\t\t"date_birth" : ' + f'"{date_birth}"' + ',\n'
        if date_death:

            json += '\t\t\t"date_death" : ' + f'"{date_death}"' + ',\n'
        if place_birth:
            json += '\t\t\t"place_birth" : ' + f'"{place_birth}"' + ',\n'
        if place_death:
            json += '\t\t\t"place_death" : ' + f'"{place_death}"' + ',\n'
        if individual_notes:
            json += '\t\t\t"individual_notes" : ' + f'"{individual_notes}"' + '\n'
        #rint(type(json))
        #print(f'length: {len(people)}')
        if i == (len(people) - 1):
            json += '\t\t}\n'
            json += '\t}\n'
        else:
            json += '\t\t}\n'
            json += '\t},\n'
json += ']'
print(json)
print(type(json))
f = open("1.json", "w", encoding="UTF-8") # creat/open the output file
f.write(json)
f.close() # save