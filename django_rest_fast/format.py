from typing import Tuple, List


def method_description(docstring: str) -> Tuple[str, str]:
    """Get method name and description by view docstring."""
    docstring = docstring or ''
    doc_lines = [i.strip() for i in docstring.splitlines() if i.strip()]
    method_name = doc_lines[0] if doc_lines else ''
    method_desc = '\n'.join(doc_lines[1:])
    return method_name, method_desc


def method_url(params: List) -> str:
    """Get method url by url parameters"""
    url = '/' + params[0][0][0]
    url = url.replace('%(', '{')
    url = url.replace(')s', '}')
    return url
