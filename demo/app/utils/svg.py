import hashlib
import io
import logging
import re
from xml.etree import ElementTree

import requests

from django.core.files import File

from app.exceptions import PFPApiBadInputError
from app.models import SchemaItemsID, Schema
from settings.settings import PFP_API_URL_GET_SCHEMA

logger = logging.getLogger(__name__)

ElementTree.register_namespace('', 'http://www.w3.org/2000/svg')


def process_new_svg(file_name) -> Schema:
    """Process and save new schema."""
    logger.debug('processing new schema')

    response = requests.get(PFP_API_URL_GET_SCHEMA(schema_id=file_name), stream=True)
    if not response.ok:
        raise PFPApiBadInputError(response.status_code, response.reason)

    svg = fix_svg(response.text)
    schema_inst = Schema.init_with_content(file_name, svg)
    schema_inst.save()

    return schema_inst


def fix_svg(svg_content: str) -> File:
    """Return file object with fixed svg content."""
    tree = ElementTree.fromstring(svg_content)
    tree = ElementTree.ElementTree(tree)

    ids = []

    for element in tree.findall('.//*[@id]'):
        # pure algorithm - skipping IDs in referencing attributes.
        id_ = element.attrib['id']
        id_cleaned = map_original_id(id_)

        element.set('id', id_cleaned)
        ids.append(SchemaItemsID(id_original=id_, id_mapped=id_cleaned))

    SchemaItemsID.objects.bulk_create_or_update(ids)

    svg = io.BytesIO()
    tree.write(svg, encoding='UTF-8')
    return File(svg)


def map_original_id(id_: str):
    return f'{fix_svg_item_id(id_)}_{hash_string(id_)[:8]}'


def fix_svg_item_id(id_: str):
    """Все элементы кроме чисел и букв подменяются на `_`

    Почему-то точка (.) и дефис (-) не обрабатываются в JS.
    """
    id_ = re.sub(r'[^\w0-9]+', '_', id_)
    return id_.lower()


def hash_string(string) -> str:
    return hashlib.sha224(string.encode('utf-8')).hexdigest()
