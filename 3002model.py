#1 All the important imports
import numpy as np  # for the calculations

import matplotlib.pyplot as plt #  for creating plots

# 2. DEFINE SIMULATION PARAMETERS FOR EACH CONDITION
# This section defines parameter sets for three distinct biological conditions:
# Healthy, Alzheimer's Disease (AD), and AD with Treatment.

def setup_parameters():
    """
    Sets up parameter dictionaries for all simulation conditions.
    Returns:
        dict: A dictionary containing parameter sets for each condition.
    """
    # Shared Parameter
    # These parameters are the same for all conditions
    base_params = {
        'total_time': 100,         # Total simulation duration in seconds
        'dt': 0.1,                 # Time step in seconds
        'w_initial': 1.0,          # Initial synaptic weight is the same for all
        'tetanus_start': 40,       # Stimulation starts at the same time
        'tetanus_end': 45          # Stimulation ends at the same time
    }

    # Condition-Specific Parameters 
    params = {
        'Healthy': {
            **base_params, # Inherit shared parameters
            'w_max': 2.5,              # Max synaptic weight in a healthy neuron
            'learning_rate': 0.5,      # Normal rate of potentiation
        },
        'AD': {
            **base_params,
            # In our AD model, the ability to strengthen the synapse is severely impaired.
            'w_max': 1.2,              # Max weight is much lower
            'learning_rate': 0.05,     # Learning rate is 10x slower
        },
        'AD + Treatment': {
            **base_params,
            # The treatment is modeled as restoring the synaptic parameters to healthy levels.
            'w_max': 2.5,
            'learning_rate': 0.5,
        }
    }
    return params


# 3. RUN THE LTP SIMULATION 

# This function is flexible and works for any set of parameters we give it.
# We will simply call it three times, once for each condition.

def run_ltp_simulation(params):
    """
    Simulates the change in synaptic weight over time based on a given set of parameters.
    Args:
        params (dict): A dictionary containing the parameters for one condition.
    Returns:
        tuple: A tuple containing the time array and the synaptic_weight array.
    """
    time_steps = np.arange(0, params['total_time'], params['dt'])
    synaptic_weight = np.zeros(len(time_steps))
    synaptic_weight[0] = params['w_initial']

    for i in range(len(time_steps) - 1):
        current_time = time_steps[i]
        current_weight = synaptic_weight[i]

        if params['tetanus_start'] <= current_time < params['tetanus_end']:
            # LTP induction rule
            dw = params['learning_rate'] * (params['w_max'] - current_weight) * params['dt']
            synaptic_weight[i+1] = current_weight + dw
        else:
            # Stable weight outside of stimulation
            synaptic_weight[i+1] = current_weight

    return time_steps, synaptic_weight


# 4. PLOT THE COMPARATIVE RESULTS
# ==============================================================================
# This function is updated to plot the results from all three simulations
# on a single graph for direct comparison.

def plot_comparative_results(all_results, params):
    """
    Generates a comparative plot of synaptic weight vs. time for all conditions.
    Args:
        all_results (dict): A dictionary containing the simulation results for each condition.
        params (dict): The main parameter dictionary for labeling.
    """
    plt.figure(figsize=(12, 8)) # Create a figure

    # --- Plot each condition with a different color and style ---
    plt.plot(all_results['Healthy']['time'], all_results['Healthy']['weight'],
             label='Healthy Control', color='royalblue', linewidth=2.5)
    
    plt.plot(all_results['AD']['time'], all_results['AD']['weight'],
             label='Alzheimer\'s Disease (AD)', color='firebrick', linewidth=2.5, linestyle='--')
    
    plt.plot(all_results['AD + Treatment']['time'], all_results['AD + Treatment']['weight'],
             label='AD + Treatment', color='forestgreen', linewidth=2.5, linestyle=':')

    # --- Add labels and title ---
    plt.title('Comparative Model of LTP Under Different Conditions', fontsize=16)
    plt.xlabel('Time (s)', fontsize=12)
    plt.ylabel('Synaptic Weight (Arbitrary Units)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)

    # --- Add shaded region for stimulation period ---
    # Using the 'Healthy' params for this as it's the same for all
    tetanus_start = params['Healthy']['tetanus_start']
    tetanus_end = params['Healthy']['tetanus_end']
    plt.axvspan(tetanus_start, tetanus_end, color='salmon', alpha=0.4, label='Tetanic Stimulation')

    plt.ylim(0, params['Healthy']['w_max'] + 0.5)
    plt.legend(fontsize=11) # Display the legend
    plt.show()

# ==============================================================================
# 5. MAIN EXECUTION BLOCK
# ==============================================================================
if __name__ == '__main__':
    # 1. Get all parameter sets
    all_params = setup_parameters()
    
    # 2. Create a dictionary to store results
    results = {}
    
    # 3. Loop through each condition, run the simulation, and store the results
    for condition_name, condition_params in all_params.items():
        time, weight = run_ltp_simulation(condition_params)
        results[condition_name] = {'time': time, 'weight': weight}
        
    # 4. Plot all the results together
    plot_comparative_results(results, all_params)
