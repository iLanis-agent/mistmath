import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)
def round0(x): return jsnum(math.floor(x + 0.5))

ML_PER_M3 = 30

def mist_plan(areaM2, ceilingM):
    if not (areaM2 > 0) or not (ceilingM > 0):
        return {"error": "the room and the ceiling must be positive"}
    ml = round0(areaM2 * ceilingM * ML_PER_M3)
    if ml <= 1500: verdict = "a tabletop unit"
    elif ml <= 4000: verdict = "a console job"
    else: verdict = "a whole-house conversation"
    return {"ml": ml, "verdict": verdict}

def tank_plan(mlPerDay, tankL):
    if not (mlPerDay > 0) or not (tankL > 0):
        return {"error": "the mist and the tank must be positive"}
    days = round1(tankL * 1000 / mlPerDay)
    if days >= 2: verdict = "an every-other-day job"
    elif days >= 1: verdict = "a daily top-up"
    else: verdict = "a twice-a-day chore"
    return {"days": days, "verdict": verdict}

def wick_plan(hoursPerDay, wickLifeH):
    if not (hoursPerDay > 0) or not (wickLifeH > 0):
        return {"error": "the hours and the wick must be positive"}
    days = math.floor(wickLifeH / hoursPerDay)
    if days >= 90: verdict = "a full season"
    elif days >= 45: verdict = "half a season"
    else: verdict = "a monthly consumable"
    return {"days": days, "verdict": verdict}

def render_mist(r, areaM2, ceilingM):
    return ("Your " + fmt(areaM2) + " m2 room with a " + fmt(ceilingM) + " m ceiling asks for " + fmt(r["ml"])
            + " mL a day - " + r["verdict"] + ".")

def render_tank(r, mlPerDay, tankL):
    every = "every day" if r["days"] == 1 else "every " + fmt(r["days"]) + " days"
    return (fmt(mlPerDay) + " mL a day from a " + fmt(tankL) + " L tank is a refill " + every
            + " - " + r["verdict"] + ".")

def render_wick(r, hoursPerDay, wickLifeH):
    return ("A labeled " + fmt(wickLifeH) + " h wick at " + fmt(hoursPerDay) + " h a day lasts " + fmt(r["days"])
            + " days - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[20,2.4],[40,2.7],[60,3],[12,2.4],[25,2.5],[35,2.8],[15,2.2],[50,3],[0,2.4],[20,0]]:
    add("mistPlan", mist_plan, render_mist, a)
for a in [[1440,4],[3240,6],[864,2],[2160,1.5],[4500,6],[1200,3],[2000,2],[900,4],[0,4],[1440,0]]:
    add("tankPlan", tank_plan, render_tank, a)
for a in [[10,720],[24,720],[8,720],[12,720],[6,720],[16,720],[4,720],[20,720],[0,720],[10,0]]:
    add("wickPlan", wick_plan, render_wick, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
