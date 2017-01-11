import random
import uuid
#import cProfile

KNOWN_IDS = []

#
# def index(es, **kwargs):
#     # print("index: [%s]" % str(kwargs))
#     es.index(kwargs)
#
#
# def update(es, **kwargs):
#     # print("update: [%s]" % str(kwargs))
#     es.index(kwargs)
#
#
# def delete(es, **kwargs):
#     # print("delete: [%s]" % str(kwargs))
#     es.delete(kwargs)


def index_single(es, params):
    global KNOWN_IDS
    op_type = random.randint(0, 2)
    if op_type == 0 or not KNOWN_IDS:
        id = uuid.uuid4()
        KNOWN_IDS.append(id)
        es.index(
            index=params["index"],
            doc_type=params["type"],
            id=id,
            op_type="create",
            body={
                "pickup_datetime": "2015-01-01 00:34:42",
                "trip_type": str(random.randint(0, 10)),
                "passenger_count": random.randint(0, 6)
            })
    elif op_type == 1:
        id = random.choice(KNOWN_IDS)
        es.index(
            index=params["index"],
            doc_type=params["type"],
            id=id,
            op_type="index",
            body={
                "pickup_datetime": "2015-01-01 00:34:42",
                "trip_type": str(random.randint(0, 10)),
                "passenger_count": random.randint(0, 6)
            })
    else:
        id = KNOWN_IDS.pop()
        es.delete(
            index=params["index"],
            doc_type=params["type"],
            id=id,
        )
    return 1, "docs"


def register(registry):
    registry.register_runner("index-single", index_single)


# def foo():
#     for i in range(0, 100000):
#         index_single(None, params={
#             "index": "taxis",
#             "type": "type"
#         })
#
#
# if __name__ == '__main__':
#     cProfile.run('foo()')
