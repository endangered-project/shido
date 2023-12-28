from django import template

register = template.Library()


@register.filter
def json_to_list(json_value):
    """
    Convert JSON to list with key and value

    Example:
    {
        "key1": "value1",
        "key2": "value2"
    }

    will be converted to
    [
        {
            "key": "key1",
            "value": "value1"
        },
        {
            "key": "key2",
            "value": "value2"
        }
    ]
    :param json_value: JSON value
    :return: Dictionary
    """
    if json_value is None:
        return []
    if type(json_value) is not dict:
        return []
    result = []
    for key, value in json_value.items():
        result.append({
            'key': key,
            'value': value
        })
    return result
