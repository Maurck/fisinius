from .get_news_validator import GetNewsValidator
from .get_news_flow import GetNewsFlow


class GetNews:

    def __call__(self, request):

        get_news_validation = GetNewsValidator()
        get_news_validation_errors = get_news_validation(request)
        if get_news_validation_errors:
            return get_news_validation_errors

        get_news_flow = GetNewsFlow()
        return get_news_flow()

            
