from utils.utils import validate_parameters

get_news_body_schema = {}

class GetNewsValidator:

    def __call__(self, request):
        body_validation_errors = validate_parameters(request.form, get_news_body_schema)
        return body_validation_errors