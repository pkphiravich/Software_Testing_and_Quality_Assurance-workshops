#!/usr/bin/env bash

#clear previous runs
rm result.txt
rm -f *.xml
rm -f *.txt

#loop through each test case, to generate result
for i in {1..6}
do
    pytest test_binarysearch.py::test_bi$i --cov --cov-report=xml:coverage$i.xml && \
        echo "passed" >> result.txt || \
        echo "failed" >> result.txt
done

#run tarantula script
python3 tarantula-skeleton.py

