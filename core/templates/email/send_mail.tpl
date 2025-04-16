{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ name }}
{% endblock %}

{% block html %}
This is an <strong>html</strong> message.
<img src="https://www.malibumakos.com/wp-content/uploads/2018/07/ocean-waves-1000x675-1000x675.jpg">
{% endblock %}