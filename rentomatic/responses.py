class ResponseTypes:
    PARAMETERS_ERROR = "ParametersError"
    RESOURCE_ERROR = "ResourceError"
    SYSTEM_ERROR = "SystemError"
    SUCCESS = "Success"


class ResponseSuccess:
    def __init__(self, value=None):
        self.type = ResponseTypes.SUCCESS
        self.value = value

    def __bool__(self):
        return True


class ResponseFailure:
    def __init__(self, type, message):
        self.type = type
        self.message = self._format_message(message)

    def _format_message(self, msg):
        if isinstance(msg, Exception):
            return f"{msg.__class__.__name__}: {msg}"
        return msg

    @property
    def value(self):
        return {"type": self.type, "message": self.message}

    def __bool__(self):
        return False


def build_response_from_invalid_request(invalid_request):
    message = "\n".join(
        ["{}: {}".format(err["parameter"], err["message"]) for err in invalid_request.errors]
    )
    return ResponseFailure(ResponseTypes.PARAMETERS_ERROR, message)
