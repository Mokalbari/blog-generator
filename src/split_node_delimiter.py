from src.textnode import TextNode, TextType


def split_node_delimiter(old_node: TextNode, delimiter: str, text_type: TextType):
    if old_node.text_type != TextType.TEXT:
        return [old_node]

    new_nodes = []
    sections = old_node.text.split(delimiter)

    if len(sections) % 2 == 0:
        raise Exception("Invalid Markdown: missing closing delimiter")

    for i in range(len(sections)):
        if sections[i] == "":
            continue

        if i % 2 == 0:
            new_nodes.append(TextNode(sections[i], TextType.TEXT))
        else:
            new_nodes.append(TextNode(sections[i], text_type))

    return new_nodes
