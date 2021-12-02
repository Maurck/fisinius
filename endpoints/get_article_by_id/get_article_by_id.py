from .get_article_by_id_validator import GetArticleByIdValidator
from .get_article_by_id_flow import GetArticleByIdFlow


class GetArticleById:

    def __call__(self, request):

        get_article_by_id_validation = GetArticleByIdValidator()
        get_article_by_id_validation_errors = get_article_by_id_validation(request)
        if get_article_by_id_validation_errors:
            return get_article_by_id_validation_errors

        get_article_by_id_flow = GetArticleByIdFlow()
        return get_article_by_id_flow(request)

            
