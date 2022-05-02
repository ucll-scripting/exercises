# Assignment
"""
Python strings hide few surprises.
Scripting generally involves some form of string processing,
so it is advisable to familiarize yourself with the built-in functionality.

Translate the function below that, given three integers `h`, `m` and `s`,
uses them to construct a string of the form `h:m:s`. All numbers must
count exactly two digits. E.g., `format_time(1,2,3)` must produce `01:02:03`, not `1:2:3`.

```javascript
function formatTime(h, m, s) {
	const hstr = `${h}`.padStart(2, "0");
	const mstr = `${m}`.padStart(2, "0");
	const sstr = `${s}`.padStart(2, "0");

	return `${hstr}:${mstr}:${sstr}`;
}
```"""
def format_time(h, m, s):
    hstr = f'{h}'.rjust(2, "0")
    mstr = f'{m}'.rjust(2, "0")
    sstr = f'{s}'.rjust(2, "0")
    return f'{hstr}:{mstr}:{sstr}'
