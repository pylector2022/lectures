from .bar import *
from .foo import *

CONSTANT = 1

def super_import_func():
    import sub
    return sub.boo.var1

import peewee

db = peewee.SqliteDatabase('filename')

var2 = super_import_func()

__all__ = bar.__all__ + foo.__all__ + [var2, db]
