from typing import Iterable, List, Optional, Union

from penman.tree import Tree, is_atomic
from penman.types import BasicTriple


def format(
    tree: Tree,
    indent: Union[int, None] = -1,
    compact: bool = False,
) -> str:
    """
    Format *tree* into a PENMAN string.

    Args:
        tree: a Tree object
        indent: how to indent formatted strings
        compact: if ``True``, put initial attributes on the first line
    Returns:
        the PENMAN-serialized string of the Tree *t*
    Example:
        >>> import penman
        >>> print(penman.format(
        ...     ('b', [('/', 'bark-01'),
        ...            (':ARG0', ('d', [('/', 'dog')]))])))
        (b / bark-01
           :ARG0 (d / dog))
    """
    pass


def format_triples(triples: Iterable[BasicTriple], indent: bool = True) -> str:
    """
    Return the formatted triple conjunction of *triples*.

    Args:
        triples: an iterable of triples
        indent: how to indent formatted strings
    Returns:
        the serialized triple conjunction of *triples*
    Example:
        >>> import penman
        >>> g = penman.decode('(b / bark-01 :ARG0 (d / dog))')
        >>> print(penman.format_triples(g.triples))
        instance(b, bark-01) ^
        ARG0(b, d) ^
        instance(d, dog)

    """
    delim = ' ^\n' if indent else ' ^ '
    # need to remove initial : on roles for triples
    conjunction = [
        f'{role.lstrip(":")}({source}, {target})'
        for source, role, target in triples
    ]
    return delim.join(conjunction)


def _format_node(
    node,
    indent: Optional[int],
    column: int,
    vars: set,
) -> str:
    """
    Format tree *node* into a PENMAN string.
    """
    pass


def _format_edge(edge, indent, column, vars):
    """
    Format tree *edge* into a PENMAN string.
    """
    pass
