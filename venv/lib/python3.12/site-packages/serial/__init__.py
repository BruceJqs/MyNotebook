"""
`serial` is an object serialization/deserialization library intended to facilitate authoring of API models which are
readable and introspective, and to expedite code and data validation and testing. `serial` supports JSON, YAML, and
XML.
"""

from __future__ import nested_scopes, generators, division, absolute_import, with_statement, \
   print_function, unicode_literals

from . import utilities, abc, model, marshal, errors, properties, meta, hooks, test, request
