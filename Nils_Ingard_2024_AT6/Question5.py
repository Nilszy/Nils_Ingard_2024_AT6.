class UserInputValidator:
    def __init__(self):
        #Initializes the validator object
        pass

    def validate_positive_integers(self, input_list):
        #Empty list to store integers
        valid_integers = []

        for item in input_list:
            #Check if the item is a positive integer 
            if item.isdigit() and int(item) > 0:
                valid_integers.append(int(item))
        
        return valid_integers

    def validation_message(self, valid_integers):
        print(f'Valid integers: {len(valid_integers)}')
        #Display message