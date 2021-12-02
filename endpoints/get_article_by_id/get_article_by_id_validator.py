from utils.utils import validate_parameters

get_article_by_id_query_schema = {
    'news_id': {
        'type': 'string',
        'nullable': False,
        'required': True,
        'minlength': 24,
        'maxlength': 24
    }
}

class GetArticleByIdValidator:

    def __call__(self, request):
        body_validation_errors = validate_parameters(request.args, get_article_by_id_query_schema)
        return body_validation_errors