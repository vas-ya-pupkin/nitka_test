from enum import Enum
from typing import Iterator

import yaml

max_file_size = 1024 * 1024  # 1 MB


class FieldType(str, Enum):
    """Config file field types to extract"""
    SOURCE = "source"
    TARGET = "target"


def process_service_config(config: bytes) -> dict:
    """Extract significant data from the config file"""
    try:
        yml: dict = yaml.safe_load(config)
    except yaml.YAMLError:
        raise ValueError

    if "job_step" not in yml:
        raise ValueError

    data = yml["job_step"]
    step_name = data.get("step_name")
    service_name = data.get("service_name")
    if not step_name or not service_name:
        raise ValueError

    return {
        "name": f"{service_name}.{step_name}",
        "service_config": data.get("service_config") or {},
        "source_tables": extract_table_names(data, FieldType.SOURCE),
        "target_tables": extract_table_names(data, FieldType.TARGET),
    }


def extract_table_names(data: dict, field_type: FieldType) -> set[str]:
    """Extract source or target table names from the config file"""
    result = set()
    for value in _find_values(data, f"{field_type.value}_table"):
        if isinstance(value, dict) and (name := value.get("table_name")):
            result.add(name)
        elif isinstance(value, str):
            result.add(value)
    return result


def validate_file_size(file) -> None:
    """Validate the size of the uploaded file"""
    if file.content_length > max_file_size:
        raise ValueError


def _find_values(data: dict | list, key_to_find: str) -> Iterator[str | dict]:
    """Find all values in a dict-like structure by key recursively"""
    if isinstance(data, dict):
        for key, value in data.items():
            if key == key_to_find:
                yield value
            else:
                yield from _find_values(value, key_to_find)
    elif isinstance(data, list):
        for item in data:
            yield from _find_values(item, key_to_find)
