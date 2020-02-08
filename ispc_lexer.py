# -*- coding: utf-8 -*-
"""
    pygments.lexers.c_cpp
    ~~~~~~~~~~~~~~~~~~~~~

    Lexers for C/C++ w/ OSPRay API calls

    :copyright: Copyright 2006-2019 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import RegexLexer, include, bygroups, using, \
    this, inherit, default, words
from pygments.util import get_bool_opt
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Error

from pygments.lexers.c_cpp import CLexer

__all__ = ['ISPCLexer']

class ISPCLexer(CLexer):
    name = "ISPCLexer"
    filename = ["*.ih", "*.ispc"]
    aliases = ["ispc"]
    mimetypes = ["text/x-ispc"]

    ispc_types = set((
        "int8",
        "int16",
        "int32",
        "int64",
        "bool"
    ))

    ispc_qualifiers = set((
        "uniform",
        "varying",
        "inline",
        "noinline",
        "export"
    ))

    ispc_statements = set((
        "delete",
        "cdo",
        "cfor",
        "cif",
        "cwhile",
        "foreach",
        "foreach_active",
        "foreach_tiled",
        "foreach_unique",
        "in",
        "operator",
        "launch",
        "new",
        "print",
        "soa",
        "sync",
        "task",
        "unmasked"
    ))

    ispc_functions = set((
        "select",
        "popcnt",
        "count_leading_zeros",
        "sign_extend",
        "floatbits",
        "intbits",
        "signbits",
        "extract",
        "select",
        "any",
        "all",
        "none",
        "lanemask"
    ))

    ispc_constants = set((
        "true",
        "false",
        "programCount",
        "programIndex",
        "threadIndex",
        "threadCount",
        "taskIndex0",
        "taskIndex1",
        "taskIndex2",
        "taskCount0",
        "taskCount1",
        "taskCount2"
    ))
    
    def get_tokens_unprocessed(self, text):
        for index, token, value in CLexer.get_tokens_unprocessed(self, text):
            if token is Name:
                if value in self.ispc_types:
                    token = Keyword.Type
                elif value in self.ispc_qualifiers:
                    token = Keyword
                elif value in self.ispc_statements:
                    token = Keyword
                elif value in self.ispc_functions:
                    token = Keyword.Function
                elif value in self.ispc_constants:
                    token = Keyword.Constant
            yield index, token, value

