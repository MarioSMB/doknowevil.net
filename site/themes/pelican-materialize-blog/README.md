# pelican-materialize-blog

pelican-materialize-blog is a [pelican](http://blog.getpelican.com/) theme based on [Materialize](http://materializecss.com/), a material design framework.

The theme started off based on [pelican-material](https://github.com/greizgh/pelican-material), so thank you to @greizgh for his contributions.

## Dependencies

Dependencies are statically included.

## Configuration

This template uses a custom filter to sort tags by article count. You need to add this to your config:

```python
from functools import partial
JINJA_FILTERS = {
    'sort_by_article_count': partial(
        sorted,
        key=lambda tags: len(tags[1]),
        reverse=True)} # reversed for descending order
```

Maybe you will probably want to use [pelican-materialbox](https://github.com/greizgh/pelican-materialbox), a pelican plugin to use [materialboxed](http://materializecss.com/media.html#materialbox) from Materialize.

## License

MIT
