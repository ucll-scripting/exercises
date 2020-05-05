# Assignment

The file `input.json` contains the grades of students for multiple tests throughout the semester in JSON-format.
For example:

```json
[
    { "id": "r0077959", "grades": [6, 8, 14, 5, 5, 8, 9, 6, 8]} ,
    { "id": "r0056617", "grades": [10, 13, 12, 19, 19, 18] }
]
```

We'd like to transform this data into an XML-like format.
The above example would thus become

```xml
<students>
<student id="r0056617"><grades><grade>10</grade><grade>13</grade><grade>12</grade><grade>19</grade><grade>19</grade><grade>18</grade></grades></student>
<student id="r0077959"><grades><grade>6</grade><grade>8</grade><grade>14</grade><grade>5</grade><grade>5</grade><grade>8</grade><grade>9</grade><grade>6</grade><grade>8</grade></grades></student>
</students>
```

* One student per line.
* The order of the students must be preserved.
* Each student data is surrounded by `<student id="...">...</student>`
* Inside the `student` tags must be a `<grades>...</grades>` tag.
* For each grade `g` there must be a corresponding `<grade>g</grade>` between the `grades` tags.
* The order of the grades must be preserved.
* Make sure there are no redundant characters. E.g. extra spaces are not allowed.
* Surround the entirety with `<students>` and `</students>` tags.
* Do *not* add indentation. Reproduce the data exactly as shown above.
