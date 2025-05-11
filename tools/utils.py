from tools.custom_types import ConlluDbRow, Node


def get_verb_node(word: str, row: ConlluDbRow) -> Node:

    for _, node in row["tree"].nodes.items():
        if node["word"] == word and node["ctag"] == "VERB":
            return node

    return None


def get_all_grammar(node: Node) -> dict[str, str]:

    if node["feats"] == "_":
        return dict()

    result = {
        k: v
        for k, v
        in map(
            lambda pair: pair.split("="),
            node["feats"].split("|")
        )
    }
    result["POS"] = node["ctag"]

    return result
