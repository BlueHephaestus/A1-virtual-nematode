Mostly used the c. elegans connectome project, built on that gopigo code,

improved several bugs and overall have it considerably improved - i was modifying the neuron implementation in order 
for it to work better with evolutionary algorithms as a continuous time recurrent network (CTRNN), but then 
ended up re-inventing NEAT, or at least getting far enough in my own designs of it that I realized I was yet again
coming upon NEAT, or Neuro Evolution of Augmenting Topologies. That's the method for evolving the nematode's connectome 
i was thinking about, and I haven't implemented that yet because I got into CTRNN derivations and came up with 
an idea for one that could modify itself while alive, and I like that a lot more than the evolutionary approach
so i'm working on that at the moment and calling it A2. Not sure if it's better than this
model in terms of making an AGI, but it's the next step i'm taking forward in terms of network and model design.

The nice thing about all of this is the parts - the nematode connectome, virtual environments, NEAT CTRNN implementations, the A2 self-mod network,
all of them are modular parts that can be combined in different ways. 

So A2 is starting to implement CTRNN derivations for selfmod, and that's where i'm leaving this repo for now.

EDIT: Actually I don't feel I understand exactly why CTRNNs would be better than normal RNNs (I just understood that continous-time was different than I thought), and normal discrete time RNNs are what I have been designing and using so far, so i'm going to continue with normal RNNs. (also that's what the connectomes use)

On to Model A-2!