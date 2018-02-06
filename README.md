SMSActivateAPI
==============
A simple library to management of your personal sms-activate.ru account!


Installation
------------

Installing this library is very easy!
```sh
sudo apt-get install git
sudo git https://github.com/cylagram/SMSActivateAPI.git
```

Usage
-----------

To use this library you do not need a great knowledge of python!
Let's start by instantiating the class:
```python
import smsactivateapi

sms = VOIPGenerator("your_api_token")   #you can find the api_token in your smsactivate account!
print sms.getBalance()
```

Methods
-------

Available methods of this library:

- [x] [getNumbersStatus](https://github.com/cylagram/SMSActivateAPI/blob/master/methods/getNumbersStatus.md)
- [x] [getBalance](https://github.com/cylagram/SMSActivateAPI/blob/master/methods/getBalance.md)
- [x] [getNumber](https://github.com/cylagram/SMSActivateAPI/blob/master/methods/getNumber.md)
- [x] getStatus
- [ ] setStatus


Errors
------

In the lib some error codes have been **implemented** with which you will be able to recognize exceptions quickly and easily!
Here is a list! The error will also be described in the response of the **method** when called!

» `306` •  Service not inserted, put one!<br />
» `400` •  The api_key is invalid. Try with another!<br />
» `401` •  Country invalid, use another!<br />
» `402` •  The api_key is missing!<br />
» `403` •  The activation ID does not exist!<br />


Support
-------

If you need help, do not worry about creating a **issue** or join [group](https://t.me/Hamstry) of telegram!
