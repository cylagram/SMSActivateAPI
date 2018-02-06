getBalance method
-----------------

Through this method you will know the balance of the account associated with the api_key!

## Using

| params | type    | required |
|-------|----------|----------|
| `None`  | None     | None     |

## Example

```python
import smsactivateapi

def call():
    api = VOIPGenerator("api_key")
    return api.getBalance()

print call()
```
All response will be in [json](https://www.json.org/json-it.html) format!
