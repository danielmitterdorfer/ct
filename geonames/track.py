def index_single(es, params):
    es.percolate(
        index="geonames",
        doc_type="type",
        id=params["id"],
        body=params["body"]
    )
    return 1, "docs"


def register(registry):
    registry.register_runner("index-single", index_single)
