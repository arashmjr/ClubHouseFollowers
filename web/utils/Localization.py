from enum import IntEnum


class MessageIds(IntEnum):

    ERROR_INSUFFICIENT_ACCOUNT_BALANCE = -9

    ERROR_BAD_JSON = -8

    ERROR_INVALID_VERFY_CODE = -7

    ERROR_TOKEN_NOT_VALID = -6

    ERROR_BAN_USER = -5

    ERROR_NOT_AUTHORIZED = -4

    ERROR_INVALID_PROPERTY = -3

    ERROR_WRONG_EMAIL_FROMAT = -2

    ERROR_NOT_FOUND = -1

    SUCCESS = 1



strings = {MessageIds.SUCCESS: "Action successfully done!",
           MessageIds.ERROR_NOT_FOUND: "Method you requested not found!",
           MessageIds.ERROR_BAD_JSON: "The json you have sent is not in valid format, please check your request and try again.",
           MessageIds.ERROR_WRONG_EMAIL_FROMAT: "The email has wrong format.",
           MessageIds.ERROR_INVALID_PROPERTY: "One or some of the properties you send are not in valid format.",
           MessageIds.ERROR_NOT_AUTHORIZED: "There was a problem authenticating your request. This could be due to missing or incorrect authentication credentials. This may also be returned in other undefined circumstances.",
           MessageIds.ERROR_BAN_USER: "Access to this server has been restricted due to excessive load.",
           MessageIds.ERROR_TOKEN_NOT_VALID: "Access Token is not valid or has expired.",
           MessageIds.ERROR_INVALID_VERFY_CODE: "The verification code is invalid or expired.",
           MessageIds.ERROR_INSUFFICIENT_ACCOUNT_BALANCE: "order size is bigger than your account balance."

           }


def localize(messageId: MessageIds) -> str:
    return strings[messageId]
