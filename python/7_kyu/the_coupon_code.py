from datetime import date

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def check_coupon(entered_code, correct_code, current_date, expiration_date):
        print(type(entered_code))
        print(type(correct_code))
        print(current_date)
        print(expiration_date)
        
        print(entered_code == correct_code)
        
        correct_code_check = type(entered_code) == type(correct_code) and (entered_code == correct_code)
        
        
        current_date_list = current_date.split(" ")
        expiration_date_list = expiration_date.split(" ")
        
        current_date_date = date(year=int(current_date_list[2]), month=months[current_date_list[0]], day=int(current_date_list[1][:-1]))
        expiration_date_date = date(year=int(expiration_date_list[2]), month=months[expiration_date_list[0]], day=int(expiration_date_list[1][:-1]))
        
        print(current_date_date)
        print(expiration_date_date)
        
        current_date_check = current_date_date <= expiration_date_date
        print(current_date_check)
        return correct_code_check and current_date_check
