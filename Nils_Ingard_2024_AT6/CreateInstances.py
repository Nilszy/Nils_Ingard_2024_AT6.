from Question5 import UserInputValidator

test_list1 = ["15", "-15", "1", "20", "abc", "543"]
test_list2 = ["99", "20", "ab", "-11", "-abe"]

instance1 = UserInputValidator()
valid_integers1 = instance1.validate_positive_integers(test_list1)
instance1.validation_message(valid_integers1)

instance2 = UserInputValidator()
valid_integers2 = instance2.validate_positive_integers(test_list2)
instance2.validation_message(valid_integers2)