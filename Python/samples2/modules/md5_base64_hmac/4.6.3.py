# -*- encoding: utf-8 -*-
"""
Koд аутентификации сообщения HMAC
"""
import hmac

m = hmac.new('password')
m.update("Nobody inspects")
m.update(" the spammish repetition")
m.digest()
