from utils.utils import validate_parameters

get_news_by_word_query_schema = {
    'news_word': {
        'type': 'string',
        'nullable': False,
        'required': True,
        'minlength': 0,
        'maxlength': 50
    }
}

class GetNewsByWordValidator:

    def __call__(self, request):
        body_validation_errors = validate_parameters(request.args, get_news_by_word_query_schema)
        return body_validation_errors