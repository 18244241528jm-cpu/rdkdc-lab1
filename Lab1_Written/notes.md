# Lab1 Experimental Report

## Task 1: UR5(e) Simulation

### Execution Commands
```bash
# Start simulation
ros2 launch rdkdc ur5e_simulation.launch.py

# Run control script
python Lab1_Code/lab1_1.py
```

### Key Parameters
- `UR_MAX_DELTA=0.05`: Maximum joint angle change (radians)
- `UR_DT_MARGIN=0.90`: Time interval safety margin
- `UR_DT_FLOOR=0.8`: Minimum time interval

### Queuing vs Non-Queuing Behavior
- **Non-Queuing**: Rapid successive calls overwrite previous targets, intermediate waypoints may not be reached
- **Queuing**: Wait for previous motion to complete before sending new target, ensuring all waypoints are reached

## Task 2: Matrices and Functions

### Function Implementation Details

#### ROTX/ROTY/ROTZ
- Basic rotation matrices using standard trigonometric formulas
- Numerically stable with proper boundary case handling

#### EULERXYZ/EULERXYZINV
- Euler angle transformation: R = Rx(a) @ Ry(b) @ Rz(c)
- Inverse transformation handles gimbal lock cases (when |cos(b)| ≈ 0)
- Displays warning and gracefully handles singular conditions

#### SKEW3/SKEW6
- Skew-symmetric matrices for screw representation
- SKEW6 handles 6D twist vectors

#### EXPCR/EXPCF
- Implemented using Rodrigues' rotation formula
- Handles boundary cases for pure translation and pure rotation
- Numerically stable, avoids division by zero

#### FINV
- Exploits special structure of homogeneous transformation matrices
- Uses R.T and -R.T@t formulas, avoiding direct matrix inversion

### Numerical Verification
All functions passed numerical precision tests:
- Euler angle round-trip error < 1e-15
- Rotation matrix orthogonality verification passed
- Homogeneous transformation inversion precision < 1e-15

### Implementation Notes
- All functions include comprehensive error handling
- Numerical stability considerations for edge cases
- Proper documentation and type hints
- Compatible with standard robotics libraries
