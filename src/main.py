from textnode import TextNode, TextType


def main():
    textnode = TextNode("Coucou", TextType.PLAIN, "http://cool.fr")

    print(textnode)


if __name__ == "__main__":
    main()
