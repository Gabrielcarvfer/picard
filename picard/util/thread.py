# -*- coding: utf-8 -*-
#
# Picard, the next-generation MusicBrainz tagger
#
# Copyright (C) 2006-2007 Lukáš Lalinský
# Copyright (C) 2008 Gary van der Merwe
# Copyright (C) 2011-2013 Michael Wiencek
# Copyright (C) 2013, 2018 Laurent Monin
# Copyright (C) 2016 Sambhav Kothari
# Copyright (C) 2017 Sophist-UK
# Copyright (C) 2018 Vishal Choudhary
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.


import sys
import traceback
from threading import Event

from PyQt5.QtCore import (
    QCoreApplication,
    QEvent,
    QRunnable,
)


class ProxyToMainEvent(QEvent):

    def __init__(self, func, event=None, *args, **kwargs):
        super().__init__(QEvent.User)
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.event = event

    def run(self):
        if self.event and self.event.isSet():
            return
        self.func(*self.args, **self.kwargs)
        if self.event:
            self.event.set()


class Runnable(QRunnable):

    def __init__(self, func, next_func, traceback=True):
        super().__init__()
        self.func = func
        self.next_func = next_func
        self.traceback = traceback

    def run(self):
        try:
            result = self.func()
        except BaseException:
            from picard import log
            if self.traceback:
                log.error(traceback.format_exc())
            if self.next_func:
                to_main(self.next_func, error=sys.exc_info()[1])
        else:
            if self.next_func:
                to_main(self.next_func, result=result)


def run_task(func, next_func=None, priority=0, thread_pool=None, traceback=True):
    if thread_pool is None:
        thread_pool = QCoreApplication.instance().thread_pool
    thread_pool.start(Runnable(func, next_func, traceback), priority)


def to_main(func, *args, **kwargs):
    event = Event()
    QCoreApplication.postEvent(QCoreApplication.instance(),
                               ProxyToMainEvent(func, event, *args, **kwargs))
    return event