import csv

def list_to_dict(l1: list, l2: list) -> dict:
    result = {}
    for index in range(len(l2)):
        result[l2[index]] = l1[index]
    return result

def csv_to_dict(file: str, dictKeyList: list) -> dict:
    result = {}
    open_file = open(file, 'r')
    read_file = csv.reader(open_file)
    csv_format = next(read_file) #skips first line (header) in a .csv file
    if csv_format[1] in ['gender', 'ethnicity', 'major']:
        for line in read_file:
            if line[0] not in result:
                result[line[0]] = {}
                result[line[0]][line[1]] = list_to_dict(line[2:], dictKeyList)
            else:
                result[line[0]][line[1]] = list_to_dict(line[2:], dictKeyList)
    else:
        for line in read_file:
            if line[0] not in result:
                result[line[0]] = {}
                result[line[0]] = list_to_dict(line[1:], dictKeyList)
            else:
                result[line[0]] = list_to_dict(line[1:], dictKeyList)
    return result

# appliedList = ['applied', 'admitted', 'enrolled', 'selectivity_rate', 'yield_rate']
# satList = ['verbal', 'math', 'verbal + math', 'writing', 'verbal + math + writing']
# gpaList = ['gpa']
# highschoolList = ['admitted']
#
# school = csv_to_dict('csv_files/school.csv', appliedList)
# major = csv_to_dict('csv_files/major.csv', appliedList)
# gender = csv_to_dict('csv_files/gender.csv', appliedList)
# high_school = csv_to_dict('csv_files/high_school.csv', highschoolList)
# residency = csv_to_dict('csv_files/residency.csv', appliedList)
# ethnicity = csv_to_dict('csv_files/ethnicity.csv', appliedList)
# print(ethnicity)
# school_gender = csv_to_dict('csv_files/school_gender.csv', appliedList)
# school_ethnicity = csv_to_dict('csv_files/school_ethnicity.csv', appliedList)
#
# gpa_school = csv_to_dict('csv_files/gpa_school.csv', gpaList)
# gpa_major = csv_to_dict('csv_files/gpa_major.csv', gpaList)
# gpa_gender = csv_to_dict('csv_files/gpa_gender.csv', gpaList)
# gpa_ethnicity = csv_to_dict('csv_files/gpa_ethnicity.csv', gpaList)
# gpa_school_gender = csv_to_dict('csv_files/gpa_school_gender.csv', gpaList)
# gpa_school_ethnicity = csv_to_dict('csv_files/gpa_school_ethnicity.csv', gpaList)
#
# sat_school = csv_to_dict('csv_files/sat_school.csv', satList)
# sat_major = csv_to_dict('csv_files/sat_major.csv', satList)
# sat_gender = csv_to_dict('csv_files/sat_gender.csv', satList)
# sat_ethnicity = csv_to_dict('csv_files/sat_ethnicity.csv', satList)
# sat_school_gender = csv_to_dict('csv_files/sat_school_gender.csv', satList)
# sat_school_ethnicity = csv_to_dict('csv_files/sat_school_ethnicity.csv', satList)
