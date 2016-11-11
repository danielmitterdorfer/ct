def index_single(es, params):
    es.create(
        index=params["index"],
        doc_type=params["type"],
        id=params["id"],
        body=params["body"][0]
    )
    return 1, "docs"


def register(registry):
    registry.register_runner("index-single", index_single)
