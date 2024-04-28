import math
def checktires(frontRight, frontLeft, rearRight, rearLeft):
    if frontRight >= 35 and frontRight <= 45 and frontLeft >= 35 and frontLeft <= 45 and rearRight >= 35 and rearRight <= 45 and rearLeft >= 35 and rearLeft <= 45 and math.fabs(frontRight - frontLeft) <= 2 and math.fabs(rearRight - rearLeft) <= 2:      # math.fabs() == absolute value
        print("Inflation is GOOD.");
    else:
        print("Inflation is BAD.");

print("Enter tire pressures (right front, left front, right rear, left rear)");
frontRight = float(input());    
frontLeft = float(input());
rearRight = float(input());
rearLeft = float(input());

checktires(frontRight, frontLeft, rearRight, rearLeft)