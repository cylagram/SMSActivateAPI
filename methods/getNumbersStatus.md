getNumbersStatus method
-----------------

Through this method you will be able to see the status of the numbers!

## Using

| params | type    | required |
|-------|----------|----------|
| `country`  | String     | Yes     |

## Example

```python
import smsactivateapi

def call():
    api = smsactivateapi.VOIPGenerator("api_key")
    return api.getNumbersStatus("0")

print call()
```
All response will be in [json](https://www.json.org/json-it.html) format!
