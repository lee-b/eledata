import json
import re
from typing import Any, Dict, List, Tuple, Union

def parse_eledown(text: str) -> Dict[str, Union[str, List[Dict[str, Any]]]]:
    def parse_arguments(text: str) -> List[Union[str, Dict[str, Any]]]:
        result = []
        argument_start = 0
        depth = 0

        for idx, char in enumerate(text):
            if char == '{':
                if depth == 0:
                    if idx > argument_start:
                        result.append(text[argument_start:idx].strip())
                    argument_start = idx + 1
                depth += 1
            elif char == '}':
                depth -= 1
                if depth == 0:
                    result.append(parse_command(text[argument_start:idx]))
                    argument_start = idx + 1

        if argument_start < len(text):
            result.append(text[argument_start:].strip())

        return result

    def parse_command(text: str) -> Dict[str, Any]:
        command_start = text.find('{')
        command_end = text.find(' ')

        if command_start != -1 and (command_end == -1 or command_start < command_end):
            command_name = text[:command_start].strip()
            arguments = parse_arguments(text[command_start:])
        else:
            command_name = text[:command_end].strip()
            remaining_text = text[command_end:].strip()
            if '{' in remaining_text:
                arguments = parse_arguments(remaining_text)
            else:
                arguments = [remaining_text]

        return {'name': command_name, 'args': arguments}

    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return parse_command(text)


def read(stream, file_type):
    if file_type == "json":
        return json.load(stream)

    elif file_type == "eld":
        return parse_eledown(stream.read())

    else:
        raise "Unknown file format"

