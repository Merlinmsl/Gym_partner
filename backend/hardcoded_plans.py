def get_hardcoded_plan(goal):
    if goal == "Body Type 1":
        return "Schedule 1:\n- 5x/week cardio\n- Moderate calories\n- Lean protein\n- Bodyweight circuits"
    elif goal == "Body Type 2":
        return "Schedule 2:\n- 4x/week weightlifting\n- High protein\n- Calorie surplus\n- Progressive overload"
    elif goal == "Body Type 3":
        return "Schedule 3:\n- Mixed workouts\n- Balanced diet\n- Focus flexibility and core"
    else:
        return "Default plan: maintain activity and eat balanced meals."
