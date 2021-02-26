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
        gedcom_id = indi.__dict__['xref_id']
        father = indi.father
        mother = indi.mother
        if indi.sex == 'F':
            child = "Дочь"
        elif indi.sex == 'M':
            child = "Сын"
        try:
            c = Individual.objects.get(gedcom_id__exact=gedcom_id)
            individual_1_id = c.id
        except Individual.DoesNotExist:
            c = None
            individual_1_id = None
        if father:
            father_id = father.__dict__['xref_id']
            try:
                a = Individual.objects.get(gedcom_id__exact=father_id)
                individual_2_father_id = a.id
            except Individual.DoesNotExist:
                a = None
        if mother:
            mother_id = mother.__dict__['xref_id']
            try:
                b=Individual.objects.get(gedcom_id__exact=mother_id)
                individual_2_mother_id = b.id
            except Individual.DoesNotExist:
                b = None
        #individual_id
        if father:
            json += '\t{ \n'
            json += '\t\t"model" : "familyroster.Relationship"' + ',\n'
            json += '\t\t"pk" : ' + f'{i+1}' + ',\n'
            json += '\t\t"fields" : {\n'
            json += '\t\t\t"relationship_type" : ' + f'"Child-Father"' + ',\n'
            json += '\t\t\t"individual_1_id" : ' + f'"{individual_1_id}"' + ',\n'
            json += '\t\t\t"individual_1_role_id" : ' + f'"{child}"' + ',\n'
            json += '\t\t\t"individual_2_id" : ' + f'"{individual_2_father_id}"' + ',\n'
            json += '\t\t\t"individual_2_role_id" : ' + f'"Отец"' + '\n'
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
        if mother:
            json += '\t{ \n'
            json += '\t\t"model" : "familyroster.Relationship"' + ',\n'
            json += '\t\t"pk" : ' + f'{i+1}' + ',\n'
            json += '\t\t"fields" : {\n'
            json += '\t\t\t"relationship_type" : ' + f'"Child-Mother"' + ',\n'
            json += '\t\t\t"individual_1_id" : ' + f'"{individual_1_id}"' + ',\n'
            json += '\t\t\t"individual_1_role_id" : ' + f'"{child}"' + ',\n'
            json += '\t\t\t"individual_2_id" : ' + f'"{individual_2_mother_id}"' + ',\n'
            json += '\t\t\t"individual_2_role_id" : ' + f'"Мать"' + '\n'
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
f = open("relationship_father_mother.json", "w", encoding="UTF-8") # creat/open the output file
f.write(json)
f.close() # save