# wikipedia-network-analysis:
Tools for analyzing wikipedia using network and graph theory.

#Project Overview:
Python Script for gathering all wikipedia articles starting with the letter 'A', storing the results, then performing calculations with the NetworkX
(and potentially other) modules.

#File Structure:
- master.py
    - Controls all other scripts
- retriever.py
    - Selects an article to start from
    - If article has been seen,
        - Discard article
    - Else
        - Add target to seen list
    - Retrieves wikipedia article (starting with the letter A)
    - Pass the resulting object to parser.py
- parser.py
    - Takes the python object from retriever.py
    - Iterate across list:links[], finding all target links that start with 'A', pass link to writer.py
    - If this target has been seen,
        - discard target
    - Else
        - Add target to retriever queue
- writer.py
    - Takes link from parser.py
    - Appends to network.csv
    