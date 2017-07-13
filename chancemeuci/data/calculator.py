x = [('Arts', {'applied': '2,116', 'admitted': '681', 'enrolled': '127', 'selectivity_rate': '32.20%', 'yield_rate': '18.60%', 'gpa': '3.82', 'verbal': '596', 'math': '594', 'verbal + math': '1190', 'writing': '580', 'verbal + math + writing': '1770'}), ('Drama', {'applied': '545', 'admitted': '170', 'enrolled': '37', 'selectivity_rate': '31.20%', 'yield_rate': '21.80%', 'gpa': '4', 'verbal': '597', 'math': '575', 'verbal + math': '1173', 'writing': '597', 'verbal + math + writing': '1769'}), {'applied': '34,865', 'admitted': '13,452', 'enrolled': '3,060', 'selectivity_rate': '38.60%', 'yield_rate': '22.70%', 'gpa': '3.95', 'verbal': '579', 'math': '658', 'verbal + math': '1237', 'writing': '581', 'verbal + math + writing': '1818'}, {'applied': '20150', 'admitted': '10374', 'enrolled': '1706', 'selectivity_rate': '51.50%', 'yield_rate': '16.40%'}, {'applied': '25,104', 'admitted': '11,334', 'enrolled': '2,373', 'selectivity_rate': '45.10%', 'yield_rate': '20.90%', 'gpa': '4.02', 'verbal': '608', 'math': '649', 'verbal + math': '1256', 'writing': '605', 'verbal + math + writing': '1861'}]

def calculate(l: list) -> float:
    total_percentage = 0
    for data_structure in l:
        if type(data_structure) == tuple:
            for element in data_structure:
                print(type(element))
                if type(element) == dict:
                    total_percentage += float(element['selectivity_rate'].strip('%'))
                    print(total_percentage)
        elif type(data_structure) == dict:
            total_percentage += float(data_structure['selectivity_rate'].strip('%'))
            print(total_percentage)
    return total_percentage/len(l)

print(calculate(x))