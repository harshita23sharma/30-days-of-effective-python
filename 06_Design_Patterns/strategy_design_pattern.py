"""
Strategy Design Pattern allows: 
An algorithm is composed of both Higher level parts & lower level parts

It enables the exact behaviour of a system to be selected at runtime
At runtime you specify the actual details, you feed them into whatever component
is able to consume them and then that component uses its high level approach with
your low level strategy in order to do something

"""

from abc import ABC
from enum import Enum, auto


class OutputFormat(Enum):
    MARKDOWN = auto()
    HTML = auto()


# not required but a good idea
# Abstract Base class/ Interface : KInd of Blueprint
class ListStrategy(ABC):
    def start(self, buffer): pass

    def end(self, buffer): pass

    def add_list_item(self, buffer, item): pass


class MarkdownListStrategy(ListStrategy):

    # We don't require star and end, so we just need to override the add_list_item
    # We only implement the methods which we require
    def add_list_item(self, buffer, item):
        buffer.append(f' * {item}\n')


class HtmlListStrategy(ListStrategy):

    def start(self, buffer):
        buffer.append('<ul>\n')

    def end(self, buffer):
        buffer.append('</ul>\n')

    def add_list_item(self, buffer, item):
        buffer.append(f'  <li>{item}</li>\n')


class TextProcessor:
    def __init__(self, list_strategy=HtmlListStrategy()):
        self.buffer = []
        self.list_strategy = list_strategy

    def append_list(self, items):
        self.list_strategy.start(self.buffer)
        for item in items:
            self.list_strategy.add_list_item(
                self.buffer, item
            )
        self.list_strategy.end(self.buffer)

    # Get the strategy using Enum class
    def set_output_format(self, format):
        if format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownListStrategy()
        elif format == OutputFormat.HTML:
            self.list_strategy = HtmlListStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return ''.join(self.buffer)


if __name__ == '__main__':
    items = ['foo', 'bar', 'baz']

    tp = TextProcessor()
    tp.set_output_format(OutputFormat.MARKDOWN)
    tp.append_list(items)
    print(tp)

    tp.set_output_format(OutputFormat.HTML)
    tp.clear()
    tp.append_list(items)
    print(tp)