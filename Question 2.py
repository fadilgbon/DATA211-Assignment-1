#Question 2: Nested Dictionary from Strings

list_of_classes_for_winter2026_semester = ["Discrete Mathematics", "University Calculus II", 'Introduction to Data Science', "Computer Science for Multidisciplinary Studies II", "Technical Terms of Medicine and the Life Sciences"] #initialixing list of classes
dictionary_of_classes_for_winter2026_semester = {} #initialized empty dictionary
for class_name in list_of_classes_for_winter2026_semester: #loops through the class names in the given list
    length_of_class_name_in_winter2026_semester = len(class_name) #finds out its length
    parity_of_class_name_in_winter2026_semester = "even" if length_of_class_name_in_winter2026_semester % 2 == 0 else "odd" #conditional to check if its length is odd or even
    dictionary_of_classes_for_winter2026_semester[class_name] ={"length":length_of_class_name_in_winter2026_semester, "parity":parity_of_class_name_in_winter2026_semester} #sets the key (classname) equal to the dictionary of its length and parity
print(dictionary_of_classes_for_winter2026_semester)