path = r"C:\Python\Python38\Django\familysite\ca1z66_78236416fprf45ca4e51z3.ged"
json = ''
json += '[ \n'
c = Relationship.objects.all()
d = Relationship.objects.all()
list_for_checks = []
for i in c:
    if i.individual_1_role == "Дочь" or i.individual_1_role == "Сын":
        role1=i.individual_1_role
        for i2 in d:
            if i2.individual_1_role == "Дочь" or i2.individual_1_role == "Сын":
                role2=i2.individual_1_role
                a=i.individual_1_id_id
                b=i2.individual_1_id_id
                if i.individual_2_id_id == i2.individual_2_id_id and i.individual_1_id_id != i2.individual_1_id_id and (b, a) not in list_for_checks and (a, b) not in list_for_checks:
                    list_for_checks.append((a, b))
                    json += '\t{ \n'
                    json += '\t\t"model" : "familyroster.Relationship"' + ',\n'
                    json += '\t\t"pk" : ' + f'"x"' + ',\n'
                    json += '\t\t"fields" : {\n'
                    json += '\t\t\t"relationship_type" : ' + f'"Siblings"' + ',\n'
                    json += '\t\t\t"individual_1_id" : ' + f'"{i.individual_1_id_id}"' + ',\n'
                    if role1 == "Дочь":
                        json += '\t\t\t"individual_1_role" : ' + f'"Сестра"' + ',\n'
                    if role1 == "Сын":
                        json += '\t\t\t"individual_1_role" : ' + f'"Брат"' + ',\n'
                    json += '\t\t\t"individual_2_id" : ' + f'"{i2.individual_1_id_id}"' + ',\n'
                    if role2 == "Дочь":
                        json += '\t\t\t"individual_2_role" : ' + f'"Сестра"' + '\n'
                    if role2 == "Сын":
                        json += '\t\t\t"individual_2_role" : ' + f'"Брат"' + '\n'
                    json += '\t\t}\n'
                    json += '\t},\n'
json += ']'
f = open("relationship_siblings.json", "w", encoding="UTF-8") # creat/open the output file
f.write(json)
f.close() # save
