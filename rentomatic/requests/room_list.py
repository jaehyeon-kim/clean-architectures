class RoomListValidRequest:
    def __init__(self, filters=None):
        self.filters = filters

    def __bool__(self):
        return True


class RoomListInvalidRequest:
    def __init__(self):
        self.errors = []

    def add_error(self, parameter, message):
        self.errors.append({"parameter": parameter, "message": message})

    def has_errors(self):
        return len(self.errors) > 0

    def __bool__(self):
        return False


def build_room_list_request(filters=None):
    accepted_filters = ["code__eq", "price__eq", "price__lt", "price__gt"]
    invalid_req = RoomListInvalidRequest()

    if filters is not None:
        if not isinstance(filters, dict):
            invalid_req.add_error("filters", "Is not iterable")
            return invalid_req

        for key, _ in filters.items():
            if key not in accepted_filters:
                invalid_req.add_error("filters", f"Key {key} cannot be used")

        if invalid_req.has_errors():
            return invalid_req

    return RoomListValidRequest(filters)
