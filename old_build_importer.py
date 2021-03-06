#!/usr/bin/env python2

import koji
import json

from retask import Task
from retask import Queue

from darkimporter.libimporter import get_redis_config

def find_builds(oldid, newid):
    """

    :param oldid: The id to start from
    :param newid: The id to end
    :return: None
    """
    koji_session = koji.ClientSession("http://koji.fedoraproject.org/kojihub/")


    config = get_redis_config()
    jobqueue = Queue('jobqueue', config)
    jobqueue.connect()

    for i in range(oldid, newid + 1):
        build_rpms = koji_session.listBuildRPMs(i)
        if build_rpms:
            r1 = build_rpms[0]
            release = r1['release'].split('.')[-1]
            if release == 'el5':
                continue
            print i, release # Enqueue the job here.
            info = {
                'build_id': i,
                'instance': 'primary',
                'release': release,
            }

            task = Task(info)
            enqueue(task)
        else:
            print "Missing: ", i


if __name__ == '__main__':
    find_builds(596268,  606268)
