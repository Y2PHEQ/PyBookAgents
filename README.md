<p align="center">
  <a href="https://github.com/sintxcs">
    <img src="https://raw.githubusercontent.com/sintxcs/PyBookAgents/main/assets/PyBookAgents.jpg" alt="Logo">
  </a>
  <p align="center">
    Random user agents generator for Facebook. It has 4 options: Dalvik, iPhone, Android, and Random (it's either Android or iPhone).
</p>

## Terminal Installation
```ruby
pip3 install git+https://github.com/sintxcs/PyBookAgents.git
```

## Importing the module in your script
```python
try:
    import PyBookAgents
except ModuleNotFoundError:
    os.system("pip3 install git+https://github.com/sintxcs/PyBookAgents.git)
    import PyBookAgents
```

## Dalvik User Agent
```python
from PyBookAgents import dalvik_ugen

Input Example:
print(PyBookAgents.dalvik_ugen())

Output Example:
>> Dalvik/2.1.0 (Linux; U; Android 12.0.0; OnePlus Build/MYJY.211413.014 [FBAN/FB4A;FBAV/220.0.0.47115;FBBV/317123424;FBDM/FBDM/{density=2.1,width=1814,height=1023};FBLC/hu_HU;FBRV/317123424;FBCR/Metfone;FBMF/OnePlus;FBBD/OnePlus_8_Pro;FBPN/com.facebook.lite;FBDV/OnePlus_8_Pro;FBSV/9;FBOP/19;FBBK/4;FBCA/x86_64:x86:arm64-v8a;]
```

## iPhone User Agent
```python
from PyBookAgents import iphone_ugen

Input Example:
print(PyBookAgents.iphone_ugen())

Output Example:
>> Mozilla/5.0 (iPhone; CPU iPhone OS 6_7_2 like Mac OS X) AppleWebkit/509.1.15 (KHTML, like Gecko) Mobile/21B101 [FBAN/FBIOS;FBAV/445.0.0.35.117;FBBV/548375166;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/6_7_2;FBSS/3;FBID/phone;FBLC/lo_LA;FBOP/30;FBRV/554305165]
```

## Android User Agent
```python
from PyBookAgents import android_ugen

Input Example:
print(PyBookAgents.android_ugen())

Output Example:
>> Mozilla/5.0 (Linux; Android 13.0.0; OnePlus Build/CH92.213488.013; wv) AppleWebkit/512.27 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5362.121 Mobile Safari/435.33 Instagram 312.1.0.34.111 Android (34/14; 420dpi; 1080x2133; oneplus; OnePlus_8_Pro; r0s; s5e9925; de_DE; 553971276)

or

>> Mozilla/5.0 (Linux; Android 9.0.0; Realme Build/YDCQ.214379.010; wv) AppleWebkit/598.28 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5872.119 Mobile Safari/536.29 [FB_IAB/FB4A;FBAV/445.0.0.34.118;]
```

## Random: iPhone & Android
```python
from PyBookAgents import random_ugen

Input Example:

print(PyBookAgents.random_ugen())

Output Example:
>> It's either Android or iPhone User Agent
```
> **Disclaimer**: For educational purposes only. I won't take any responsibility if any users take advantage of this and exploit it for illicit activities.


## Social Links
[Facebook](https://facebook.com/sintxcs) • [Telegram](https://t.me/syntxcs)
