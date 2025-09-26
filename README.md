# 3002-model
Model Explanation

The Healthy Control (blue line) forms a functional baseline. During the time period of super high stimulation at about 40-45s, the simulated high frequency firing of the CA3 neuron produces the high LTP. This is the reason for the steep learning curve going up. This is controlled by a high learning_rate parameter, representing the high efficiency of the molecular mechanism (such as the activation of the NDA receptor, calcium influx in the cell) that is healthy in the animal and drives the insertion of the AMPA receptor. The resulting high plateau shows the successful and persistent strengthening of the synapse which basically means that memory has been successfully encoded.



The Alzheimer's Disease (AD) model (red dashed line) is an example of a pathological failure of this mechanism. Even though stimulation is the same in both cases, there is negligible potentiation of the synapse. This represents a model of how in early AD pathological factors such as amyloid-beta oligomers can disrupt the function of the NMDA receptor and its downstream signaling processes. This biological impairment is reflected in a dramatically decreased learning_rate and maximum weight (w_max) resulting in a near flat curve that indicates a complete failure to induce LTP, and by extension, a failure to form new long term memories.



The model of AD + Treatment (green dotted line) is the direct test of the research hypothesis. Here, a simulated therapy is used to bring the learning_rate and w_max parameters back to healthy levels. The resulting curve is almost identical to that of the healthy control, showing a complete rescue of LTP. This kind of powerful visualization suggests that a treatment targeting the specific molecular machinery of synaptic plasticity could re-establish the basic ability of the Schaffer collateral pathway to increase the strength of its connections, re-enabling the cellular processes involved in memory consolidation.
