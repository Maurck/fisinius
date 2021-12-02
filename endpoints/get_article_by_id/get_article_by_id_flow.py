from models.news import News
from utils.utils import json_message
from flask import jsonify


class GetArticleByIdFlow:

    def __call__(self, request):

        news_id = request.args.get('news_id')
        article_obj = News.objects(
            id=news_id
        ).first()

        if article_obj is not None:
            return jsonify({"news": article_obj.to_article_json()})

        return json_message("Noticia no encontrada")
