# INPUT: observation of context, group, individuals
observe(context, group, individuals)

# Step 1: Detect violations (boundary / norm crossings)
violated_boundary = detect_violation(context, group, individuals)

if violated_boundary == NONE:
    maintain_connection()  # keep trust, openness
    return

# Step 2: Classify violation type
if violation_affects("other"):
    violation_type = "OTHER"
elif violation_affects("group"):
    violation_type = "WE"
elif violation_affects("self"):
    violation_type = "SELF"
else:
    violation_type = "UNKNOWN"

# Step 3: Evaluate benignity factors
benignity = evaluate_benignity(
    alternative_norms = check_alternative_norms(violated_boundary),
    commitment        = check_commitment_to_norm(violated_boundary),
    distance          = check_psychological_distance(context, violated_boundary)
)

if not benignity:
    # Serious violation → prioritize protection
    respond_with_protection(violation_type)
    return

# Step 4: Select response mode + attitude
if violation_type == "OTHER":
    response_mode = "GENTLENESS"   # respectful correction
    attitude      = COMPASSION     # warmth, empathy
elif violation_type == "WE":
    response_mode = "PLAY"         # co-exploration, shared fun
    attitude      = CURIOSITY      # openness to explore
elif violation_type == "SELF":
    response_mode = "HUMOR"        # self-deprecating lightness
    attitude      = HUMILITY       # reduce ego, invite safety
else:
    response_mode = "REFLECTION"   # meta-communication
    attitude      = OPENNESS       # admit uncertainty

perform_response(response_mode, attitude)

# Step 5: Update outcomes dynamically
update_outcomes(
    trust_level       = measure_trust(),
    openness_level    = measure_openness(),
    critical_thinking = measure_group_reflection(),
    creativity        = measure_idea_generation()
)


