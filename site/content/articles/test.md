Title: My First Review
Date: 2014-03-12 10:20
Category: Review
Image: test.jpg

Following is a `review` of my favorite mechanical keyboard.

There are two ways to specify the identifier:

```python
print("The triple-colon syntax will *not* show line numbers.")
```

To display line numbers, use a path-less shebang instead of colons:

```python
print("The path-less shebang syntax *will* show line numbers.")
```

these

``` jinja
<header>
  <nav class="blue-grey darken-3" role="navigation">
    <div class="nav-wrapper container">
      <a href="{{SITEURL}}" class="brand-logo">{{SITENAME}}</a>
      <a href="#" data-activates="mobile-nav" class="button-collapse"><i class="mdi-navigation-menu"></i></a>
      <ul id="dropdown" class="dropdown-content">
        {% if DISPLAY_CATEGORIES_ON_MENU %}
        {% for cat, null in categories %}
        <li
        {% if cat == category %} class="active"{% endif %}><a class="truncate" href="{{ SITEURL }}/{{ cat.url }}">{{ cat }}</a></li>
        {% endfor %}
        {% endif %}
      </ul>
      <ul class="right hide-on-med-and-down">
        <li><a class="dropdown-button" href="#!" data-activates="dropdown">Categories <i class="mdi-navigation-arrow-drop-down right"></i></a></li>
        <li><a href="{{SITEURL}}/archives.html">Archives</a></li>
      </ul>
      <ul id="mobile-nav" class="side-nav">
        {% if DISPLAY_CATEGORIES_ON_MENU %}
        {% for cat, null in categories %}
        <li
        {% if cat == category %} class="active"{% endif %}><a href="{{ SITEURL }}/{{ cat.url }}">{{ cat }}</a></li>
        {% endfor %}
        {% endif %}
        <li><a href="{{SITEURL}}/archives.html">Archives</a></li>
      </ul>
    </div>
  </nav>
</header>
```
