from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    """Return an HTTP response with the text "Django".

    Parameters
    ----------
    request : HttpRequest
        The HTTP request object.

    Returns
    -------
    HttpResponse
        An HTTP response with the text "Django".
    """
    return HttpResponse("Django")
