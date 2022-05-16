def transpose(data):
    output = []
    if isinstance(data, dict):
        keys = tuple(data.keys())
        values = tuple(data.values())
        output.append(keys)
        output.append(values)
    else:
        names = []
        since_days = []
        karma_points = []
        bitecoin_earned = []
        for member in data:
            names.append(member.name)
            since_days.append(member.since_days)
            karma_points.append(member.karma_points)
            bitecoin_earned.append(member.bitecoin_earned)
        output.append(tuple(names))
        output.append(tuple(since_days))
        output.append(tuple(karma_points))
        output.append(tuple(bitecoin_earned))
    return output
