---
layout: docs
title: Resolvers
---

# Overview

The purpose of this resolver is to retrieve the current datetime

## Available Resolvers

### date

Fetches the current datetime in an [ISO 8601 format](https://docs.python.org/3/library/time.html#time.strftime).
The default format is "%Y-%m-%d %H:%M:%S".

Syntax:

```yaml
parameter|sceptre_user_data:
    <name>: !date
```

Examples:

Retrieve date (using default format) and pass it to a
cloudformation parameter:
```
parameters:
    now: !date
```

Retrieve the date (in MM/DD/YYYY format) and pass it to a
cloudformation parameter:
```
parameters:
    now: !date "%m/%d/%Y"
```

Retrieve the time (in H:M:S format) and pass it to a
cloudformation parameter:
```
parameters:
    now: !date "%H:%M:%S"
```
