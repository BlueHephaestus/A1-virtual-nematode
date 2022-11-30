"""
# a script that will convert neurons.py into a data-only file mapping each neuron's synaptic connections.
# so what do we want this to be?
# we have only really 3 values for a given line:
source, dest, weight.

So yea, it's a weighted graph.

Alright we'll be loading it into a dictionary but for now we'll encode it in the most sensical way:

src,dst,w

for every line.
"""
with open("neurons.txt", "w") as nf:
    with open("neurons.py", "r") as f:

        src = None
        for line in f:
            line = line.strip()
            if "def " in line:
                # new src, get
                line = line.replace("():", "")
                src = line.split(" ")[1]
            if "postSynaptic" in line:
                dst = line.split("'")[1]
                w = line.split(" ")[-1]
                nf.write(f"{src} {dst} {w}\n")
                print(src, dst, w)



