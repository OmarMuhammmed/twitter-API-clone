
def error_messages(type, field):
    if type == "blank":
       
        return f"The {field} field must not be blank!"
    if type == "required":
        
        return f"The {field} field is required!"

def response_messages(lang: str = None):
    return {
        "PASSWORD_AND_PASSWORD_CONFIRM_NOT_MATCH": "Password and confirmation password do not match!",
        "TOKEN_IS_NOT_VALID_OR_HAS_EXPIRED": "The token is not valid or has expired!",
        "EMAIL_ADDRESS_DOES_NOT_EXIST": "The e-mail address does not exist!",
        "USER_DOES_NOT_EXIST": "The user does not exist!",
        "CONFIRM_YOUR_ADDRESS_EMAIL": "Please confirm your email address!",
        "EMAIL_OR_PASSWORD_IS_NOT_VALID": "The email or the password is not valid!",
        "MISSING_PARAMETER": "missing parameter",
        "SOMETHING_WENT_WRONG": "Something went wrong!",
        "YOU_ARE_NOT_AUTHORIZED_FOR_THIS_ACTION": "You are not authorized for this action.",
        "ENTER_A_VALID_EMAIL_ADDRESS": "Please enter a valid email address.",
        "USER_WITH_THIS_EMAIL_ADDRESS_ALREADY_EXISTS": "A user with this email address already exists.",
        "INVALID_PASSWORD": "The password must contain at least 8 characters, at least one upper and lower case letter, one number and one special character.",
        "COMMENT_NOT_FOUND": "Comment not found!",
        "POST_NOT_FOUND": "Post not found!",
        "MESSAGE_OR_IMAGE_FIELD_MUST_NOT_EMPTY.": "The message or image field must not be empty.",
        "BODY_OR_IMAGE_FIELD_MUST_NOT_EMPTY": "The body or image field must not be empty.",
        "FILE_SIZE_TOO_LARGE": "File size too large. Got 13558755. Maximum is 10485760",
        
        "SUCCESSFUL_REGISTRATION": "Successful registration!",
        "SUCCESSFUL_ACTIVATION_ACCOUNT": "Your account has been successfully created and activated!",
        "LOGIN_SUCCESS": "Successful login!",
        "PASSWORD_CHANGED_SUCCESSFULLY": "The password has been successfully changed!",
        "PASSWORD_RESET_SUCCESSFULLY": "Password reset successful!",
        "PASSWORD_RESET_LINK_SEND": "The password reset link has been sent. Please check your email.",
        "LOGOUT_SUCCESSFULLY": "Successful logout!",
    }


LANG = "en"

res = response_messages(LANG)