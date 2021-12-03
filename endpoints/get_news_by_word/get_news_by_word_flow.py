import re
from models.news import News
from utils.utils import json_message
from flask import jsonify


class GetNewsByWordFlow:

    def __call__(self, request):

        news_word = request.args.get('news_word')

        regex = re.compile(f'.*{news_word}.*', re.IGNORECASE)

        news_list = News.objects(
            title=regex
        )

        if len(news_list) > 0:
            news_jsons_list = []
            news_jsons_list = list(map(lambda news_obj: news_obj.to_news_json(), news_list))
            return jsonify({"news": news_jsons_list})
        return jsonify({"msg": "No hay noticias"})
