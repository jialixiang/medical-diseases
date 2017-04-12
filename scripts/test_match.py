#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import csv
from collections import defaultdict

from config import *
from outliers import unmatched, unknown


if __name__ == "__main__":

    files = [
        u"内科学第八版",
        u"妇产科学第八版",
        u"皮肤性病学第六版",
        u"儿科学第八版",
        u"外科学八年制第二版",
        u"临床医学概论",
    ]

    contents = {}
    for filename in files:
        with open("files/%s.txt" % filename) as txt_file:
            content = txt_file.readlines()
            content = [x.strip().decode("utf-8") for x in content]
            contents[filename] = content

    print len(unmatched)
    print len(unknown)

    title_re = re.compile(u"第[%s]*[章节篇].*" % u"".join(number_words), re.UNICODE)
    subtitle_re = re.compile(u"^[%s]*、.*" % u"".join(number_words), re.UNICODE)
    trititle_re = re.compile(u"([%s]*).*" % u"".join(number_words), re.UNICODE)

    search = False

    results = defaultdict(dict)
    for name in unmatched:
        if name in unknown:
            continue

        gender = u"/"
        age = u"/"

        for filename in files:
            content = contents[filename]
            for txt in content:
                if (re.findall(title_re, txt) or re.findall(subtitle_re, txt) or re.findall(trititle_re, txt)):
                    if name in txt:
                        search = True
                    else:
                        search = False

                if search:
                    # Try search gender key words
                    if any([word in txt for word in gender_words]):
                        for sentence in txt.split(u"。"):
                            if any([word in sentence for word in gender_words]):
                                if gender == u"/":
                                    gender = u""
                                gender += sentence

                    # Try search age key words
                    if any([word in txt for word in age_words]):
                        for sentence in txt.split(u"。"):
                            if any([word in sentence for word in age_words]):
                                if age == u"/":
                                    age = u""
                                age += sentence

        results[name]["gender"] = gender
        results[name]["age"] = age

        # Output results to csv
        with open(u'files/output/其他.csv', 'wb') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([u"疾病名称".encode("utf-8")] + [mapping[k].encode("utf-8") for k in mapping.keys()])

            for name in sorted(results):
                chracters = results[name]
                csv_writer.writerow([name.encode("utf-8")] + [
                    chracters[k].encode("utf-8") if chracters.has_key(k) else u""
                    for k in mapping.keys() \
                ])
