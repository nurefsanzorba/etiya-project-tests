class CreateCustomerData():
    
    #Valid demographic infos
    VALID_FIRST_NAME = "Selami"
    VALID_LAST_NAME = "Göngör"
    VALID_DATE_OF_BIRTH = "12/12/1990" # MM/dd/YYYY format
    VALID_NAT_ID = "55544466678"

    #Gender Options
    GENDER_FEMALE = "Female"
    GENDER_MALE = "Male"
    GENDER_NOT_SAY = "Prefer not to say"

    #Gender List
    GENDER_LIST = [GENDER_FEMALE, GENDER_MALE, GENDER_NOT_SAY]

    #Invalid demographic infos
    INVALID_FIRST_NAME = "A"
    INVALID_LAST_NAME = "B"
    INVALID_FATHER_NAME = ""
    INVALID_MOTHER_NAME = ""
    INVALID_DATE_OF_BIRTH = "12/11/2010" #Younger than 16 MM/dd/YYYY format
    INVALID_TEN_DIGIT_NAT_ID = "1111111110"
    INVALID_TWELVE_DIGIT_NAT_ID = "111111111000"

    #Enable Controls
    IS_ENABLED_TRUE = True
    IS_ENABLED_FALSE = False

    #Valid address infos
    VALID_TITLE = "Home"
    VALID_CITY = "İstanbul"
    VALID_STREET = "İstiklal"
    VALID_HOUSE_NO = "10"
    VALID_DESCRIPTION = "Yakın Taksim"

    #Invalid address infos
    EMPTY_TITLE = ""
    EMPTY_CITY = ""
    EMPTY_STREET = ""
    EMPTY_HOUSE_NO = ""
    EMPTY_DESCRIPTION = ""

    #Valid contact medium infos
    VALID_MOBILE_PHONE = "05554443322"
    VALID_EMAIL = "test@mail.com"

    #Invalid contact medium infos
    INVALID_LESS_TEN_MOBILE_PHONE = "5553311"
    INVALID_MORE_FIFTEEN_MOBILE_PHONE = "6665554443332221"
    INVALID_EMAIL = "test@@mail.com"

    #Empty contact medium infos
    EMPTY_MOBILE_PHONE = ""
    EMPTY_EMAIL = ""

    #Optional fields on contact medium infos
    HOME_PHONE = "3332211"
    FAX = "1112233"

    #Cancel redirection URL
    DEMOGRAPHIC_CANCEL_REDIRECTION_URL = "http://localhost:4200/b2c"

    #Demographic info errors
    ERROR_FIRST_NAME = "First Name is required (2-20 characters)"
    ERROR_LAST_NAME = "Last Name is required (2-20 characters)"
    ERROR_NAT_ID = "NAT ID must be an 11-digit number."
    ERROR_AGE = "Customer must be at least 16 years old."

    #Address info errors
    ERROR_ADDRESS_TITLE = "Address Title is required."
    ERROR_STREET = "Street is required."
    ERROR_HOUSE_NO = "House/Flat Number is required."
    ERROR_DESCRIPTION = "Address Description is required."

    #Contact Medium errors
    ERROR_MOBILE_PHONE = "Please enter a valid mobile phone number (including area code)"
    ERROR_EMAIL = "E-mail must be valid e-mail address!"

    #Already exists customer error
    ALREADY_EXIST_CUSTOMER_ERROR = "Customer with this national identity exists."

    #Already exists customer nat ID
    EXIST_NAT_ID = "11122233344"






