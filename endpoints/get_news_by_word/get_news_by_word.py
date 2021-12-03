from .get_news_by_word_validator import GetNewsByWordValidator
from .get_news_by_word_flow import GetNewsByWordFlow


class GetNewsByWord:

    def __call__(self, request):

        get_news_by_word_validation = GetNewsByWordValidator()
        get_news_by_word_validation_errors = get_news_by_word_validation(request)
        if get_news_by_word_validation_errors:
            return get_news_by_word_validation_errors

        get_news_by_word_flow = GetNewsByWordFlow()
        return get_news_by_word_flow(request)

            
