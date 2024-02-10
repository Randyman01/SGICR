from django import template

register = template.Library()

@register.filter
def add_class(value, css_class):
    css_classes = value.field.widget.attrs.get('class', '')
    if css_classes:
        css_classes += f' {css_class}'
    else:
        css_classes = css_class
    return value.as_widget(attrs={'class': css_classes})
@register.filter
def attr(value, attr_value):
    # Ensure that value is a form field and has a widget
    if hasattr(value, 'field') and hasattr(value.field, 'widget'):
        # Split the attr_value into attribute name and value
        attr_name, attr_value = attr_value.split(':',  1)

        # Update the widget's attributes with the new attribute
        value.field.widget.attrs[attr_name] = attr_value

    return value
