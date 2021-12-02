from models.news import News
from flask import jsonify


class GetNewsFlow:

    def __call__(self, request):

        from_index = request.args.get('from', type=int, default=0)
        limit_index = request.args.get('limit', type=int, default=0)
        news_list = News.objects().limit(limit_index).skip(from_index)

        if len(news_list) > 0:
            news_jsons_list = []
            news_jsons_list = list(map(lambda news_obj: news_obj.to_json(), news_list))
            return jsonify({"news": news_jsons_list})
        return jsonify({"msg": "No hay noticias"})
