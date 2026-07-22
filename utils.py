from typing import List, Any


def flatten(lst: List[Any]) -> List[Any]:
    """Flatten a nested list into a flat list.

    Args:
        lst (List[Any]): A nested list.

    Returns:
        List[Any]: A flat list containing all the elements.
    """
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


def deduplicate(lst: List[Any]) -> List[Any]:
    """Remove duplicates from a list while maintaining order.

    Args:
        lst (List[Any]): A list that may contain duplicates.

    Returns:
        List[Any]: A list with duplicates removed.
    """
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]