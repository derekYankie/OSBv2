
from inspect import getmembers, ismethod
from types import FunctionType


def get_pvc_name(workspace_id):
    return f"workspace-{workspace_id}"


disallowed_class_types = ["BaseQuery", "type", "registry", "MetaData"]


def row2dict(obj):
    disallowed_names = {name for name, value in getmembers(
        type(obj)) if isinstance(value, FunctionType)}
    result = {}
    for name in dir(obj):
        if name[0] != "_" and name not in disallowed_names and hasattr(obj, name):
            val = getattr(obj, name)
            if not ismethod(val):
                clas = val.__class__.__name__
                if clas == "InstrumentedList":
                    val = list(row2dict(r) for r in val)
                if clas not in disallowed_class_types:
                    result.update({name: val})
    return result
