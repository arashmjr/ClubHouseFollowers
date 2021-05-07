from web.utils.Localization import MessageIds, localize


class BaseResponse:
    success: bool
    message_code: int
    message: str

    def __init__(self, success: bool = True, message_code: MessageIds = MessageIds.SUCCESS):
        super().__init__()
        self.message_code = message_code
        self.success = success
        self.message = localize(message_code)

    def serialize(self):
        return {

            'success': self.success,
            'message': self.message,
        }


class BaseError:
    message_code: MessageIds
    message: str

    def __init__(self, message_code: MessageIds):
        self.message_code = message_code
        self.message = localize(message_code)

    def serialize(self):
        return {
            "error": {
                'code': self.message_code,
                'message': self.message,
            }
        }
