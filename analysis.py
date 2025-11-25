import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
efficiency = [76.57, 71.85, 75.65, 76.89]
average_efficiency = np.mean(efficiency)
industry_target = 90

# Print the average to verify
print(f"Average Equipment Efficiency: {average_efficiency:.2f}")

# Visualization
fig, ax = plt.subplots()
bar_width = 0.5
index = np.arange(len(quarters))

bars = ax.bar(index, efficiency, bar_width, label='Quarterly Efficiency')

# Add the industry target line
ax.axhline(y=industry_target, color='r', linestyle='--', label=f'Industry Target ({industry_target}%)')

ax.set_xlabel('Quarter')
ax.set_ylabel('Efficiency Rate (%)')
ax.set_title('Quarterly Equipment Efficiency vs. Industry Target')
ax.set_xticks(index)
ax.set_xticklabels(quarters)
ax.set_ylim(0, 100)
ax.legend()

# Add data labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.2f}', va='bottom', ha='center')


plt.tight_layout()

# Save the figure
plt.savefig('equipment_efficiency.png')

print("Analysis complete. Chart saved to equipment_efficiency.png")
