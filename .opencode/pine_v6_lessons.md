# Pine Script v6 Syntax Lessons Learned

## 1. `if` blocks cannot be empty (comments don't count as statements)
**Error:** `"if" cannot be used as a variable or function name`
**Cause:** Pine Script requires at least one actual statement inside an `if` block. Comments before a nested `if`/`for` don't count.
**Fix:** Combine conditions directly instead of nesting empty blocks:
```pine
// ❌ WRONG — outer if has only comment before nested if
if barstate.isconfirmed and canCollect
     // Step 1: Update observations
     if array.size(obsType) > 0
          for i = ...

// ✅ RIGHT — combine conditions
if barstate.isconfirmed and canCollect and array.size(obsType) > 0
     for i = ...
```

## 2. Variable declarations inside `if` blocks cause syntax errors
**Error:** `Syntax error at input "int"`
**Fix:** Declare variables at top level, then assign inside `if` blocks:
```pine
// ❌ WRONG
if condition
     int mask = value
     doSomething(mask)

// ✅ RIGHT
mask = value
if condition
     doSomething(mask)
```

## 3. `input.time` requires `const int` literal
**Error:** `Cannot call "input.time" with argument "defval"="call "timestamp" (simple int)"`
**Fix:** Use Unix timestamp literal (milliseconds):
```pine
// ❌ WRONG
evaluationStartTime = input.time(timestamp(2020, 1, 1, 0, 0), "Start date")

// ✅ RIGHT — 1577836800000 = 2020-01-01 00:00:00 UTC in milliseconds
evaluationStartTime = input.time(1577836800000, "Start date")
```

## 4. `shorttitle` max 10 characters
**Error:** `The shorttitle is too long (X characters). It should be 10 characters or less.`

## 5. `?` at end of line works, `:` at end of line does NOT
**Error:** `end of line without line continuation`
**Fix:** Wrap multi-line ternaries in parentheses:
```pine
// ❌ WRONG
x = condition
     ? trueVal
     : falseVal

// ✅ RIGHT
x = (condition
     ? trueVal
     : falseVal)
```

## 6. Lambda/function definitions inside `if` blocks not supported
**Error:** Various syntax errors
**Fix:** Inline the logic or define functions at top level only.

## 7. Comments are not statements
Pine Script treats comments as whitespace, not executable statements. Any construct requiring a statement (if/else/for blocks) must have at least one non-comment line.

## 8. `for i = 0 to -1` executes once in Pine Script
Unlike most languages, `for i = 0 to array.size(arr) - 1` runs once when the array is empty (i=0, then out-of-bounds). Always guard with `if array.size(arr) > 0`.

## 9. Function bodies (`=>`) also need parentheses for multi-line ternaries
**Error:** `end of line without line continuation` inside function body
**Cause:** `=>` provides statement continuation but NOT implicit parentheses for ternary `:` line breaks.
**Fix:** Wrap ternary chain in parentheses inside function bodies:
```pine
// ❌ WRONG — `:` at end of line even inside function body
scoreBand(int score) =>
    score >= 80 ? 3 :
    score >= 70 ? 2 :
    0

// ✅ RIGHT — wrap in parentheses
scoreBand(int score) =>
    (score >= 80 ? 3 :
    score >= 70 ? 2 :
    0)
```

This also applies to nested ternaries — outer parentheses don't help inner levels. Flatten into helper variables or wrap each nesting level separately.

## 10. `for` and `if` cannot be the first statement after comments/blank lines or in an `if` body
**Error:** `"for"/"if" cannot be used as a variable or function name`
**Cause:** When `for` or `if` is the first statement after comments, blank lines, or function definitions, Pine v6's parser tries to interpret the keyword as a variable or function name rather than as the start of a new block/section. This is a variant of Lesson 1 — the parser needs at least one non-keyword statement to recognize the context.
**Fix:** Add a real statement before the keyword:
```pine
// ❌ WRONG — `for` is first statement in if body (after comments only)
if barstate.isconfirmed and canCollect and array.size(obsType) > 0
     for i = array.size(obsType) - 1 to 0
          obs = array.get(obsType, i)

// ❌ WRONG — `if` is first statement after function definitions and comments
segBucketForHV() =>
     (...)  // function body

// comments only
if barstate.isconfirmed and canCollect
     // processing...

// ✅ RIGHT — add a real statement before `for`
if barstate.isconfirmed and canCollect and array.size(obsType) > 0
     obsCount = array.size(obsType)
     for i = obsCount - 1 to 0
          obs = array.get(obsType, i)

// ✅ RIGHT — add a real statement before `if`
segBucketForHV() =>
     (...)

segmentProcessingStart = true
if barstate.isconfirmed and canCollect
     // processing...
```
The parser needs at least one non-keyword statement (variable assignment, function call, etc.) to recognize the block start.

## 11. No type annotations on user-defined function parameters
**Error:** `Syntax error at input "array"` (or similar keyword)
**Cause:** Pine v6 does not support `int`/`float`/`string`/`bool` type annotations in user-defined function parameter lists. The parser may accept them in some positions but fail in others (especially after line ~760). The error often points at a seemingly unrelated keyword (like `array`) because the parser recovers incorrectly.
**Fix:** Use bare parameter names without type annotations:
```pine
// ❌ WRONG — type annotation on parameter
scoreBand(int score) =>
    (score >= 80 ? 3 : score >= 70 ? 2 : 0)

decodeBase4Digit(int packedValue, int divisor) =>
    int(math.floor(packedValue / divisor)) % 4

// ✅ RIGHT — bare parameter names
scoreBand(score) =>
    (score >= 80 ? 3 : score >= 70 ? 2 : 0)

decodeBase4Digit(packedValue, divisor) =>
    int(math.floor(packedValue / divisor)) % 4
```
This applies to ALL type annotations on UDF parameters — `int`, `float`, `string`, `bool`. Variable declarations with type annotations (`int x = ...`) at the top level are fine; only function parameter lists are affected.

## 12. UDFs with side effects only (void) — inline instead
**Error:** `Syntax error at input "array"` (or similar) at a column past the end of the function signature
**Cause:** Pine v6 UDFs defined with `=>` must return a value. Functions that only perform side effects (like `array.set`) with no return value confuse the parser — the error often points at the first keyword inside the body (e.g., `array`) at a column position that doesn't match the line.
**Fix:** Inline the code at every call site instead of using a UDF:
```pine
// ❌ WRONG — void function with side effects
recordSegSignal(bucket) =>
     if bucket >= 0 and bucket < SEG_BUCKET_COUNT
          array.set(segNewSignalCount, bucket, array.get(segNewSignalCount, bucket) + 1)

// ✅ RIGHT — inline at call site
if bucket >= 0 and bucket < SEG_BUCKET_COUNT
     array.set(segNewSignalCount, bucket, array.get(segNewSignalCount, bucket) + 1)
```
If you need a helper that performs side effects AND returns a value, use a ternary with a tuple-like pattern or just inline. Pine v6 does not support void UDFs.

## 13. Statement indentation differs from continuation indentation
Block statements use multiples of four spaces (4, 8, 12, ...). Wrapped calls and expressions must instead use a non-multiple-of-four indentation (for example, five spaces inside a four-space block). This distinction preserves block structure while marking the line as a continuation.
