Using basic flask template from:

<https://github.com/hack4impact/flask-base>


### Lessons learned from formatting HTML/CSS for printing

Firefox does not print flexbox content well. If it goes across multiple pages it will simple cut off at a single page.

Chrome is better. Developer tools > ... > Rendering > Emmulate CSS Media > print
Toggle device toolbar (Cmd + Shift + M). Macbook pro 13in is 113 DPI, so 8.5 inches (letter paper) is $$113 * (8.5 - margin_inches). For 4cm margins this is ~782px.
