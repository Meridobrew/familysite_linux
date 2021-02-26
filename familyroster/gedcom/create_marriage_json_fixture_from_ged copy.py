from ged4py import GedcomReader
path = r"C:\Python\Python38\Django\familysite\ca1z66_78236416fprf45ca4e51z3.ged"
people = []
with GedcomReader(path) as parser:
    for i, fam in enumerate(parser.records0("FAM")):
        people.append(i)
json = ''
json += '[ \n'
with GedcomReader(path) as parser:
    for i, fam in enumerate(parser.records0("FAM")):
        husband = fam.sub_tag("HUSB")
        if husband is None:
            continue
        husband_gedcom_id = husband.xref_id
        wife = fam.sub_tag("WIFE")
        if wife is None:
            continue
        wife_gedcom_id = wife.xref_id
        try:
            c = Individual.objects.get(gedcom_id__exact=husband_gedcom_id)
            individual_1_id = c.id
        except Individual.DoesNotExist:
            c = None
            individual_1_id = None
        try:
            d = Individual.objects.get(gedcom_id__exact=wife_gedcom_id)
            individual_2_id = d.id
        except Individual.DoesNotExist:
            d = None
            individual_2_id = None
        json += '\t{ \n'
        json += '\t\t"model" : "familyroster.Relationship"' + ',\n'
        json += '\t\t"pk" : ' + f'{i+1}' + ',\n'
        json += '\t\t"fields" : {\n'
        json += '\t\t\t"relationship_type" : ' + f'"Marriage"' + ',\n'
        json += '\t\t\t"individual_1_id" : ' + f'"{individual_1_id}"' + ',\n'
        json += '\t\t\t"individual_1_role" : ' + f'"Муж"' + ',\n'
        json += '\t\t\t"individual_2_id" : ' + f'"{individual_2_id}"' + ',\n'
        json += '\t\t\t"individual_2_role" : ' + f'"Жена"' + '\n'

            #if individual_notes:
            #    json += '\t\t\t"individual_notes" : ' + f'"{individual_notes}"' + '\n
            #rint(type(json))
            #print(f'length: {len(people)}')
        if i == (len(people) - 1):
            json += '\t\t}\n'
            json += '\t}\n'
        else:
            json += '\t\t}\n'
            json += '\t},\n'

json += ']'
f = open("relationship_marriage.json", "w", encoding="UTF-8") # creat/open the output file
f.write(json)
f.close() # save