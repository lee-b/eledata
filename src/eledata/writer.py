import json
from typing import Any, Dict, IO, List, Union

def write_eledown(data: Dict[str, Union[str, List[Dict[str, Any]]]], stream: IO[str], indent: int = 0) -> None:
    def write_args(args: List[Union[str, Dict[str, Any]]], indent: int) -> None:
        for arg in args:
            if isinstance(arg, str):
                stream.write(' ' + arg)
            else:
                stream.write('\n' + ' ' * indent + '{')
                write_eledown(arg, stream, indent + 2)
                stream.write('}')

    stream.write(data['name'])
    write_args(data['args'], indent)


def write(stream, data, file_format):
    if file_format == "json":
        json.dump(data, stream)

    elif file_format == "eld":
        write_eledown(data, stream)

    else:
        raise "Unknown file format"

