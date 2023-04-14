def swap_dict_key_value(d: dict) -> dict:
    output_dict = {}
    for key, value in d.items():
        output_dict[value] = key  # Swap key and value
    return {k: v for k, v in sorted(output_dict.items())}  # Sorted by keys