targetSteps=10000
currentSteps=0
gh=0
while currentSteps<targetSteps:
    step=input()
    if(step=="Going home"):
        lastStep=int(input())
        currentSteps+=lastStep
        gh=1
        break
    else:
        currentSteps+=int(step)

if(currentSteps<targetSteps):
    print(f"{targetSteps-currentSteps} more steps to reach goal.")
else:
    print(f"Goal reached! Good job!\n{currentSteps-targetSteps} steps over the goal!" )