# doknowevil.net

I wanted a statically generated blog. I started with [pelican](http://blog.getpelican.com/), and made a theme.

![dke theme](dke.png)

## Using

Standard Pelican stuff. You must be in the `site` directory. This assumes you have Pelican installed or are in a venv with Pelican installed.

### Build

```
make clean
make html
```

### Development

Start up the live-reload development server with:

```
make serve
```

Then visit: [http://localhost:8000](http://localhost:8000)

## License

MIT