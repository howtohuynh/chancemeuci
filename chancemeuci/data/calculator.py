def calculate(l: list) -> float:
    percentage_list = []
    for dictionary in l:
        percentage_list.append(float(dictionary['selectivity_rate'].strip('%')))
    percentage_list.sort()
    return [percentage_list, sum(percentage_list)/len(percentage_list)]

