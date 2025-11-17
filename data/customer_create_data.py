class CreateCustomerData():
    
    #Valid demographic infos
    VALID_FIRST_NAME = "Selami"
    VALID_LAST_NAME = "Göngör"
    VALID_DATE_OF_BIRTH = "23/12/1990"
    GENDER = "Male"
    VALID_NAT_ID = "55544466678"

    #Invalid demographic infos
    INVALID_FIRST_NAME = "A"
    INVALID_LAST_NAME = "B"
    INVALID_FATHER_NAME = ""
    INVALID_MOTHER_NAME = ""
    INVALID_DATE_OF_BIRTH = "17/11/2010" #Younger than 16

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
    VALID_MOBILE_PHONE = ""
    VALID_EMAIL = ""

    #Invalid contact medium infos
    INVALID_MOBILE_PHONE = ""
    INVALID_EMAIL = ""

    #Empty contact medium infos
    EMPTY_MOBILE_PHONE = ""
    EMPTY_EMAIL = ""

    #Cancel Redirection URL
    DEMOGRAPHIC_CANCEL_REDIRECTION_URL = "http://localhost:4200/b2c"





