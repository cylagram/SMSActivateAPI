getNumber method
-----------------

Through this method you can buy a number with the account balance associated with the apy_key!

## Using

| params | type    | required |
|-------|----------|----------|
| `service`  | String     | Yes     |
| `country`  | String     | Yes     |

## Example

```python
import smsactivateapi

def call():
    api = smsactivateapi.VOIPGenerator("api_key")
    return api.getNumber("tg","2")

print call()
```
All response will be in [json](https://www.json.org/json-it.html) format!
