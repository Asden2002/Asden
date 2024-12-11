def find_common_participants(group1, group2, delimiter=','):

    group1_list = group1.split(delimiter)
    group2_list = group2.split(delimiter)

    common_participants = set(group1_list).intersection(group2_list)

    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print("Общие участники:", common)

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"
common = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", common)