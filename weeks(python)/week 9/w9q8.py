def sort_dict_asc(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

def sort_dict_desc(d):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

my_dict = {
    'apple': 10,
    'banana': 5,
    'cherry': 30,
    'date': 20
}
sorted_dict_asc = sort_dict_asc(my_dict)
print("Sorted Dictionary (Ascending):", sorted_dict_asc)

sorted_dict_desc = sort_dict_desc(my_dict)
print("Sorted Dictionary (Descending):", sorted_dict_desc)
