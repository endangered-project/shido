from django.db import models


class Class(models.Model):
    """
    Class that will contain instances
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Instance(models.Model):
    """
    Instance that's in class
    """
    name = models.CharField(max_length=100)
    class_instance = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


RAW_TYPE_CHOICES = (
    ('string', 'String'),
    ('number', 'Integer'),
    ('float', 'Float'),
    ('boolean', 'Boolean'),
    ('date', 'Date'),
    ('datetime', 'Date Time'),
    ('markdown', 'Markdown'),
    ('image', 'Image'),
    ('file', 'File'),
    ('instance', 'Instance'),
    ('instance_list', 'Instance List'),
    ('json', 'JSON'),
    ('class', 'Class'),
    ('url', 'URL')
)

type_limitation_template = {
    "string": {
        "min_length": 0,
        "max_length": 255
    },
    "number": {
        "min_value": -2147483648,
        "max_value": 2147483647
    },
    "float": {
        "min_value": -2147483648,
        "max_value": 2147483647,
        "decimal_places": 2
    },
    "boolean": {},
    "date": {},
    "datetime": {},
    "markdown": {},
    "image": {},
    "file": {},
    "instance": {
        "class_id": 0
    },
    "instance_list": {
        "allow_class_id_list": []
    },
    "json": {
        "initial_json": {}
    },
    "class": {},
    "url": {}
}


class PropertyType(models.Model):
    """
    Property of the instance
    """
    name = models.CharField(max_length=100)
    class_instance = models.ForeignKey(Class, on_delete=models.CASCADE)
    # raw type is the type that the program will be rendered
    # since in database we can contain only some basic types like string, int, float, etc.
    # but sometime we want to render it as a date, markdown, image, etc.
    # this type the program will know how to render it
    raw_type = models.CharField(max_length=100, choices=RAW_TYPE_CHOICES)
    # limitation is the limitation of the property and will store in JSON format
    # due to the variety of the limitation
    # example of limitation:
    #  - min and max value of number
    #  - min and max length of string
    # this will specify the format by the program
    limitation = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.name


class ObjectPropertyRelation(models.Model):
    """
    Connect instance and property
    """
    instance_object = models.ForeignKey(Instance, on_delete=models.CASCADE)
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    # raw value will passed by the program to the frontend to render the real value
    raw_value = models.CharField(max_length=1000000)

    def __str__(self):
        return str(self.instance_object) + ' - ' + str(self.property_type)
