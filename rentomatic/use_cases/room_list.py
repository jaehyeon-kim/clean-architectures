from rentomatic.responses import (
    ResponseTypes,
    ResponseSuccess,
    ResponseFailure,
    build_response_from_invalid_request,
)


def room_list_use_case(repo, request):
    if not request:
        return build_response_from_invalid_request(request)
    try:
        rooms = repo.list(filters=request.filters)
        return ResponseSuccess(rooms)
    except Exception as e:
        return ResponseFailure(ResponseTypes.SYSTEM_ERROR, e)
