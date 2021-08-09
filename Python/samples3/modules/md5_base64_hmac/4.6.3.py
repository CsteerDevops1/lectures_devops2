#!/usr/bin/env python3
"""
Koд аутентификации сообщения HMAC
"""
import hmac

m = hmac.new(key=b"password", digestmod="sha1")
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
print(m.digest())
