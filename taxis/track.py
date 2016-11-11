def index_single(es, params):
    es.index(
        index=params["index"],
        doc_type=params["type"],
        body=params["body"][0]
    )
    return 1, "docs"


def register(registry):
    registry.register_runner("index-single", index_single)
