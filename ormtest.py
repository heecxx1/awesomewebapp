#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'测试'

__author__ = 'Xinxin'

import asyncio
import orm as orm
from ormshiti import User, Comment

user = User(id=1213,name='Xinxin')
user.save()
users = User.findall()
raise (user[1])



