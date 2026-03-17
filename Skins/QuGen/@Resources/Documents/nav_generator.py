import os
import re
os.system('cls')
os.chdir(os.getcwd())

def camel_case_split(camel_case_string):
    pattern = r'(?<=[a-z])(?=[A-Z])'
    words = re.sub(pattern, ' ', camel_case_string)
    return words

def get_file_name_without_ext(file_name):
    return file_name.split('.')[0]

def remove_duplicates(list):
    seen = set()
    unique_list = []
    for item in list:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list

def get_sub_page_titles(list, sub_string):
    initial_list = [
        get_file_name_without_ext(item)
        for item in list
        if sub_string in item
    ]
    initial_list.remove(sub_string)

    for i in range(len(initial_list)):
        initial_list[i] = initial_list[i].replace(sub_string + '-', '')

    result_list = [
        item
        for item in initial_list
        if '-' not in item
    ]

    return result_list

if __name__ == "__main__":
    file_name = 'Home-ResourceDescriptions-Resources-Scripts-Util'

    file_name_split = file_name.split('-')

    file_name_iteration = 'Home'
    for word in file_name_split:
        if word != 'Home':
            file_name_iteration += '-' + word
        if word != file_name_split[-1]:
            print('[' + camel_case_split(word) + '](/stevehsudrawing/QuGen/wiki/' + file_name_iteration + ') >')
        else:
            print('[**' + camel_case_split(word) + '**](/stevehsudrawing/QuGen/wiki/' + file_name_iteration + ')')
    print()

    sub_files_list = os.listdir('./@Resources/Documents')
    sub_files_list_flitted = get_sub_page_titles(sub_files_list, file_name)
    for item in sub_files_list_flitted:
        print('- [' + camel_case_split(item) + '](/stevehsudrawing/QuGen/wiki/' + file_name + '-' + item + ')')
    print()
