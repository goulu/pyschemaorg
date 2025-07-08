import inspect
import td

tds = {}
for name, obj in inspect.getmembers(td):
    if inspect.isclass(obj):
        tds[name] = obj


def factory(row: dict) -> td.Thing:
    """
    Factory function to create an instance of a TypedDict class by its name.    
    """
    type = row.get('@type')
    if type not in tds:
        raise ValueError(f"TypedDict class '{name}' not found in td module.")

    cls = tds[type]

    return cls(row)
