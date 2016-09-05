Title: My Other Really Cool Post 3
Date: 2011-12-06 10:20
Category: Python
Tags: nature
Slug: my-other-really-cool-post-3
Authors: Tyler Mulligan
Summary:
    Raindrops on roses
    Whiskers on kittens
    <strong>brown paper packages</strong>

```
import configparser
import argparse
import json
import os
from colour import Color
from math import ceil


def main():

    args = parse_args()

    if args.string:
        phrase = args.string
    else:
        print('string required')
        raise SystemExit

    rb = Rainbow(args.colors, args.start_color, args.end_color, args.format)
    rainbow_text = rb.generate(phrase)

    print(rainbow_text)


class Rainbow(object):
    """A rainbow object that can be applied to a string"""

    def __init__(self, color_count=None, start_color=None, end_color=None, output_format=None):

        conf = parse_config('config.ini')

        self.color_count = int(conf['color_count'])
        self.start_color = conf['start_color']
        self.current_color = conf['start_color']
        self.index = None
        self.end_color = conf['end_color']
        self.output_format = conf['format']
        self.rainbow = []
        self.cpc = 1

        if color_count:
            self.color_count = int(color_count)

        if start_color:
            self.start_color = start_color
            self.current_color = start_color

        if end_color:
            self.end_color = end_color

        if output_format:
            self.output_format = output_format

        with open(conf['formats_file']) as f:
            self.formats = json.loads(f.read())

        if self.output_format in self.formats:
            self.template = self.formats[self.output_format]
        else:
            raise RuntimeError('format not found! Are you sure it exists in ' + conf['formats_file'] + '?')

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.rainbow[self.index]
        except IndexError:
            raise StopIteration

        self.index += 1

        return result
```
