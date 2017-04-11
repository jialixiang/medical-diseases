#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import csv
from collections import defaultdict

from config import *

# Characters needed:
# 性别; 年龄段


if __name__ == "__main__":


    title_re = re.compile(u"第[%s]*[章节篇].*" % u"".join(number_words), re.UNICODE)

    for filename in [u"内科学第八版", u"妇产科学第八版", u"皮肤性病学第六版", u"儿科学第八版"]:

        results = defaultdict(dict)

        with open("files/%s.txt" % filename) as txt_file:
            content = txt_file.readlines()

        current_title = None

        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip().decode("utf-8") for x in content]
        for txt in content:
            #if txt.startswith(u"第") and (u"节 " in txt or u"章 " in txt):
            if re.findall(title_re, txt):
                name = u"".join(re.split(u"[章节篇]", txt)[1:])
                # Replace space and tab in unicode
                name = name.replace(" ", "").replace("\t", "")

                if name in filter_words or len(name) > 50:
                    current_title = None
                    continue

                current_title = name
                gender = u""
                age = u""

            elif current_title:

                # Try search gender key words
                if any([word in txt for word in gender_words]):
                    for sentence in txt.split(u"。"):
                        if any([word in sentence for word in gender_words]):
                            gender += sentence

                    results[current_title]["gender"] = gender

                # Try search age key words
                if any([word in txt for word in age_words]):
                    for sentence in txt.split(u"。"):
                        if any([word in sentence for word in age_words]):
                            age += sentence

                    results[current_title]["age"] = age

        # Output results to csv
        with open(u'files/output/%s.csv' % filename, 'wb') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([u"疾病名称".encode("utf-8")] + [mapping[k].encode("utf-8") for k in mapping.keys()])

            for name in sorted(results):
                chracters = results[name]
                csv_writer.writerow([name.encode("utf-8")] + [
                    chracters[k].encode("utf-8") if chracters.has_key(k) else u""
                    for k in mapping.keys() \
                ])
